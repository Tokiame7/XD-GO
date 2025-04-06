<template>
  <div class="user-form">
    <el-form
      :model="form"
      class="form"
      label-width="auto"
      style="max-width: 600px"
      label-position="top"
    >
      <el-form-item label="用户名">
        <el-input v-model="form.name" />
      </el-form-item>
      <el-form-item label="用户电话">
        <el-input v-model="form.phone" />
      </el-form-item>
      <el-form-item label="用户邮箱">
        <el-input v-model="form.email" />
      </el-form-item>
      <el-form-item label="用户地址" v-if="userStore.userInfo.role === 'buyer'">
        <el-input v-model="form.shipping_address" />
      </el-form-item>

    <el-button type="primary" @click="goToEdit">修改个人信息</el-button>

      <el-form-item>
        <!--<el-button type="primary" @click="onSubmit">修改</el-button>-->
        <el-button @click="cancel">返回主页</el-button>

        <el-button
          type="success"
          @click="goToAddressManage"
          v-if="userStore.userInfo.role === 'buyer'"
        >管理收货地址</el-button>

      </el-form-item>
    </el-form>
  </div>
</template>

<script setup>
import { reactive, onMounted } from 'vue'
import { useUserStore } from '@/stores/user'
import { ElMessage } from 'element-plus'
import { useRouter } from 'vue-router'
import { getUserInfo } from '@/api/user'

const userStore = useUserStore()
const router = useRouter()
const form = reactive({
  name: userStore.userInfo.username,
  phone: userStore.userInfo.phone,
  email: userStore.userInfo.email,
  shipping_addres: userStore.userInfo.shipping_address,
})
const loadInfo = async () => {
  try {
    const { data } = await getUserInfo()
    Object.assign(form, {
      name: data.username,
      phone: data.phone,
      email: data.email,
      shipping_address: data.shipping_address,
    })
  } catch (error) {
    console.error('数据加载失败:', error.response.data.message)
    ElMessage.error('数据加载失败')
  }
}

onMounted(() => {
  loadInfo()
})

// 更新用户信息
/* const onSubmit = () => {
  // 修改用户信息
  userStore.updateUserName(form.name)
  // console.log('submit!')
  ElMessage.success('修改成功')
  router.push('/')
}*/

// 取消修改
const cancel = () => {
  router.push('/')
}

// 新增路由跳转方法
const goToAddressManage = () => {
  router.push('/address')
}

// 新增跳转方法
const goToEdit = () => {
    router.push('/user/edit')
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
