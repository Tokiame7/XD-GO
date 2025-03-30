<template>
  <div class="register-container">
    <div class="register-box">
      <h2>User Registration</h2>

      <el-form ref="formRef" :model="form" :rules="rules">
        <el-form-item prop="username">
          <el-input v-model="form.username" placeholder="Please enter username" prefix-icon="User" />
        </el-form-item>

        <el-form-item prop="password">
          <el-input v-model="form.password" type="password" placeholder="Please enter password" prefix-icon="Lock"
            show-password />
        </el-form-item>

        <el-form-item prop="confirmPassword">
          <el-input v-model="form.confirmPassword" type="password" placeholder="Please confirm password"
            prefix-icon="Lock" show-password />
        </el-form-item>

        <el-form-item prop="phone">
          <el-input v-model="form.phone" placeholder="Please enter phone number" prefix-icon="Iphone" />
        </el-form-item>

        <el-form-item prop="email">
          <el-input v-model="form.email" placeholder="Please enter email" prefix-icon="Iphone" />
        </el-form-item>

        <el-form-item>
          <el-radio-group v-model="form.role">
            <el-radio-button value="seller">Register as Seller</el-radio-button>
            <el-radio-button value="buyer">Register as Buyer</el-radio-button>
          </el-radio-group>
        </el-form-item>

        <el-form-item>
          <el-button type="primary" :loading="loading" class="submit-btn" @click="handleRegister">
            Register
          </el-button>
        </el-form-item>
      </el-form>

      <!-- Login link -->
      <div class="login">
        Already have an account?
        <el-link type="primary" @click="handleLogin">Login now</el-link>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, reactive } from 'vue'
import { useRouter } from 'vue-router'
import { ElMessage } from 'element-plus'
import { register } from '@/api/user'
// import { User, Lock, Iphone, Key } from '@element-plus/icons-vue'

const router = useRouter()

// Registration form
const formRef = ref()
const form = reactive({
  username: '',
  password: '',
  confirmPassword: '',
  phone: '',
  email: '',
  role: 'buyer'
})

// Form validation rules
const rules = {
  username: [
    { required: true, message: 'Please enter username', trigger: 'blur' },
    { min: 3, max: 20, message: 'Username must be between 3-20 characters', trigger: 'blur' }
  ],
  password: [
    { required: true, message: 'Please enter password', trigger: 'blur' },
    { min: 6, message: 'Password must be at least 6 characters', trigger: 'blur' }
  ],
  confirmPassword: [
    { required: true, message: 'Please confirm password', trigger: 'blur' },
    {
      validator: (rule, value, callback) => {
        if (value !== form.password) {
          callback(new Error('Passwords do not match'))
        } else {
          callback()
        }
      },
      trigger: 'blur'
    }
  ],
  phone: [
    { required: true, message: 'Please enter phone number', trigger: 'blur' },
    { pattern: /^1[3-9]\d{9}$/, message: 'Invalid phone number format', trigger: 'blur' }
  ],
  email: [
    { required: true, message: 'Please enter email', trigger: 'blur' },
  ]
}

// Registration handler
const loading = ref(false)
const handleRegister = async () => {
  try {
    loading.value = true

    // Form validation
    await formRef.value.validate()

    delete form.confirmPassword
    console.log(JSON.stringify(form));

    // Send registration request
    const res = await register(JSON.stringify(form))
    console.log(res)

    // Registration success message
    ElMessage.success('Registration successful')

    // Redirect to login page
    router.push('/login')

  } catch (error) {
    console.error('Registration failed:', error)
    ElMessage.error(error)
  } finally {
    loading.value = false
  }
}

// Redirect to login
const handleLogin = () => {
  router.push('/login')
}
</script>

<style lang="scss" scoped>
.register-container {
  display: flex;
  justify-content: center;
  align-items: center;
  min-height: 100vh;
  background-color: #f5f7fa;

  .register-box {
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

    .submit-btn {
      width: 100%;
      margin-bottom: 20px;
    }

    .login {
      text-align: center;
    }
  }
}
</style>