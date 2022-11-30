<template>
  <div class="app-container flex flex-col bg-dark">
    <form-wizard
      class="mywizard"
      title=""
      subtitle=""
      shape="circle"
      color="#20a0ff"
      error-color="#ff4949"
      next-button-text="下一步"
      step-size="xs"
      transition="fffff"
      style="width: 100%"
      @on-complete="onComplete"
    >
      <wizard-step
        slot-scope="props"
        slot="step"
        :tab="props.tab"
        :transition="props.transition"
        :index="props.index"
      >
        d
      </wizard-step>
      <tab-content title="获取特征权重">
        <el-row>
          <h2>联合建模后各特征权重值：</h2>
        </el-row>
        <el-row>
          <el-table
            :data="tableData"
            :row-class-name="tableRowClassName"
            style="width: 100%"
            stripe
            border
          >
            <el-table-column prop="name" label="特征名" />
            <el-table-column prop="value" label="权重值" />
          </el-table>
        </el-row>
      </tab-content>
      <tab-content title="输入预测分数">
        <el-row>
          <!-- <el-col :span="3" :offset="4">
            <h2>道路方信息</h2>
          </el-col> -->
          <el-col :span="3" :offset="11">
            <h2>司机方信息</h2>
          </el-col>
        </el-row>
        <el-row>
          <!-- <el-col :span="10">
            <el-table
              :data="inputTableData21"
              :row-class-name="tableRowClassName"
              style="width: 100%"
              stripe
              border
            >
              <el-table-column prop="name" label="特征名" />
              <el-table-column prop="value" label="特征值">
                <template slot-scope="scope">
                  <el-input
                    v-model="scope.row.value"
                    type="text"
                    size="small"
                  />
                </template>
              </el-table-column>
            </el-table>
          </el-col> -->
          <!-- <el-col :span="10" :offset="4"> -->
          <el-col :span="10" :offset="7">
            <el-table
              :data="inputTableData22"
              :row-class-name="tableRowClassName"
              style="width: 100%"
              stripe
              border
            >
              <el-table-column prop="name" label="特征名" />
              <el-table-column prop="value" label="特征值">
                <template slot-scope="scope">
                  <el-input
                    v-model="scope.row.value"
                    type="text"
                    size="small"
                  />
                </template>
              </el-table-column>
            </el-table>
          </el-col>
        </el-row>
        <el-row>
          <!-- <el-col :span="1" :offset="4">
            <el-button type="primary">获取道路方信息</el-button>
          </el-col> -->
          <!-- <el-col :span="1" :offset="13"> -->
          <el-col :span="3" :offset="10">
            <el-button style="width: 230px" type="primary" @click="getDriverData">获取司机方信息</el-button>
          </el-col>
        </el-row>
        <el-row>
          <el-col :span="3" :offset="10">
            <el-button style="width: 230px" type="primary" @click="sendPredict">开始预测</el-button>
          </el-col>
        </el-row>
        <el-row>
          <el-col :span="6" :offset="9">
            <el-input :value="score" disabled />
          </el-col>
        </el-row>
      </tab-content>
      <tab-content title="输入可行性评估值">
        <el-row>
          <h2>建议的可行性估值：</h2>
        </el-row>
        <el-row>
          <el-table
            :data="inputTableData3"
            :row-class-name="tableRowClassName"
            style="width: 100%"
            stripe
            border
          >
            <el-table-column label="特征名">
              <template slot-scope="scope">
                {{ scope.row.name }}
              </template>
            </el-table-column>
            <el-table-column label="特征值">
              <template slot-scope="scope">
                <el-input
                  v-model="scope.row.value"
                  type="text"
                  size="small"/>
              </template>
            </el-table-column>
          </el-table>
        </el-row>
        <el-row>
          <el-col :span="6" :offset="10">
            <el-button
              type="primary"
              @click="readValue"
            >读入可行性评估值</el-button
            >
          </el-col>
        </el-row>
      </tab-content>
      <el-button slot="prev" type="primary">后退</el-button>
      <el-button slot="next" type="primary">下一步</el-button>
      <el-button slot="finish" type="primary">开始分析</el-button>
    </form-wizard>
  </div>
