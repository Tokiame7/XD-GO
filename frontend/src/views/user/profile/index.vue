<template>
  <div class="user-form">
    <el-form :model="form" class="form" label-width="auto" style="max-width: 600px" label-position="top">
      <el-form-item label="用户名">
        <el-input v-model="form.name" />
      </el-form-item>
      <el-form-item label="用户电话">
        <el-input v-model="form.phone" />
      </el-form-item>

      <el-form-item>
        <el-button type="primary" @click="onSubmit">修改</el-button>
        <el-button @click="cancel">取消</el-button>

        <el-button type="success" @click="goToAddressManage">管理收货地址</el-button>
        
      </el-form-item>
    </el-form>
  </div>
</template>

<script setup>
import { reactive } from 'vue'
import { useUserStore } from '@/stores/user'
import { ElMessage } from 'element-plus'
import { useRouter } from 'vue-router'

const userStore = useUserStore()
const router = useRouter()

// 用户信息表单数据
const form = reactive({
  name: userStore.userInfo.username,
  phone: userStore.userInfo.phone
})
// 更新用户信息
const onSubmit = () => {
  // 修改用户信息
  userStore.updateUserName(form.name)
  // console.log('submit!')
  ElMessage.success('修改成功')
  router.push('/')
}

// 取消修改
const cancel = () => {
  router.push('/')
}

// 新增路由跳转方法
const goToAddressManage = () => {
    router.push('/address')
}


</script>

<style scoped lang="scss">
.user-form {
  width: 100%;
  max-width: 1200px;
  margin: 0 auto;
  padding: 20px;
  .form {
    margin-top: 20px;
    margin: 0 auto;
  }
}
</style>