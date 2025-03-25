import { defineStore } from 'pinia'

// 模拟购物车数据
const mockCartItems = [
  {
    id: 1,
    name: 'iPhone 15 Pro',
    price: 7999,
    image: 'https://via.placeholder.com/200',
    quantity: 1,
    selected: true,
  },
  {
    id: 2,
    name: '华为 Mate 60 Pro',
    price: 6999,
    image: 'https://via.placeholder.com/200',
    quantity: 2,
    selected: true,
  },
  {
    id: 3,
    name: '小米 14 Pro',
    price: 4999,
    image: 'https://via.placeholder.com/200',
    quantity: 1,
    selected: false,
  },
]

export const useCartStore = defineStore('cart', {
  state: () => ({
    items: mockCartItems,
  }),

  getters: {
    // 商品总数
    count: (state) => state.items.reduce((sum, item) => sum + item.quantity, 0),

    // 已选商品数量
    selectedCount: (state) => state.items.filter((item) => item.selected).length,

    // 已选商品总价
    totalPrice: (state) =>
      state.items
        .filter((item) => item.selected)
        .reduce((sum, item) => sum + item.price * item.quantity, 0),

    // 是否全选
    isAllSelected: (state) => state.items.length > 0 && state.items.every((item) => item.selected),
  },

  actions: {
    // 添加商品到购物车
    addToCart(product, quantity = 1) {
      const existItem = this.items.find((item) => item.id === product.id)
      if (existItem) {
        existItem.quantity += quantity
      } else {
        this.items.push({
          ...product,
          quantity,
          selected: true,
        })
      }
    },

    // 从购物车移除商品
    removeFromCart(productId) {
      const index = this.items.findIndex((item) => item.id === productId)
      if (index > -1) {
        this.items.splice(index, 1)
      }
    },

    // 更新商品数量
    updateQuantity(productId, quantity) {
      const item = this.items.find((item) => item.id === productId)
      if (item) {
        item.quantity = quantity
      }
    },

    // 切换商品选中状态
    toggleSelected(productId) {
      const item = this.items.find((item) => item.id === productId)
      if (item) {
        item.selected = !item.selected
      }
    },

    // 切换全选状态
    toggleSelectAll() {
      const targetValue = !this.isAllSelected
      this.items.forEach((item) => {
        item.selected = targetValue
      })
    },

    // 清空购物车
    clearCart() {
      this.items = []
    },
  },
})
