<template>
    <div class="flex-container">
        <span>flex item1</span>
        <div>flex item2</div>
        <span>flex item3</span>
        <div>flex item4</div>
    </div>
</template>
  
<script>

</script>
  
<style scoped>
.flex-container {
    display: flex;

    /* flex-wrap: nowra; */

    /* 超出范围会进行换行 */
    flex-wrap: wrap; 
    /* flex-wrap: wrap-reverse; */

    width: 400px;
}

.flex-container span {
    background-color: antiquewhite;
    width: 100px;
    height: 100px;
    margin-left: 2%;

}

.flex-container div {
    background-color: aqua;
    width: 100px;
    height: 100px;
    margin-left: 2%;
}
</style>
  