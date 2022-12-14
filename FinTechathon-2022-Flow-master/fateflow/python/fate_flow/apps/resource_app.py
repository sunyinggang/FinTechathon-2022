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
from flask import request

from fate_flow.manager.resource_manager import ResourceManager
from fate_flow.utils.api_utils import get_json_result
from fate_flow.utils.detect_utils import validate_request


@manager.route('/query', methods=['post'])
def query_resource():
    use_resource_job, computing_engine_resource = ResourceManager.query_resource(**request.json)
    return get_json_result(retcode=0, retmsg='success', data={"use_resource_job": use_resource_job,
                                                              "computing_engine_resource": computing_engine_resource})


@manager.route('/return', methods=['post'])
@validate_request('job_id')
def return_resource():
    status = ResourceManager.return_resource(job_id=request.json.get("job_id"))
    return get_json_result(data=status)


