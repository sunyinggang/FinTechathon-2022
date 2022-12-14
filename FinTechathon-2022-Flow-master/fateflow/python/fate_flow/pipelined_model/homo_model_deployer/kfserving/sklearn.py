#
#  Copyright 2021 The FATE Authors. All Rights Reserved.
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


import os
import tempfile
from abc import ABC

import joblib
import kfserving

from .base import KFServingDeployer


class SKLearnKFDeployer(KFServingDeployer, ABC):
    def _do_prepare_model(self):
        working_dir = tempfile.mkdtemp()
        local_file = os.path.join(working_dir, "model.joblib")
        joblib.dump(self.model_object, local_file)
        return local_file


class SKLearnV1KFDeployer(SKLearnKFDeployer):
    def _do_prepare_predictor(self):
        # Use our own sklearnserver image that has scikit-learn==0.24.2 because KFServing's default one
        # uses scikit-learn==0.20.3 that cannot de-serialize models of higher versions.
        self.isvc.spec.predictor.sklearn = kfserving.V1beta1SKLearnSpec(
            image="federatedai/sklearnserver:v0.6.1-0.24.2",
            protocol_version='v1',
            storage_uri=self.storage_uri)


class SKLearnV2KFDeployer(SKLearnKFDeployer):
    def _do_prepare_predictor(self):
        self.isvc.spec.predictor.sklearn = kfserving.V1beta1SKLearnSpec(
            protocol_version='v2',
            storage_uri=self.storage_uri)
