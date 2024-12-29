<template>
    <div class="div1">
      <button class="button1">左上</button>
      <button class="button2">右上</button>
      <button class="button3">左下</button>
      <button class="button4">右下</button>
  
      <button class="button5">中间</button>
  
    </div>
    <div>
      <button class="button6">float属性设置位置</button>
  
    </div>
  </template>
  
  <script>
  
  export default {
    components: {
    },
    data() {
      return {
  
      };
    },
  
    methods: {
  
    }
  }
  
  
  </script>
  
  
  <style>
  
  
  .button1 {
  
    /* 需要用到 position: fixed 固定位置，然后在设置要固定在那个地方 */
    position: fixed;
    left: 0px;
    top: 0px;
  
  }
  
  
  .button2 {
    position: fixed;
    right: 0px;
    top: 0px;
  }
  
  
  .button3 {
    position: fixed;
    bottom: 0px;
    left: 0px;
  }
  
  
  .button4 {
    position: fixed;
    bottom: 0px;
    right: 0px
  }
  
  
  .button5 {
    position: fixed;
    left: calc(50vw - 2vw);
    top: calc(50vh - 5vh);
  }
  
  
  .button6{
    float:right;
    margin-right: 20%;
  }
  </style>