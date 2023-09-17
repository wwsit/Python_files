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
    /* width: 400px; */

    /* justify-content:center;  */

  
}

.flex-container span {
    background-color: antiquewhite;
    width: 100px;
    height: 100px;
    margin-left: 2%;
    flex-grow: 2;

}

.flex-container div {
    background-color: aqua;
    width: 100px;
    height: 100px;
    margin-left: 2%;
    flex-grow: 1;

}
</style>
  