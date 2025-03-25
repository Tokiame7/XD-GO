<template>
  <div class="login-container">
    <div class="login-box">
      <h2>用户登录</h2>

      <!-- 登录方式切换 -->
      <div class="login-type">
        <el-radio-group v-model="loginType">
          <el-radio-button value="account">账号密码登录</el-radio-button>
          <!-- <el-radio-button value="phone">手机验证码登录</el-radio-button> -->
        </el-radio-group>
      </div>

      <!-- 账号密码登录 -->
      <el-form v-if="loginType === 'account'" ref="accountFormRef" :model="accountForm" :rules="accountRules">
        <el-form-item prop="username">
          <el-input v-model="accountForm.username" placeholder="请输入用户名" prefix-icon="User" />
        </el-form-item>
        <el-form-item prop="password">
          <el-input v-model="accountForm.password" type="password" placeholder="请输入密码" prefix-icon="Lock"
            show-password />
        </el-form-item>
      </el-form>

      <!-- 手机验证码登录 -->
      <!-- <el-form v-else ref="phoneFormRef" :model="phoneForm" :rules="phoneRules">
        <el-form-item prop="phone">
          <el-input v-model="phoneForm.phone" placeholder="请输入手机号" prefix-icon="Iphone" />
        </el-form-item>
        <el-form-item prop="code">
          <div class="verify-code">
            <el-input v-model="phoneForm.code" placeholder="请输入验证码" prefix-icon="Key" />
            <el-button :disabled="!!countdown" @click="handleSendCode">
              {{ countdown ? `${countdown}秒后重新获取` : '获取验证码' }}
            </el-button>
          </div>
        </el-form-item>
      </el-form> -->

      <!-- 记住密码 -->
      <!-- <div class="remember" v-if="loginType === 'account'">
        <el-checkbox v-model="remember">记住密码</el-checkbox>
         <el-link type="primary" @click="handleForgotPassword">忘记密码？</el-link>
      </div> -->

      <!-- 登录按钮 -->
      <el-button type="primary" :loading="loading" class="submit-btn" @click="handleLogin">
        登录
      </el-button>

      <!-- 注册链接 -->
      <div class="register">
        还没有账号？
        <el-link type="primary" @click="handleRegister">立即注册</el-link>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, reactive } from 'vue'
import { useRouter } from 'vue-router'
import { ElMessage } from 'element-plus'
// import { User, Lock, Iphone, Key } from '@element-plus/icons-vue'
import { login } from '@/api/user'
import { useUserStore } from '@/stores/user'

const router = useRouter()
const userStore = useUserStore()

// 登录方式
const loginType = ref('account')

// 买家登录还是卖家登录

// 账号密码登录表单
const accountFormRef = ref()
const accountForm = reactive({
  username: '',
  password: ''
})
const accountRules = {
  username: [
    { required: true, message: '请输入用户名/手机号/邮箱', trigger: 'blur' }
  ],
  password: [
    { required: true, message: '请输入密码', trigger: 'blur' },
    { min: 6, message: '密码不能少于6位', trigger: 'blur' }
  ]
}

// 登录处理
const loading = ref(false)
const handleLogin = async () => {
  try {
    loading.value = true

    // 表单验证
    const formRef = accountFormRef.value
    await formRef.validate()

    // 发请求
    const { data } = await login(JSON.parse(JSON.stringify(accountForm)))
    console.log(data);
    userStore.setUser(data.token, {
      userId: data.userid,
      username: data.username,
      role: data.role
    })

    // 登录成功
    ElMessage.success('登录成功')
    if (data.role === 'seller') {
      router.push('/seller')
    } else if (data.role === 'buyer'){
      router.push('/')
    }
  } catch (error) {
    console.error('登录失败:', error.response.data.message)
    ElMessage.error(error.response.data.message)
  } finally {
    loading.value = false
  }
}

// 忘记密码
// const handleForgotPassword = () => {
//   router.push('/forgot-password')
// }

// 注册
const handleRegister = () => {
  router.push('/register')
}
</script>

<style lang="scss" scoped>
.login-container {
  display: flex;
  justify-content: center;
  align-items: center;
  min-height: 100vh;
  background-color: #f5f7fa;

  .login-box {
    width: 400px;
    padding: 40px;
    background-color: #fff;
    border-radius: 4px;
    box-shadow: 0 2px 12px 0 rgba(0, 0, 0, 0.1);

    h2 {
      margin: 0 0 30px;
      text-align: center;
      font-size: 24px;
    }

    .login-type {
      margin-bottom: 30px;
      text-align: center;
    }

    .verify-code {
      display: flex;
      gap: 12px;

      .el-input {
        flex: 1;
      }

      .el-button {
        width: 120px;
      }
    }

    .remember {
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin: 20px 0;
    }

    .submit-btn {
      width: 100%;
      margin-bottom: 20px;
    }

    .register {
      text-align: center;
    }
  }
}
</style>
