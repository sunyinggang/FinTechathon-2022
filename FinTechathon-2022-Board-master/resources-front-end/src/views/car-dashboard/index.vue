<template>
  <div class="app-container flex flex-col" style="height: 100%">
    <div class="my-container">
      <!-- <div class="pos-none1">占位</div> -->
      <div class="content">
        <div class="left">
          <div
            class="left-item"
            @click="
              () => {
                tab = 0;
              }
            "
          >
            <el-progress
              :percentage="per1"
              width="80"
              type="circle"
              class="left-progress"
            />
            <div class="left-icon">
              <svg viewBox="0 0 1024 1024">
                <path
                  d="M500 128.8c-95.2 5.6-173.6 83.2-180 178.4-7.2 112 80.8 205.6 191.2 205.6 106.4 0 192-86.4 192-192 0.8-110.4-92-198.4-203.2-192zM512 575.2c-128 0-383.2 64-383.2 192v96c0 17.6 14.4 32 32 32h702.4c17.6 0 32-14.4 32-32V766.4c0-127.2-255.2-191.2-383.2-191.2z"
                />
              </svg>
            </div>
            <div class="left-text">个人状况</div>
            <i class="el-icon-d-arrow-right left-arrow" />
          </div>
          <div
            class="left-item"
            @click="
              () => {
                tab = 1;
              }
            "
          >
            <el-progress
              :percentage="per2"
              width="80"
              type="circle"
              class="left-progress"
            />
            <div class="left-icon">
              <svg viewBox="0 0 1026 1024">
                <path
                  d="M1025.024 780.288l-128 0 0 59.392q0 26.624-18.432 45.056t-45.056 18.432l-64.512 0q-26.624 0-45.056-18.432t-18.432-45.056l0-59.392-384 0 0 59.392q0 26.624-18.944 45.056t-45.568 18.432l-64.512 0q-26.624 0-45.056-18.432t-18.432-45.056l0-59.392-129.024 0 0-201.728q0-57.344 36.352-89.088t91.648-35.84q4.096-17.408 12.8-47.104t18.432-64 20.48-68.608 19.968-60.928q27.648-77.824 115.712-77.824l397.312 0q39.936 0 65.536 22.016t35.84 51.712l21.504 63.488q11.264 34.816 23.04 69.632t22.016 65.024 16.384 46.592q55.296 5.12 91.648 36.864t36.352 88.064l0 201.728zM125.952 648.192q26.624 0 45.568-18.432t18.944-45.056-18.944-45.568-45.568-18.944-45.056 18.944-18.432 45.568 18.432 45.056 45.056 18.432zM793.6 454.656l-37.888-187.392-487.424 0-33.792 187.392 559.104 0zM896 648.192q26.624 0 46.08-19.456t19.456-46.08q0-27.648-19.456-46.592t-46.08-18.944q-27.648 0-46.592 18.944t-18.944 46.592q0 26.624 18.944 46.08t46.592 19.456z"
                />
              </svg>
            </div>
            <div class="left-text">车辆状况</div>
            <i class="el-icon-d-arrow-right left-arrow" />
          </div>
          <div
            class="left-item"
            @click="
              () => {
                tab = 2;
              }
            "
          >
            <el-progress
              :percentage="per3"
              width="80"
              type="circle"
              class="left-progress"
            />
            <div class="left-icon">
              <svg viewBox="0 0 1024 1024">
                <path
                  d="M512 621.696l-150.848-150.826667 30.165333-30.186666L512 561.365333l120.682667-120.682666 30.165333 30.165333L512 621.696z m150.848-150.826667l-30.165333-30.186666a170.666667 170.666667 0 1 0-241.365334 0L361.173333 470.826667c-83.306667-83.306667-83.306667-218.389333 0-301.696 83.306667-83.306667 218.389333-83.306667 301.696 0 83.306667 83.306667 83.306667 218.389333 0 301.696zM512 362.666667a42.666667 42.666667 0 1 1 0-85.333334 42.666667 42.666667 0 0 1 0 85.333334z m-134.186667 365.290666a21.333333 21.333333 0 1 1 30.144-30.165333l110.634667 110.613333L857.664 469.333333H768v-42.666666h106.538667A63.936 63.936 0 0 1 938.666667 490.474667V874.88A64 64 0 0 1 874.602667 938.666667H149.397333A63.914667 63.914667 0 0 1 85.333333 874.858667V490.453333A63.808 63.808 0 0 1 149.461333 426.666667H256v42.666666H149.461333A21.141333 21.141333 0 0 0 128 490.474667v302.208l200.042667-200.042667a21.205333 21.205333 0 0 1 30.058666 0.128c8.32 8.32 8.192 21.973333 0.106667 30.037333L130.474667 850.56a21.333333 21.333333 0 0 1-2.474667 2.133333v22.186667c0 11.669333 9.536 21.141333 21.397333 21.141333h396.437334l-168.042667-168.042666zM874.581333 896A21.333333 21.333333 0 0 0 896 874.858667V491.050667a21.973333 21.973333 0 0 1-1.984 2.261333L548.757333 838.592l54.186667 54.186667c1.002667 1.002667 1.898667 2.090667 2.666667 3.221333h269.013333z"
                />
              </svg>
            </div>
            <div class="left-text">道路状况</div>
            <i class="el-icon-d-arrow-right left-arrow" />
          </div>
        </div>
        <el-card class="box-card">
          <div slot="header" class="clearfix">
            <span>建议</span>
          </div>
          <div class="card-text">
            <div v-if="tab == 0">
              <div class="textBox">
                <ul class="textItem">
                  {{
                    personInfo
                  }}
                </ul>
              </div>
            </div>
            <div v-if="tab == 1">
              <div class="borderBlock">
                <ul>
                  <!-- 检测到方向盘握力异常： -->
                  <ul
                    :style="{
                      '--cardTextColor1': cardTextColor1,
                      color: cardTextColor1,
                    }"
                  >
                    {{
                      carInfo
                    }}
                  </ul>
                </ul>
              </div>
              <div class="card1">
                <svg
                  class="svg1"
                  t="1669627964869"
                  viewBox="0 0 1024 1024"
                  version="1.1"
                  xmlns="http://www.w3.org/2000/svg"
                  p-id="1350"
                >
                  <path
                    d="M1001.661867 796.544c48.896 84.906667 7.68 157.013333-87.552 157.013333H110.781867c-97.834667 0-139.050667-69.504-90.112-157.013333l401.664-666.88c48.896-87.552 128.725333-87.552 177.664 0l401.664 666.88zM479.165867 296.533333v341.333334a32 32 0 1 0 64 0v-341.333334a32 32 0 1 0-64 0z m0 469.333334v42.666666a32 32 0 1 0 64 0v-42.666666a32 32 0 1 0-64 0z"
                    fill="#FAAD14"
                    p-id="1351"
                  />
                </svg>
              </div>
            </div>
            <div v-if="tab == 2">
              <ul>
                小雨，路面略微湿滑, 前方路段风险系数：<span
                  :style="{
                    '--cardTextColor2': cardTextColor2,
                    color: cardTextColor2,
                  }"
                >{{ roadScore }}</span
                >
              </ul>
              <ul>
                <div class="container">
                  <div
                    :style="{ '--percentNumber': percentNumber, '--cardTextColor2': cardTextColor2 }"
                    class="card"
                  >
                    <div class="box">
                      <div class="percent">
                        <svg class="svg2">
                          <circle cx="90" cy="90" r="90" />
                          <circle cx="90" cy="90" r="90" />
                        </svg>
                        <div class="number">
                          <h2 :style="{ '--cardTextColor2': cardTextColor2 }">
                            {{ percentNumber }}<span>%</span>
                          </h2>
                        </div>
                      </div>
                    </div>
                  </div>
                </div>
              </ul>
            </div>
          </div>
        </el-card>
      </div>
      <!-- <div class="pos-none2">占位</div> -->
    </div>
  </div>