</template>

<script>
import { FormWizard, TabContent } from 'vue-form-wizard'
import 'vue-form-wizard/dist/vue-form-wizard.min.css'
import request from '@/utils/request'
// import axios from 'axios'

export default {
  components: {
    FormWizard,
    TabContent
  },
  data: function() {
    return {
      score: '',
      tabIndex: 1,
      allData: {
        first: [
          {
            'name': 'steering_wheel_pressure',
            'value': 0.888215284
          },
          {
            'name': 'sex',
            'value': 0.2153267

          },
          {
            'name': 'heart_rate',
            'value': 0.233105
          },
          {
            'name': 'drive_time',
            'value': 0.55163158
          },
          {
            'name': 'car_condition',
            'value': 0.392874664

          },
          { 'name': 'light',
            'value': 0.220911775

          },
          { 'name': 'phone',
            'value': 0.853473957

          },
          {
            'name': 'bias',
            'value': 0.014002856

          },
          {
            'name': 'bump',
            'value': 0.009391197

          },
          {
            'name': 'driver_age',
            'value': 0.656148902
          },
          {
            'name': 'road_blas',
            'value': 0.803548282
          },
          {
            'name': 'age',
            'value': 0.42153134

          },
          {
            'name': 'self_estimate',
            'value': 0.705836705
          },
          {
            'name': 'pedal_pressure',
            'value': 0.084746292
          }
        ],
        second: [
          {
            'name': 'steering_wheel_pressure',
            'value': 0.543754453

          },
          {
            'name': 'sex',
            'value': 0.5648629

          },
          {
            'name': 'heart_rate',
            'value': 0.524331
          },
          {
            'name': 'drive_time',
            'value': 0.726285648

          },
          {
            'name': 'car_condition',
            'value': 0.068058351

          },
          { 'name': 'light',
            'value': 0.349532115

          },
          { 'name': 'phone',
            'value': 0.549291418

          },
          {
            'name': 'bias',
            'value': 0.400464497

          },
          {
            'name': 'bump',
            'value': 0.055252891

          },
          {
            'name': 'driver_age',
            'value': 0.668579765

          },
          {
            'name': 'road_blas',
            'value': 0.677603823

          },
          {
            'name': 'age',
            'value': 0.42153134

          },
          {
            'name': 'self_estimate',
            'value': 0.960650006

          },
          {
            'name': 'pedal_pressure',
            'value': 0.4215613
          }
        ],
        third: [
          {
            'name': 'steering_wheel_pressure',
            'value': 0.687279353

          },
          {
            'name': 'sex',
            'value': 0.4859357

          },
          {
            'name': 'heart_rate',
            'value': 0.3345

          },
          {
            'name': 'drive_time',
            'value': 0.846190928
          },
          {
            'name': 'car_condition',
            'value': 0.049121928
          },
          { 'name': 'light',
            'value': 0.502738225
          },
          { 'name': 'phone',
            'value': 0.074179637
          },
          {
            'name': 'bias',
            'value': 0.052412655
          },
          {
            'name': 'bump',
            'value': 0.491464064
          },
          {
            'name': 'driver_age',
            'value': 0.294710115
          },
          {
            'name': 'road_blas',
            'value': 0.510727916
          },
          {
            'name': 'age',
            'value': 0.42153134

          },
          {
            'name': 'self_estimate',
            'value': 0.611981273
          },
          {
            'name': 'pedal_pressure',
            'value': 0.614371785
          }
        ]
      },
      tableData: [
        {
          name: '',
          value: undefined
        }
      ],
      inputTableData22: [
        {
          name: '',
          value: undefined
        }
      ],
      inputTableData21: [
        {
          name: 'average_speed',
          value: undefined
        }, {
          name: 'average_flow',
          value: undefined
        }, {
          name: 'road_type',
          value: undefined
        }, {
          name: 'road_width',
          value: undefined
        }, {
          name: 'road_facility',
          value: undefined
        }, {
          name: 'cross',
          value: undefined
        }, {
          name: 'recent_accident',
          value: undefined
        }, {
          name: 'weather',
          value: undefined
        }
      ],
      inputTableData3: [
        {
          name: '',
          value: undefined
        }
      ],
      options: {
        types: [
          {
            description: '上传数据',
            accept: {
              'text/plain': ['.csv', '.json']
              // 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet': ['.xlsx'],
              // 'application/vnd.ms-excel': ['.xls'],
              // 'image/*': ['.png', '.gif', '.jpeg', '.jpg', '.webp']
            }
          }
        ],
        multiple: false, // 是否允许上传多个文件,
        excludeAcceptAllOption: true // 是否排除允许全部类型选项
      }
    }
  },
  computed: {},
  created: function() {
    this.getFeature()
  },
  methods: {
    onComplete: function() {
      this.$router.push({
        name: 'CARDASH',
        query: {
          tabIndex: this.tabIndex
        }
      })
    },
    validateFirstStep() {
      return new Promise((resolve, reject) => {
        this.$refs.ruleForm.validate((valid) => {
          resolve(valid)
        })
      })
    },
    tableRowClassName({ row, rowIndex }) {
      if (rowIndex === 1) {
        return 'warning-row'
      } else if (rowIndex === 3) {
        return 'success-row'
      }
      return ''
    },
    getFeature() {
      request
        .post('/v1/tracking/component/output/model', {
          component_name: 'auto_lr_0',
          job_id: this.$route.query.jobId,
          party_id: '9999',
          role: 'guest'
        })
        .then((response) => {
          const getData = response.data.data.weight
          const getName = Object.getOwnPropertyNames(getData)
          this.tableData = getName.map((item) => {
            const name = item
            const value = getData[item]
            return { name, value }
          })
          // this.inputTableData21 = getName.map((item) => {
          //   const name = item
          //   return { name }
          // })
          this.inputTableData22 = getName.map((item) => {
            const name = item
            return { name }
          })
          this.inputTableData3 = this.inputTableData22
        })
        .catch((error) => {
          console.log('error', error)
        })
    },
    sendPredict() {
      this.score = ((Math.random() * (0.9 - 0.65)) + 0.65).toFixed(3)
      // axios.post('http://82.157.40.112:8350/api/admin/login', {
      //   password: 'admin',
      //   username: 'admin'
      // }, {
      //   headers: {
      //     Host: '82.157.40.112:8350',
      //     Origin: 'http://82.157.40.112:8350'
      //   }}
      // )
      //   .then(response => {
      //     console.log(response)
      //   }
      //   )
    },
    async readValue() {
      let fileHandleList
      try {
        fileHandleList = await window.showOpenFilePicker(this.options)
      } catch (error) {
        window.$message.error(
          '该浏览器不支持showOpenFilePicker方法，请切换浏览器'
        )
      }
      const fileData = await fileHandleList[0].getFile()
      if (fileData.type === 'application/json') {
        // 读文件数据
        const getText = await fileData.text()
        const reader = JSON.parse(getText)
        for (const k in reader) {
          // this.inputTableData3[k] = reader[k]
          this.$set(this.inputTableData3[k], 'value', reader[k].value)
          console.log(reader[k])
          console.log(this.inputTableData3)
        }
      }
    },
    getDriverData() {
      const flag = Math.floor(Math.random() * (4 - 1)) + 1
      this.tabIndex = flag
      switch (flag) {
        case 1:
          this.inputTableData22 = this.allData.first
          break
        case 2:
          this.inputTableData22 = this.allData.second
          break
        case 3:
          this.inputTableData22 = this.allData.third
          break
        default:
          break
      }
    }
  }
}
</script>

<style lang="css" scoped>
.mywizard >>> .wizard-icon-container {
  width: 100%;
  height: 100%;
  border-radius: 50%;
}

.el-row {
  margin-bottom: 10px;
}
</style>
