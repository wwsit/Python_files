<template>
  <div class="first">
    <span>哈哈哈哈</span>
  </div>

  <div class="second">
    <div class="secord_img"><img src="./img/image.png"></div>
    <div class="second_text_1">hahahah</div>
    <span> 33331`</span>
    <div class="second_text_2">111111</div>
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
.first {
  margin-top: 5%;
  display: flex;
  justify-content: center;
  /* 设置使内容居中 */

}

.second{
  display: flex;
}

.secord_img {

}

img {
  width: 10rem;
  height: 10rem;
}


.second_text_1 {
  background:papayawhip;

  /* 将块元素转成 内联块元素 */
  display: inline-block;

  /* 占有剩余的空间 */
  flex-grow: 1;
}
</style>