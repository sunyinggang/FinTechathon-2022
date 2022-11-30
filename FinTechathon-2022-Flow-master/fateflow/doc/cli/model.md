## Model

### load

Load a model generated by `deploy` to Fate-Serving.


```bash
flow model load -c examples/model/publish_load_model.json
flow model load -j <job_id>
```

**Options**

| Parameter | Short Flag | Long Flag     | Optional | Description      |
| --------- | ---------- | ------------- | -------- | ---------------- |
| conf_path | `-c`       | `--conf-path` | Yes      | Config file path |
| job_id    | `-j`       | `--job-id`    | Yes      | Job ID           |

**Example**

```json
{
  "data": {
    "detail": {
      "guest": {
        "9999": {
          "retcode": 0,
          "retmsg": "success"
        }
      },
      "host": {
        "10000": {
          "retcode": 0,
          "retmsg": "success"
        }
      }
    },
    "guest": {
      "9999": 0
    },
    "host": {
      "10000": 0
    }
  },
  "jobId": "202111091122168817080",
  "retcode": 0,
  "retmsg": "success"
}
```

### bind

Bind a model generated by `deploy` to Fate-Serving.

```bash
flow model bind -c examples/model/bind_model_service.json
flow model bind -c examples/model/bind_model_service.json -j <job_id>
```

**Options**

| Parameter | Short Flag | Long Flag     | Optional | Description      |
| --------- | ---------- | ------------- | -------- | ---------------- |
| conf_path | `-c`       | `--conf-path` | No       | Config file path |
| job_id    | `-j`       | `--job-id`    | Yes      | Job ID           |

**Example**

```json
{
  "retcode": 0,
  "retmsg": "service id is 123"
}
```

### import

Import the model from a file or storage engine.

```bash
flow model import -c examples/model/import_model.json
flow model import -c examples/model/restore_model.json --from-database
```

**Options**

| Parameter     | Short Flag | Long Flag         | Optional | Description                          |
| ------------- | ---------- | ----------------- | -------- | ------------------------------------ |
| conf_path     | `-c`       | `--conf-path`     | No       | Config file path                     |
| from_database |            | `--from-database` | Yes      | Import the model from storage engine |

**Example**

```json
{
  "data": {
    "board_url": "http://127.0.0.1:8080/index.html#/dashboard?job_id=202111091125358161430&role=local&party_id=0",
    "code": 0,
    "dsl_path": "/root/Codes/FATE-Flow/jobs/202111091125358161430/job_dsl.json",
    "job_id": "202111091125358161430",
    "logs_directory": "/root/Codes/FATE-Flow/logs/202111091125358161430",
    "message": "success",
    "model_info": {
      "model_id": "local-0#model",
      "model_version": "202111091125358161430"
    },
    "pipeline_dsl_path": "/root/Codes/FATE-Flow/jobs/202111091125358161430/pipeline_dsl.json",
    "runtime_conf_on_party_path": "/root/Codes/FATE-Flow/jobs/202111091125358161430/local/0/job_runtime_on_party_conf.json",
    "runtime_conf_path": "/root/Codes/FATE-Flow/jobs/202111091125358161430/job_runtime_conf.json",
    "train_runtime_conf_path": "/root/Codes/FATE-Flow/jobs/202111091125358161430/train_runtime_conf.json"
  },
  "jobId": "202111091125358161430",
  "retcode": 0,
  "retmsg": "success"
}
```

### export

Export the model to a file or storage engine.

```bash
flow model export -c examples/model/export_model.json
flow model export -c examples/model/store_model.json --to-database
```

**Options**

| Parameter   | Short Flag | Long Flag       | Optional | Description                        |
| ----------- | ---------- | --------------- | -------- | ---------------------------------- |
| conf_path   | `-c`       | `--conf-path`   | No       | Config file path                   |
| to_database |            | `--to-database` | Yes      | Export the model to storage engine |

**Example**

