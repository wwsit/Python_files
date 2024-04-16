<template>
  <el-upload ref="upload" class="upload-demo" action="" :limit="1" :on-exceed="handleExceed" :auto-upload=false
    :on-change="handleSuccess" :on-remove="handleRemove" :file-list="fileList" :on-preview="handleFile">

    <template #trigger>
      <el-button type="primary">上传excel文件</el-button>
    </template>
    <template #tip>
      <div class="el-upload__tip text-red">
        请上传.png格式的图片
      </div>
    </template>
  </el-upload>

  <el-button type="primary" @click="getData()" class="click_button">加载附件</el-button>
</template>

<script>
import { genFileId } from 'element-plus'
import axios from 'axios'
export default {


  data() {
    return {
      fileList: [],
      upload: "",
      add_download_url:"",

    }
  },

  methods: {


    // 只能上传一个文件
    handleExceed(files) {
      console.log(files)
      this.$refs.upload.clearFiles()
      const file = files[0]
      file.uid = genFileId()
      this.$refs.upload.handleStart(file)
    },


    open2(msg) {
      this.$message({
        message: msg,
        type: 'error',
      })
    },

    // 文件上传成功
    handleSuccess(file, fileList) {
      let filename = file.raw.name
      if (filename.indexOf(".png") != -1) {
        this.upload = file.raw  // 以文件对象的形式传给后端

        let formData = new FormData()
        formData.append('files', this.upload)
        formData.append("oaid", "test")

        axios({
          url: "http://192.168.255.10:5000" + "/api/saveData",
          method: "post",
          data: formData,
        }).then((res) => {
          if (res.data.result == "success") {
          }
          else {
            console.log(res)
          }

        }).catch((error) => {
          console.log(error)
        })



      } else {
        this.open2("请上传.png格式的图片")
        this.$refs.upload.clearFiles()
      }


    },


    // 移除文件
    handleRemove(file, fileList) {
      this.upload = ""
      this.add_download_url = ""
    },


    // 点击上传列表中的文件，进行下载
    handleFile(files) {
      window.open(this.add_download_url, '_blank');
    },


    // 加载附件的格式
    getData() {
      this.fileList = [{ name: "test.png", url: "https://d1.lanrentuku.com/upload/img/sucaiku/202010130648/5f84dd29906d3.png" }]
    },


  },


  mounted() {

  },


}
</script>

<style lang="less">
.upload-demo {

  margin-top: 5%;
  margin-left: 50%;
  width: 500px;
}


.click_button {
  margin-left: 50%;
  margin-top: 5%;
}
</style>