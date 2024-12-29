<template>
  <div>
    <button @click="setCookie()">设置cookie</button>
    <button @click="getCookie()">获取cookie</button>
    <button @click="addCookie()">cookie值+1</button>
    <button>删除cookie则通过将过期时间调整到已过期时间</button>
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

    setCookie() {

      const date = new Date();
      date.setTime(date.getTime() + (1 * 60 * 1000));  // 单位：分钟
      const expires = "expires=" + date.toUTCString();

      // 格式： key=value;过期时间；   
      // encodeURIComponent: 对特殊字符进行转换
      document.cookie = "name=" + encodeURIComponent(1) + ";" + expires + ";";

    },




    getCookie() {

      // 如果存在多个cookie，通过；进行拆分
      const cookies = document.cookie.split('; ');

      // 通过for循环去寻找目标cookie
      for (let i = 0; i < cookies.length; i++) {
        const [cookieName, cookieValue] = cookies[i].split('=');
        if (cookieName === "name") {
          console.log(cookieValue)
          alert(cookieValue)
        }
      }

    },


    addCookie() {

      // 读取cookie
      const cookies = document.cookie.split('; ');
      for (let i = 0; i < cookies.length; i++) {
        const [cookieName, cookieValue] = cookies[i].split('=');
        if (cookieName === "name") {

          // 重新设置cookie
          const date = new Date();
          date.setTime(date.getTime() + (1 * 60 * 1000));  // 分钟
          const expires = "expires=" + date.toUTCString();
          document.cookie = "name=" + encodeURIComponent(parseInt(cookieValue, 10) + 1) + ";" + expires + ";";

        }
      }



    }

  }
}


</script>


<style>
div {

  margin-left: 25%;
  margin-top: 5%;
}

button{
  margin-left: 2%;
}
</style>