```json
{
  "data": {
    "board_url": "http://127.0.0.1:8080/index.html#/dashboard?job_id=202111091124582110490&role=local&party_id=0",
    "code": 0,
    "dsl_path": "/root/Codes/FATE-Flow/jobs/202111091124582110490/job_dsl.json",
    "job_id": "202111091124582110490",
    "logs_directory": "/root/Codes/FATE-Flow/logs/202111091124582110490",
    "message": "success",
    "model_info": {
      "model_id": "local-0#model",
      "model_version": "202111091124582110490"
    },
    "pipeline_dsl_path": "/root/Codes/FATE-Flow/jobs/202111091124582110490/pipeline_dsl.json",
    "runtime_conf_on_party_path": "/root/Codes/FATE-Flow/jobs/202111091124582110490/local/0/job_runtime_on_party_conf.json",
    "runtime_conf_path": "/root/Codes/FATE-Flow/jobs/202111091124582110490/job_runtime_conf.json",
    "train_runtime_conf_path": "/root/Codes/FATE-Flow/jobs/202111091124582110490/train_runtime_conf.json"
  },
  "jobId": "202111091124582110490",
  "retcode": 0,
  "retmsg": "success"
}
```

### migrate

Migrate the model.

```bash
flow model migrate -c examples/model/migrate_model.json
```

**Options**

| Parameter | Short Flag | Long Flag     | Optional | Description      |
| --------- | ---------- | ------------- | -------- | ---------------- |
| conf_path | `-c`       | `--conf-path` | No       | Config file path |

**Example**

```json
{
  "data": {
    "arbiter": {
      "10000": 0
    },
    "detail": {
      "arbiter": {
        "10000": {
          "retcode": 0,
          "retmsg": "Migrating model successfully. The Config of model has been modified automatically. New model id is: arbiter-100#guest-99#host-100#model, model version is: 202111091127392613050. Model files can be found at '/root/Codes/FATE-Flow/temp/fate_flow/arbiter#100#arbiter-100#guest-99#host-100#model_202111091127392613050.zip'."
        }
      },
      "guest": {
        "9999": {
          "retcode": 0,
          "retmsg": "Migrating model successfully. The Config of model has been modified automatically. New model id is: arbiter-100#guest-99#host-100#model, model version is: 202111091127392613050. Model files can be found at '/root/Codes/FATE-Flow/temp/fate_flow/guest#99#arbiter-100#guest-99#host-100#model_202111091127392613050.zip'."
        }
      },
      "host": {
        "10000": {
          "retcode": 0,
          "retmsg": "Migrating model successfully. The Config of model has been modified automatically. New model id is: arbiter-100#guest-99#host-100#model, model version is: 202111091127392613050. Model files can be found at '/root/Codes/FATE-Flow/temp/fate_flow/host#100#arbiter-100#guest-99#host-100#model_202111091127392613050.zip'."
        }
      }
    },
    "guest": {
      "9999": 0
    },
    "host": {
      "10000": 0
    }
  },
  "jobId": "202111091127392613050",
  "retcode": 0,
  "retmsg": "success"
}
```

### tag-list

List tags of the model.

``` bash
flow model tag-list -j <job_id>
```

**Options**

| Parameter | Short Flag | Long Flag  | Optional | Description |
| --------- | ---------- | ---------- | -------- | ----------- |
| job_id    | `-j`       | `--job_id` | No       | Job ID      |

### tag-model

Add or remove a tag from the model.

```bash
flow model tag-model -j <job_id> -t <tag_name>
flow model tag-model -j <job_id> -t <tag_name> --remove
```

**Options**

| Parameter     | Short Flag | Long Flag       | Optional | Description           |
| -------- | ------ | ------------ | -------- | -------------- |
| job_id   | `-j`   | `--job_id`   | No       | Job ID        |
| tag_name | `-t`   | `--tag-name` | No       | Tag name         |
| remove   |        | `--remove`   | Yes       | Remove the tag |

### deploy

Configure predict DSL.

```bash
flow model deploy --model-id <model_id> --model-version <model_version>
```

**Options**