</template>

<script>
export default {
  components: {},
  data: function() {
    return {
      flag: 0,
      tab: 1,
      per1: 50,
      per2: 30,
      per3: 20,
      percentNumber: 76,
      cardTextColor1: 'yellow',
      cardTextColor2: 'yellow',
      personInfo: '驾驶员心率异常，请注意休息',
      carInfo: '轮胎有磨损',
      roadInfo: '小雨，路面略微湿滑',
      roadScore: '中'
    }
  },
  computed: {},
  mounted() {
    switch (this.$route.query.tabIndex) {
      case 1:
        this.personInfo = '驾驶员心率异常，请注意休息'
        this.carInfo = '轮胎有磨损'
        this.roadInfo = '小雨，路面略微湿滑'
        this.roadScore = '中'
        this.percentNumber = 32
        this.cardTextColor2 = 'green'
        this.per1 = 50
        this.per2 = 30
        this.per3 = 20
        break
      case 2:
        this.personInfo = '司机状态良好'
        this.carInfo = '制动系统异常'
        this.roadInfo = '路面能见度低，事故多发'
        this.roadScore = '中'
        this.percentNumber = 56
        this.cardTextColor2 = 'yellow'
        this.per1 = 5
        this.per2 = 45
        this.per3 = 50
        break
      case 3:
        this.personInfo = '睡眠不足，注意休息'
        this.carInfo = '车辆自检良好'
        this.roadInfo = '路面坡度大，路况复杂，事故多发，小心行驶'
        this.roadScore = '高'
        this.percentNumber = 86
        this.cardTextColor2 = 'red'
        this.per1 = 15
        this.per2 = 15
        this.per3 = 70
        break
      default:
        break
    }
  },
  methods: {}
}
</script>

