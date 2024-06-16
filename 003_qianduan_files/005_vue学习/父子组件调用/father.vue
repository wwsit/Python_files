<template>

  <!-- 1.1 需要用到ref属性，给这个组件起个标识，叫child -->
  <ChildA ref="child"></ChildA>

  <button @click="useChildMethod">调用子组件</button>

</template>

<script>
import ChildA from "./son.vue"

export default {
  components: {
    ChildA
  },
  methods: {


    useChildMethod() {

      // 1.2 通过 this.$refs 去访问 child组件里面的内容
      this.$refs.child.Soninfo()
    },

    fatherinfo(){
      console.log("我是父组件。。。")
    }

  }
}
</script>
