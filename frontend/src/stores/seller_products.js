// 导入一个defineStore 方法
import { defineStore } from 'pinia'
import { ref } from 'vue'//ref 让数据变为响应式数据 ref()\ref([]) 可以是单个数据、数组、对象
import { Axios } from 'axios'
//pinia 就是打包数据和方法让这些数据在几个组件间被统一管理
import { getShopProducts } from '@/api/seller'


export const useSellerProucts = defineStore('sellreproducts', () => {//第一个属性是唯一属性
  //定义数据
  const sellerProductsList = ref([])

  //定义修改数据的方法(action 同步+异步)


  const getSellerProductsList = async (params) => {
    try {
      // 使用 await 等待 Promise 解决
      const res = await getShopProducts(params);
      // 赋值响应数据中的商品列表
      sellerProductsList.value = res.data;
    } catch (error) {
      // 处理请求错误
      console.error('获取卖家商品列表失败:', error);
    }
  };

  //导出需要的数据和方法
  return {
    sellerProductsList,
    getSellerProductsList
  }
})


