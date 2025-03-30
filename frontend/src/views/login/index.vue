<template>
  <div class="login-container">
    <div class="login-box">
      <h2>User Login</h2>

      <!-- Login type toggle -->
      <div class="login-type">
        <el-radio-group v-model="loginType">
          <el-radio-button value="account">Account Login</el-radio-button>
          <!-- <el-radio-button value="phone">SMS Code Login</el-radio-button> -->
        </el-radio-group>
      </div>

      <!-- Account login form -->
      <el-form v-if="loginType === 'account'" ref="accountFormRef" :model="accountForm" :rules="accountRules">
        <el-form-item prop="username">
          <el-input v-model="accountForm.username" placeholder="Please enter username" prefix-icon="User" />
        </el-form-item>
        <el-form-item prop="password">
          <el-input v-model="accountForm.password" type="password" placeholder="Please enter password"
            prefix-icon="Lock" show-password />
        </el-form-item>
      </el-form>

      <!-- SMS code login form -->
      <!-- <el-form v-else ref="phoneFormRef" :model="phoneForm" :rules="phoneRules">
        <el-form-item prop="phone">
          <el-input v-model="phoneForm.phone" placeholder="Please enter phone number" prefix-icon="Iphone" />
        </el-form-item>
        <el-form-item prop="code">
          <div class="verify-code">
            <el-input v-model="phoneForm.code" placeholder="Please enter verification code" prefix-icon="Key" />
            <el-button :disabled="!!countdown" @click="handleSendCode">
              {{ countdown ? `Resend in ${countdown}s` : 'Get Verification Code' }}
            </el-button>
          </div>
        </el-form-item>
      </el-form> -->

      <!-- Remember password -->
      <!-- <div class="remember" v-if="loginType === 'account'">
        <el-checkbox v-model="remember">Remember password</el-checkbox>
         <el-link type="primary" @click="handleForgotPassword">Forgot password?</el-link>
      </div> -->

      <!-- Login button -->
      <el-button type="primary" :loading="loading" class="submit-btn" @click="handleLogin">
        Login
      </el-button>

      <!-- Register link -->
      <div class="register">
        Don't have an account?
        <el-link type="primary" @click="handleRegister">Register now</el-link>
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

// Login type
const loginType = ref('account')

// Account login form
const accountFormRef = ref()
const accountForm = reactive({
  username: '',
  password: ''
})
const accountRules = {
  username: [
    { required: true, message: 'Please enter username/phone/email', trigger: 'blur' }
  ],
  password: [
    { required: true, message: 'Please enter password', trigger: 'blur' },
    { min: 6, message: 'Password must be at least 6 characters', trigger: 'blur' }
  ]
}

// Login handler
const loading = ref(false)
const handleLogin = async () => {
  try {
    loading.value = true

    // Form validation
    const formRef = accountFormRef.value
    await formRef.validate()

    // Send request
    const { data } = await login(JSON.parse(JSON.stringify(accountForm)))
    console.log(data);
    userStore.setUser(data.token, {
      userId: data.userid,
      username: data.username,
      role: data.role
    })

    // Login success
    ElMessage.success('Login successful')
    if (data.role === 'seller') {
      router.push('/seller')
    } else if (data.role === 'buyer') {
      router.push('/')
    }
  } catch (error) {
    console.error('Login failed:', error.response.data.message)
    ElMessage.error(error.response.data.message)
  } finally {
    loading.value = false
  }
}

// Register
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