window.onload = function () {

    // 只有valu属性的标签，在获取值的使用才可以使用document.getElementById("xxx").value
    // 否则只能使用document.getElementById("xxx").innerText去获取显示的值

    // 获取div标签 显示的值
    let id1_value = document.getElementById("id1").innerText
    // 修改div标签 显示的值
    document.getElementById("id1").innerText = "3333"

    // 获取button标签 显示的值
    let id2_value = document.getElementById("id2").innerText
    // 修改button标签 显示的值
    document.getElementById("id2").innerText = "新的button值"

    // 获取input标签 显示的值
    let id3_value = document.getElementById("id3").value
    // 修改input标签 显示的值
    document.getElementById("id3").setAttribute("value", "input新值")


    // 获取属性的值
    let id4_value = document.getElementById("id4").getAttribute("class")
    // 设置属性值
    document.getElementById("id4").setAttribute("class", "设置新的属性值")

    // 设置按钮不可点击 true和 false值用小写
    document.getElementById("id5").disabled = true
    // 设置按钮可以点击
    // document.getElementById("id5").disabled= false

    // 调整样式-修改字体颜色
    document.getElementById("id4").style.color = "red"


    // 表格数据
    let result = [["a", 18, "A班"], ["b", 19, "A班"], ["c", 20, "B班"]]
    for (let i = 0; i < result.length; i++) { //对stus进行循环遍历，并建立tr标签
        // 只有jquery语法能使用append方法
        $("#table_value").append(
            "<tr id='table'>" +
            "<td><div id='tb_xuhao'>" + (i + 1) + "</div></td>" +
            "<td><div id='tb_name'>" + result[i][0] + "</div></td>" +
            "<td><div id='tb_age'>" + result[i][1] + "</div></td>" +
            "<td><div id='tb_class'>" + result[i][2] + "</div></td>" +
            "</tr>"
        )
    }


}

// 按钮点击事件
function ButtonClick() {
    alert("按钮点击了")
}

// 按钮失焦事件
function ButtonBlur() {
    alert("按钮失焦")
}