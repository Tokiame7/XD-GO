<template>
  <div class="register-container">
    <div class="register-box">
      <h2>用户注册</h2>

      <el-form ref="formRef" :model="form" :rules="rules">
        <el-form-item prop="username">
          <el-input v-model="form.username" placeholder="请输入用户名" prefix-icon="User" />
        </el-form-item>

        <el-form-item prop="password">
          <el-input v-model="form.password" type="password" placeholder="请输入密码" prefix-icon="Lock" show-password />
        </el-form-item>

        <el-form-item prop="confirmPassword">
          <el-input v-model="form.confirmPassword" type="password" placeholder="请确认密码" prefix-icon="Lock"
            show-password />
        </el-form-item>

        <el-form-item prop="phone">
          <el-input v-model="form.phone" placeholder="请输入手机号" prefix-icon="Iphone" />
        </el-form-item>

        <el-form-item prop="email">
          <el-input v-model="form.email" placeholder="请输入邮箱" prefix-icon="Iphone" />
        </el-form-item>

        <el-form-item>
          <el-radio-group v-model="form.role">
            <el-radio-button value="seller">卖家注册</el-radio-button>
            <el-radio-button value="buyer">买家注册</el-radio-button>
          </el-radio-group>
        </el-form-item>

        <el-form-item>
          <el-button type="primary" :loading="loading" class="submit-btn" @click="handleRegister">
            注册
          </el-button>
        </el-form-item>
      </el-form>

      <!-- 登录链接 -->
      <div class="login">
        已有账号？
        <el-link type="primary" @click="handleLogin">立即登录</el-link>
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

// 注册表单
const formRef = ref()
const form = reactive({
  username: '',
  password: '',
  confirmPassword: '',
  phone: '',
  email: '',
  role: 'buyer'
})

// 表单验证规则
const rules = {
  username: [
    { required: true, message: '请输入用户名', trigger: 'blur' },
    { min: 3, max: 20, message: '用户名长度在3-20个字符之间', trigger: 'blur' }
  ],
  password: [
    { required: true, message: '请输入密码', trigger: 'blur' },
    { min: 6, message: '密码不能少于6位', trigger: 'blur' }
  ],
  confirmPassword: [
    { required: true, message: '请确认密码', trigger: 'blur' },
    {
      validator: (rule, value, callback) => {
        if (value !== form.password) {
          callback(new Error('两次输入的密码不一致'))
        } else {
          callback()
        }
      },
      trigger: 'blur'
    }
  ],
  phone: [
    { required: true, message: '请输入手机号', trigger: 'blur' },
    { pattern: /^1[3-9]\d{9}$/, message: '手机号格式不正确', trigger: 'blur' }
  ],
  email: [
    { required: true, message: '请输入邮箱', trigger: 'blur' },
  ]
}

// 注册处理
const loading = ref(false)
const handleRegister = async () => {
  try {
    loading.value = true

    // 表单验证
    await formRef.value.validate()

    delete form.confirmPassword
    console.log(JSON.stringify(form));

    // 发送注册请求
    const res = await register(JSON.stringify(form))
    console.log(res)

    // 注册成功提示
    ElMessage.success('注册成功')

    // 跳转到登录页
    router.push('/login')

  } catch (error) {
    console.error('注册失败:', error)
    ElMessage.error(error)
  } finally {
    loading.value = false
  }
}

// 跳转登录
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
