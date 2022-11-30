<template>
  <dv-border-box-10>
    <div class="container">
      <img class="svgImg" src="./img/page_1/1.png" >
      <embed ref="iframe" class="iframe" width="100%" scrolling="auto" src="https://insightlane.org/showcase/index.html?city=boston_bike" @load="loadFrame">
    </div>
  </dv-border-box-10>
</template>

<script>
import Card1 from './card1.vue'

export default {
  components: {
    Card1
  },
  data: function() {
    return {
      iframeWin: {},
      iframeLoading: true
    }
  },
  computed: {},
  mounted() {
    this.iframeWin = this.$refs.iframe
  },
  destroyed() {},
  methods: {
    loadFrame() {
      console.log('load')
      var css = document.createElement('link')
      css.href = 'style.css'
      css.rel = '.title.overlay{display:none}'
      css.type = 'text/css'
      console.log(this.iframeWin)
      //   this.iframeWin.document.appendChild(css)
      // 获取iframe html文件head
      //   const element = doc.getElementsByClassName('title overlay')
      //   console.log(element)
    }
  }
}
</script>

<style lang="scss" scoped>
.container {
  position: absolute;
  top: 0.5%;
  left: 0.5%;
  width: 99%;
  height: 99%;
  background-color: #111416;
  overflow: hidden;
}

.iframe {
  position: absolute;
  top: 6.5vh;
  left: 1vw;
  width: 50vw;
  height: 94vh;
}

.iframe >>> .title {
  display: none;
}

.svgImg {
  position: absolute;
  top: -3vh;
  left: -5.5vw;
  width: 105vw;
  height: 105vh;
}
</style>