| Parameter      | Short Flag | Long Flag          | Optional | Description                                                  |
| -------------- | ---------- | ------------------ | -------- | ------------------------------------------------------------ |
| model_id       |            | `--model-id`       | No       | Model ID                                                     |
| model_version  |            | `--model-version`  | No       | Model version                                                |
| cpn_list       |            | `--cpn-list`       | Yes      | Components list                                              |
| cpn_path       |            | `--cpn-path`       | Yes      | Load components list from a file                             |
| dsl_path       |            | `--dsl-path`       | Yes      | Predict DSL file path                                        |
| cpn_step_index |            | `--cpn-step-index` | Yes      | Specify a checkpoint model to replace the pipeline model<br />Use `:` to separate component name and step index<br />E.g. `--cpn-step-index cpn_a:123` |
| cpn_step_name  |            | `--cpn-step-name`  | Yes      | Specify a checkpoint model to replace the pipeline model.<br />Use `:` to separate component name and step name<br />E.g. `--cpn-step-name cpn_b:foobar` |

**Example**

```json
{
  "retcode": 0,
  "retmsg": "success",
  "data": {
    "model_id": "arbiter-9999#guest-10000#host-9999#model",
    "model_version": "202111032227378766180",
    "arbiter": {
      "party_id": 9999
    },
    "guest": {
      "party_id": 10000
    },
    "host": {
      "party_id": 9999
    },
    "detail": {
      "arbiter": {
        "party_id": {
          "retcode": 0,
          "retmsg": "deploy model of role arbiter 9999 success"
        }
      },
      "guest": {
        "party_id": {
          "retcode": 0,
          "retmsg": "deploy model of role guest 10000 success"
        }
      },
      "host": {
        "party_id": {
          "retcode": 0,
          "retmsg": "deploy model of role host 9999 success"
        }
      }
    }
  }
}
```

### get-predict-dsl

Get predict DSL of the model.

```bash
flow model get-predict-dsl --model-id <model_id> --model-version <model_version> -o ./examples/
```

**Options**

| Parameter     | Short Flag | Long Flag         | Optional | Description   |
| ------------- | ---------- | ----------------- | -------- | ------------- |
| model_id      |            | `--model-id`      | No       | Model ID      |
| model_version |            | `--model-version` | No       | Model version |
| output_path   | `-o`       | `--output-path`   | No       | Output path   |

### get-predict-conf

Get the template of predict config.

```bash
flow model get-predict-conf --model-id <model_id> --model-version <model_version> -o ./examples/
```

**Options**

| Parameter     | Short Flag | Long Flag         | Optional | Description   |
| ------------- | ---------- | ----------------- | -------- | ------------- |
| model_id      |            | `--model-id`      | No       | Model ID      |
| model_version |            | `--model-version` | No       | Model version |
| output_path   | `-o`       | `--output-path`   | No       | Output path   |

### get-model-info

Get model information.

```bash
flow model get-model-info --model-id <model_id> --model-version <model_version>
flow model get-model-info --model-id <model_id> --model-version <model_version> --detail
```

**Options**

| Parameter     | Short Flag | Long Flag         | Optional | Description                  |
| ------------- | ---------- | ----------------- | -------- | ---------------------------- |
| model_id      |            | `--model-id`      | No       | Model ID                     |
| model_version |            | `--model-version` | No       | Model version                |
| role          | `-r`       | `--role`          | Yes      | Party role                   |
| party_id      | `-p`       | `--party-id`      | Yes      | Party ID                     |
| detail        |            | `--detail`        | Yes      | Display detailed information |

### homo-convert

Convert trained homogenous model to the format of another ML framework.

```bash
flow model homo-convert -c examples/model/homo_convert_model.json
```

**Options**

| Parameter | Short Flag | Long Flag     | Optional | Description      |
| --------- | ---------- | ------------- | -------- | ---------------- |
| conf_path | `-c`       | `--conf-path` | No       | Config file path |

### homo-deploy

Deploy trained homogenous model to a target online serving system. Currently the supported target serving system is KFServing.

```bash
flow model homo-deploy -c examples/model/homo_deploy_model.json
```

**Options**

| Parameter | Short Flag | Long Flag     | Optional | Description      |
| --------- | ---------- | ------------- | -------- | ---------------- |
| conf_path | `-c`       | `--conf-path` | No       | Config file path |