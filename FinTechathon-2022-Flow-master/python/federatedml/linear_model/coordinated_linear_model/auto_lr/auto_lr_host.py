#
#  Copyright 2019 The FATE Authors. All Rights Reserved.
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.
#
import copy

from federatedml.framework.hetero.procedure import convergence
from federatedml.framework.hetero.procedure import paillier_cipher, batch_generator
from federatedml.linear_model.coordinated_linear_model.logistic_regression.hetero_logistic_regression.hetero_lr_base import \
    HeteroLRBase
from federatedml.linear_model.linear_model_weight import LinearModelWeights
from federatedml.optim.gradient import hetero_lr_gradient_and_loss
from federatedml.param.auto_sshe_lr_param import AutoSSHELRParam
from federatedml.transfer_variable.transfer_class.auto_lr_transfer_variable import AutoLRTransferVariable
from federatedml.util import LOGGER
from federatedml.util import consts


class AutoLRHost(HeteroLRBase):
    def __init__(self):
        super(AutoLRHost, self).__init__()
        self.model_param = AutoSSHELRParam()
        self.weight_list = []
        self.batch_num = None
        self.batch_index_list = []
        self.role = consts.HOST
        self.auto_transfer_variables = AutoLRTransferVariable()
        self.current_trial = 0
        self.n_iter_ = 0

        self.cipher = paillier_cipher.Host()
        self.batch_generator = batch_generator.Host()
        self.gradient_loss_operator = hetero_lr_gradient_and_loss.Host()
        self.converge_procedure = convergence.Host()

    def _init_model(self, params):
        self.model_param = self.auto_transfer_variables.trial_param.get(suffix=('init_model',))[0]
        super()._init_model(self.model_param)
        self.n_iters = params.n_iters
        self.trial_num = params.trial_num
        self.need_prone = params.need_prone

    def fit(self, data_instances, validate_data=None):
        """
        Train lr model of role host
        Parameters
        ----------
        data_instances: Table of Instance, input data
        """

        LOGGER.info("Enter hetero_logistic_regression host")
        # self.header = self.get_header(data_instances)
        self.prepare_fit(data_instances, validate_data)

        classes = self.one_vs_rest_obj.get_data_classes(data_instances)

        if len(classes) > 2:
            self.need_one_vs_rest = True
            self.need_call_back_loss = False
            self.one_vs_rest_fit(train_data=data_instances, validate_data=validate_data)
        else:
            self.need_one_vs_rest = False
            self.fit_binary(data_instances, validate_data)

    def fit_n_iters(self, start_iters, data_instances, validate_data):
        LOGGER.warn("start fit_n_iters: start_iters = {}".format(start_iters))
        # self.model_param = self.auto_transfer_variables.trial_param.get(suffix=(self.current_trial, ))[0]
        super()._init_model(self.model_param)
        model_shape = self.get_features_shape(data_instances)
        self.cipher_operator = self.cipher.gen_paillier_cipher_operator(suffix=(self.current_trial, ))

        self.batch_generator.initialize_batch_generator(data_instances, shuffle=self.shuffle, suffix=(self.current_trial, ))
        if self.batch_generator.batch_masked:
            self.batch_generator.verify_batch_legality(least_batch_size=model_shape, suffix=(self.current_trial, ))


        self.gradient_loss_operator.set_total_batch_nums(self.batch_generator.batch_nums)
        w = self.initializer.init_model(model_shape, init_params=self.init_param_obj)
        self.model_weights = LinearModelWeights(w, fit_intercept=self.init_param_obj.fit_intercept)
        max_iters = self.max_iter + start_iters
        self.n_iter_ = start_iters
        while self.n_iter_ < max_iters:
            self.callback_list.on_epoch_begin(self.n_iter_)
            LOGGER.warn("iter: " + str(self.n_iter_))
            batch_data_generator = self.batch_generator.generate_batch_data(suffix=(self.n_iter_,))
            batch_index = 0
            self.optimizer.set_iters(self.n_iter_)
            for batch_data in batch_data_generator:
                # transforms features of raw input 'batch_data_inst' into more representative features 'batch_feat_inst'
                batch_feat_inst = batch_data
                # LOGGER.debug(f"MODEL_STEP In Batch {batch_index}, batch data count: {batch_feat_inst.count()}")

                LOGGER.debug(
                    "iter: {}, batch: {}, before compute gradient, data count: {}".format(
                        self.n_iter_, batch_index, batch_feat_inst.count()))
                optim_host_gradient = self.gradient_loss_operator.compute_gradient_procedure(
                    batch_feat_inst, self.cipher_operator, self.model_weights, self.optimizer, self.n_iter_,
                    batch_index)
                # LOGGER.debug('optim_host_gradient: {}'.format(optim_host_gradient))

                self.gradient_loss_operator.compute_loss(self.model_weights, self.optimizer,
                                                         self.n_iter_, batch_index, self.cipher_operator,
                                                         batch_masked=self.batch_generator.batch_masked)

                self.model_weights = self.optimizer.update_model(self.model_weights, optim_host_gradient)
                batch_index += 1

            self.is_converged = self.converge_procedure.sync_converge_info(suffix=(self.n_iter_,))

            LOGGER.info("Get is_converged flag from arbiter:{}".format(self.is_converged))
            LOGGER.info("iter: {}, is_converged: {}".format(self.n_iter_, self.is_converged))
            LOGGER.debug(f"flowid: {self.flowid}, step_index: {self.n_iter_}")

            self.callback_list.on_epoch_end(self.n_iter_)
            self.n_iter_ += 1
            self.predict(validate_data, suffix=(self.n_iter_, ))
            prone_flag = self.auto_transfer_variables.proned_flag.get(suffix=(self.n_iter_, ))[0]
            if self.need_prone and prone_flag:
                LOGGER.warn("{}th trial is prone!".format(self.current_trial))
                break

            if self.stop_training:
                break

            if self.is_converged:
                break

        self.predict(validate_data, suffix=('epoch', self.current_trial))
        self.weight_list.append(copy.deepcopy(self.model_weights))

    def fit_binary(self, data_instances, validate_data):
        # self._abnormal_detection(data_instances)
        # self.check_abnormal_values(data_instances)
        # self.check_abnormal_values(validate_data)
        # self.validation_strategy = self.init_validation_strategy(data_instances, validate_data)
        self.callback_list.on_train_begin(data_instances, validate_data)

        LOGGER.debug(f"MODEL_STEP Start fin_binary, data count: {data_instances.count()}")

        self.header = self.get_header(data_instances)
        model_shape = self.get_features_shape(data_instances)

        if self.transfer_variable.use_async.get(idx=0):
            LOGGER.debug(f"set_use_async")
            self.gradient_loss_operator.set_use_async()
        LOGGER.info("Start initialize model.")
        # model_shape = self.get_features_shape(data_instances)
        if self.init_param_obj.fit_intercept:
            self.init_param_obj.fit_intercept = False

        if not self.component_properties.is_warm_start:
            w = self.initializer.init_model(model_shape, init_params=self.init_param_obj)
            self.model_weights = LinearModelWeights(w, fit_intercept=self.init_param_obj.fit_intercept)
        else:
            self.callback_warm_start_init_iter(self.n_iter_)

        while self.current_trial < self.trial_num:
            self.fit_n_iters(self.n_iter_, data_instances, validate_data)
            self.current_trial += 1

        self.callback_list.on_train_end()
        best_one = self.auto_transfer_variables.best_one.get()[0]
        self.model_weights = self.weight_list[best_one]
        self.set_summary(self.get_model_summary())

        # LOGGER.debug("Final lr weights: {}".format(self.model_weights.unboxed))

    def predict(self, data_instances, suffix=tuple()):
        self.transfer_variable.host_prob.disable_auto_clean()
        LOGGER.info("Start predict ...")
        self._abnormal_detection(data_instances)
        data_instances = self.align_data_header(data_instances, self.header)
        if self.need_one_vs_rest:
            self.one_vs_rest_obj.predict(data_instances)
            return

        prob_host = self.compute_wx(data_instances, self.model_weights.coef_, self.model_weights.intercept_)
        self.transfer_variable.host_prob.remote(prob_host, role=consts.GUEST, idx=0, suffix=suffix)
        LOGGER.info("Remote probability to Guest")
