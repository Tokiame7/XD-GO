<template>
  <div class="shop-layout">
    <!-- 顶部导航栏 -->
    <header class="header">
      <div class="header-content">
        <!-- 左侧导航 -->
        <div class="nav-left">
          <router-link to="/seller" class="logo">
            <img src="" alt="logo">
            <span>XD_GO</span>
          </router-link>
          <el-menu mode="horizontal" :router="true" :default-active="activeMenu">
            <el-menu-item index="/seller">MyProducts</el-menu-item>
            <el-menu-item index="/addproducts">EditProducts</el-menu-item>
            <el-menu-item index="/sellerorders">MyOrders</el-menu-item>
            <el-menu-item index="/order">Switch To Buyer</el-menu-item>
          </el-menu>
        </div>

        <!-- 右侧用户信息 -->
        <div class="nav-right">
          <template v-if="isLoggedIn">
            <el-dropdown @command="handleUserCommand">
              <div class="user-info">
                <el-avatar :size="32" :src="userAvatar" />
                <span class="username">{{ username }}</span>
              </div>
              <template #dropdown>
                <el-dropdown-menu>
                  <el-dropdown-item command="profile">个人信息</el-dropdown-item>
                  <el-dropdown-item divided command="logout">退出登录</el-dropdown-item>
                </el-dropdown-menu>
              </template>
            </el-dropdown>
          </template>
          <template v-else>
            <el-button text @click="handleLogin">登录</el-button>
            <el-button type="primary" @click="handleRegister">注册</el-button>
          </template>
        </div>
      </div>
    </header>

    <!-- 主要内容区 -->
    <main class="main-content">
      <router-view v-slot="{ Component }">
        <transition name="fade" mode="out-in">
          <component :is="Component" />
        </transition>
      </router-view>
    </main>

    <!-- 底部信息 -->
    <footer class="footer">
      <div class="footer-content">
        <div class="footer-section">
          <h3>关于我们</h3>
          <ul>
            <li><a href="#">公司简介</a></li>
            <li><a href="#">联系我们</a></li>
            <li><a href="#">招贤纳士</a></li>
            <li><a href="#">商务合作</a></li>
          </ul>
        </div>
        <div class="footer-section">
          <h3>帮助中心</h3>
          <ul>
            <li><a href="#">购物指南</a></li>
            <li><a href="#">支付方式</a></li>
            <li><a href="#">配送方式</a></li>
            <li><a href="#">售后服务</a></li>
          </ul>
        </div>
        <div class="footer-section">
          <h3>商家服务</h3>
          <ul>
            <li><a href="#">商家入驻</a></li>
            <li><a href="#">商家后台</a></li>
            <li><a href="#">商家帮助</a></li>
            <li><a href="#">规则中心</a></li>
          </ul>
        </div>
        <div class="footer-section">
          <h3>关注我们</h3>
          <div class="qrcode">
            <img src="" alt="二维码">
            <p>扫码关注公众号</p>
          </div>
        </div>
      </div>
      <div class="copyright">
        <p>Copyright © 2024 XD商城 All Rights Reserved.</p>
      </div>
    </footer>
  </div>
</template>

<script setup>
import { ref, computed } from 'vue'
import { useRouter, useRoute } from 'vue-router'
import { ElMessage } from 'element-plus'
import { useUserStore } from '@/stores/user'

const router = useRouter()
const route = useRoute()
const userStore = useUserStore()

// 当前激活的菜单
const activeMenu = computed(() => route.path)

// 用户信息相关
const isLoggedIn = ref(userStore.token) // TODO: 从store中获取登录状态
const userAvatar = ref(userStore.userInfo.avatar) // TODO: 从store中获取用户头像
const username = ref(userStore.userInfo.username) // TODO: 从store中获取用户名


const handleUserCommand = (command) => {
  switch (command) {
    case 'profile':
      router.push('/user')
      break
    case 'logout':
      handleLogout()
      break
  }
}

const handleLogout = () => {
  // TODO: 实现登出功能
  userStore.clearUser()
  ElMessage.success('退出成功')
  isLoggedIn.value = false
}

// 登录相关
const handleLogin = () => {
  router.push('/login')
}

// 注册相关
const handleRegister = () => {
  router.push('/register')
}

</script>

<style lang="scss" scoped>
.shop-layout {
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  background-color: #f5f5f5;

  .header {
    background-color: #fff;
    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
    position: fixed;
    top: 0;
    left: 0;
    right: 0;
    z-index: 100;
    height: 60px;

    .header-content {
      max-width: 1200px;
      margin: 0 auto;
      height: 100%;
      display: flex;
      align-items: center;
      justify-content: space-between;
      padding: 0 20px;

      @media (max-width: 768px) {
        padding: 0 10px;
      }

      .nav-left {
        display: flex;
        align-items: center;

        .logo {
          display: flex;
          align-items: center;
          margin-right: 40px;
          text-decoration: none;
          color: #333;

          img {
            width: 32px;
            height: 32px;
            margin-right: 8px;
          }

          span {
            font-size: 20px;
            font-weight: bold;
          }
        }

        .el-menu {
          border-bottom: none;
        }
      }

      .search-box {
        width: 400px;

        .el-input {
          :deep(.el-input__wrapper) {
            border-radius: 20px;
          }
        }
      }

      .nav-right {
        display: flex;
        align-items: center;
        gap: 16px;

        .user-info {
          display: flex;
          align-items: center;
          cursor: pointer;

          .username {
            margin-left: 8px;
            color: #333;
          }
        }
      }
    }
  }

  .main-content {
    flex: 1;
    margin-top: 60px; // 头部高度
    padding-bottom: 40px; // 添加底部内边距，防止内容紧贴footer

    @media (max-width: 768px) {
      padding-bottom: 20px;
    }
  }

  .footer {
    margin-top: auto; // 确保footer始终在底部
    background-color: #f5f5f5;
    padding: 40px 0 20px;
    width: 100%;

    @media (max-width: 768px) {
      padding: 20px 0 10px;
    }

    .footer-content {
      max-width: 1200px;
      margin: 0 auto;
      padding: 0 20px;
      display: flex;
      justify-content: space-between;
      flex-wrap: wrap;
      gap: 20px;

      @media (max-width: 768px) {
        padding: 0 10px;
        flex-direction: column;
        gap: 15px;
      }

      .footer-section {
        flex: 1;
        min-width: 200px;

        @media (max-width: 768px) {
          min-width: 100%;
          text-align: center;
        }

        h3 {
          font-size: 16px;
          margin-bottom: 20px;
        }

        ul {
          list-style: none;
          padding: 0;
          margin: 0;

          li {
            margin-bottom: 12px;

            a {
              color: #666;
              text-decoration: none;

              &:hover {
                color: #409eff;
              }
            }
          }
        }

        .qrcode {
          text-align: center;

          img {
            width: 120px;
            height: 120px;
            margin-bottom: 8px;
          }

          p {
            color: #666;
            font-size: 12px;
          }
        }
      }
    }

    .copyright {
      text-align: center;
      margin-top: 40px;
      padding-top: 20px;
      border-top: 1px solid #ddd;
      color: #999;
      font-size: 12px;
    }
  }
}

.code-input {
  display: flex;
  gap: 12px;

  .el-input {
    flex: 1;
  }

  .el-button {
    width: 100px;
  }
}

.forget-pwd {
  float: right;
}

// 路由过渡动画
.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.3s ease;
}

.fade-enter-from,
.fade-leave-to {
  opacity: 0;
}
</style>
