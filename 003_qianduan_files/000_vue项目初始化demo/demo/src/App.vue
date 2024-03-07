<template>

    <!-- 当值为true，这个页面会展示这个"通用内容" -->
    <div  v-if="$route.meta.show">  
       通用内容
    </div>
    <router-view></router-view>
</template>

<script>

export default {
  name: 'App',
  components: {
   
  }
}
</script>

<style>

</style>
