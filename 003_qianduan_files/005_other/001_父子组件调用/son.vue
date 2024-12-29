<template>
  <button @click="userFather">调用父组件</button>
</template>
<script>
export default {

  data() {

    return {
      msg: "我是子组件中的数据"
    }
  },
  methods: {

    Soninfo(){
      console.log('我被父组件调用了。。。')
    },


    userFather(){

      // 2.1 使用 this.$parent 就可以调用父组件的内容
      this.$parent.fatherinfo()
    }
  }
}
</script>