<style lang="scss" scoped>
.app-container {
  width: 82%;
  position: absolute;
  background-image: url(/static/carBack.png);
  background-size: 165vh;
  background-repeat: no-repeat;
  background-position: center;
}
// .my-container {
//   height: 100%;
//   display: grid;
//   grid-template-rows: 6fr 20fr 10fr;
//   justify-content: center;
//   align-content: center;
//   justify-items: center;
//   align-items: center;
// }

// .pos-none1 {
//   grid-row: 1/1;
//   opacity: 0;
//   height: 100%;
//   width: 100%;
//   justify-content: stretch;
//   align-content: stretch;
// }
// .pos-none2 {
//   grid-row: 3/3;
//   opacity: 0;
//   height: 100%;
//   width: 100%;
//   justify-content: stretch;
//   align-content: stretch;
// }
// .content {
//   height: 100%;
//   width: 100%;
//   grid-row: 2/2;
//   justify-content: stretch;
//   align-content: stretch;
//   display: grid;
//   grid-template-columns: 45fr 55fr;
//   grid-gap: 5px;
//   padding: 5px;
//   box-sizing: border-box;
//   overflow: hidden;
//   grid-gap: 10px;
//   box-shadow: 0 20px 50px rgb(23, 32, 90);
//   /* border: 2px solid #409eee; */
//   padding: 20px 5px 20px 5px;
//   border-radius: 2%;
// }
.content {
  position: absolute;
  height: 47vh;
  width: 43vw;
  left: 31vw;
  top: 16.5vh;
  grid-row: 2/2;
  justify-content: stretch;
  align-content: stretch;
  display: grid;
  grid-template-columns: 45fr 55fr;
  grid-gap: 5px;
  padding: 5px;
  box-sizing: border-box;
  overflow: hidden;
  grid-gap: 10px;
  box-shadow: 0 20px 50px rgb(23, 32, 90);
  /* border: 2px solid #409eee; */
  padding: 20px 5px 20px 5px;
  border-radius: 2%;
}
.left {
  height: 100%;
  width: 100%;
  justify-content: center;
  align-content: center;
  display: grid;
  grid-template-rows: 1fr 1fr 1fr;
  grid-gap: 55px;
  background-color: #181b40;
}
.right {
  height: 100%;
  width: 100%;
  display: grid;
  justify-content: center;
  align-content: center;
  grid-template-rows: 1fr 10fr 45fr;
  /* box-shadow: 0 20px 10px rgb(23, 32, 90); */
  border: 2px solid #409eee;
}
.left-item {
  height: 100%;
  width: 100%;
  display: grid;
  justify-content: center;
  align-content: center;
  grid-template-columns: 4fr 5fr 9fr 5fr;
  padding: 2px;
  // box-shadow: 5px 5px 1px 1px rgb(23, 32, 90);
  /* border: 2px solid #409eee; */
  border-radius: 3%;
  justify-items: center;
}

