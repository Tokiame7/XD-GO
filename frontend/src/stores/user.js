// import { updateUserInfo } from '@/api/user'
// import { update } from 'lodash-es'
import { defineStore } from 'pinia'

export const useUserStore = defineStore('user', {
  state: () => ({
    token: localStorage.getItem('token'),
    userInfo: JSON.parse(localStorage.getItem('userInfo') || '{}'),
  }),

  getters: {
    isLoggedIn: (state) => !!state.token,
  },

  actions: {
    setUser(token, userInfo) {
      this.token = token
      this.userInfo = userInfo
      localStorage.setItem('token', token)
      localStorage.setItem('userInfo', JSON.stringify(userInfo))
    },

    updateUserName(newName) {
      this.userInfo = { ...this.userInfo, username: newName }
      localStorage.setItem('userInfo', JSON.stringify(this.userInfo))
    },

    clearUser() {
      this.token = null
      this.userInfo = {}
      localStorage.removeItem('token')
      localStorage.removeItem('userInfo')
    },
  },
})
