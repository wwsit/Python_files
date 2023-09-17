<template>
    <div class="flex-container">
        <span>flex item1</span>
        <div>flex item2</div>
        <span>flex item3</span>
    </div>
</template>
  
<script>

</script>
  
<style scoped>
.flex-container {
    display: flex;

    /* flex-direction: row; */
    /* flex-direction:column; */
    /* flex-direction:row-reverse;  */
    flex-direction:  column-reverse;
}

.flex-container span{
    background-color: antiquewhite;
    width: 100px;
    height: 100px;
    margin-left: 2%;
    
}

.flex-container div{
    background-color: aqua;
    width: 100px;
    height: 100px;
    margin-left: 2%;
}
</style>
  