.left-item:active {
  transform: scale(0.98);
  box-shadow: 3px 2px 22px 1px rgba(0, 0, 0, 0.24);
}
.left-progress {
  height: 100%;
  width: 100%;
  grid-column: 1/1;
}
.left-icon {
  height: 85%;
  width: 85%;
  grid-column: 2/2;
  fill: #00e6ac;
  display: flex;
  align-items: center;
  justify-content: center;
}
.left-text {
  height: 100%;
  grid-column: 3/3;
  font-size: 2rem;
  color: #409eff;
  display: flex;
  align-items: center;
  justify-items: center;
}
.left-arrow {
  height: 100%;
  width: 100%;
  grid-column: 4/4;
  font-size: 5rem;
  color: #409eff;
  display: flex;
  align-items: center;
  justify-items: center;
}
.right-top {
  height: 100%;
  width: 100%;
  grid-row: 2/2;
  font-size: 4rem;
  color: #409eff;
  display: flex;
  align-items: center;
  justify-items: center;
  text-align: center;
}
.right-content {
  height: 100%;
  width: 100%;
  grid-row: 3/3;
  font-size: 2rem;
  color: #409eff;
  display: flex;
  align-items: center;
  justify-items: center;
}
.clearfix {
  text-align: center;
  font-size: 2rem;
}
.card-text {
  font-size: 1.5rem;
}

.box-card {
  background-color: #181b40;
  border-radius: 8%;
}

/** 建议列表 */
.textBox {
  text-align: left;
  height: 100%;
  justify-items: center;
  justify-content: center;
}
.textItem {
  margin-bottom: 1.5rem;
  padding-left: 2.5rem;
  position: relative;
  font-size: 2rem;
  &:before {
    content: "";
    position: absolute;
    left: 0.6rem;
    top: 0.8rem;
    border: 1px solid yellow;
    background-color: yellow;
    display: inline-block; // 此句为css样式展示重点
    width: 1.5rem;
    height: 1.5rem;
    border-radius: 50%;
  }
}

/** 环状进度卡片 */
.container {
  position: relative;
  margin-top: 40px;
  display: flex;
  justify-content: space-around;

  .card {
    position: relative;
    display: flex;
    justify-content: center;
    align-items: center;
    text-align: center;
    transition: 0.5s;

    // &:hover {
    //   box-shadow: 0 15px 35px rgba(0, 0, 0, 0.5);
    // }
  }
}

.percent {
  position: relative;
  border-radius: 50%;
  // box-shadow: inset 0 0 50px #000;
  // background: #222;

  .number {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    display: flex;
    justify-content: center;
    align-items: center;
    border-radius: 50%;

    h2 {
      color: var(--cardTextColor2);
      font-weight: 700;
      font-size: 70px;
      transition: 0.5s;
    }
  }
}

.card:hover .percent .number h2 {
  color: var(--cardTextColor2);
  font-size: 90px;
}

.percent .number h2 span {
  font-size: 35px;
  color: var(--cardTextColor2);
}

.card:hover .percent .number h2 span {
  color: var(--cardTextColor2);
  transition: 0.5s;
}

// .text {
//   position: relative;
//   color: var(--cardTextColor2);
//   margin-top: 20px;
//   font-weight: 700;
//   font-size: 18px;
//   letter-spacing: 1px;
//   text-transform: uppercase;
//   transition: 0.5s;
// }

// .card:hover .text {
//   color: #fff;
// }

.svg2 {
  position: relative;
  width: 200px;
  height: 200px;
  transform: rotate(-90deg);

  circle {
    width: 100%;
    height: 100%;
    fill: none;
    stroke: #191919;
    stroke-width: 10;
    stroke-linecap: round;
    transform: translate(5px, 5px);

    &:nth-child(2) {
      stroke-dasharray: 565.47;
      stroke-dashoffset: 565.47;
    }
  }
}

.card {
  &:nth-child(1) svg circle:nth-child(2) {
    stroke-dashoffset: calc(565.47 - (565.47 * var(--percentNumber)) / 100);
    // stroke: #00ff43;
    stroke: var(--cardTextColor2);
    //stroke: #00a1ff;
    //stroke: #ff04f7;
  }
}

/** 卡片 */
.borderBlock {
  box-sizing: border-box;
  text-align: center;
  border: 5px solid #dedede;
  padding: 15px 25px;
  height: inherit;
  border-radius: 30px;
}
/** 感叹号 */
.card1 {
  position: relative;
}
.svg1 {
  width: 20vw;
  height: 20vh;
  position: absolute;
  left: 1vw;
  top: 1vh;
}
</style>

