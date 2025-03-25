import axios from 'axios'
import { ElMessage } from 'element-plus'
import { useUserStore } from '@/stores/user'

const request = axios.create({
  baseURL: 'http://127.0.0.1:5001',
  timeout: 10000
})

// 请求拦截器
request.interceptors.request.use(
  config => {
    const userStore = useUserStore()
    // 设置 Content-Type
    config.headers['Content-Type'] = 'application/json'
    if (userStore.token) {
      config.headers.Authorization = `Bearer ${userStore.token}`
    }
    return config
  },
  error => {
    return Promise.reject(error)
  }
)

// 响应拦截器
request.interceptors.response.use(
  response => {
    const { status, statusText, data } = response
    if (status === 200) {
      return data
    }
    ElMessage.error(statusText || '请求失败')
    return Promise.reject(new Error(statusText || '请求失败'))
  },
  error => {
    if (error.response && error.response.status === 401) {
      // const userStore = useUserStore()
      // userStore.clearUser()
      // window.location.href = '/login'
    }
    ElMessage.error(error.message || '请求失败')
    return Promise.reject(error)
  }
)

export default request
