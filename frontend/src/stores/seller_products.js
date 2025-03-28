// 导入一个defineStore 方法
import { defineStore } from 'pinia'
import { ref } from 'vue'//ref 让数据变为响应式数据 ref()\ref([]) 可以是单个数据、数组、对象
import { Axios } from 'axios'
//pinia 就是打包数据和方法让这些数据在几个组件间被统一管理
import { getShopProducts, getOrderList } from '@/api/seller'
import { getProductDetail, deleteProduct, createProduct } from '@/api/product'
import seller from '@/router/modules/seller'

export const useSellerProucts = defineStore('sellerproducts', () => {//第一个属性是唯一属性
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


export const useGetproductDetail = defineStore('sellergetproductdetail', () => {


  const sellerProductDetail = ref()

  const getSellerProductDetail = async (id) => {
    try {
      const res = await getProductDetail(id);
      sellerProductDetail.value = res.data;
    } catch (error) {
      console.error('获取商品细节失败', error);
    }
  };

  return {
    sellerProductDetail,
    getSellerProductDetail
  }
})
//删除方法
export const useDeleteProduct = defineStore('deleteproduct', () => {

  const deleName = ref([])
  const DeleteProduct = async (proid) => {
    try {
      const res = await deleteProduct(proid);
      deleName.value = res.data
    } catch (error) {
      console.log('删除商品失败', error);
    }
  }

  return {
    DeleteProduct,
    deleName
  }
})
//增加方法
export const useAddProduct = defineStore('addproduct', () => {


  const createProducts = async (data) => {
    try {
      const res = await createProduct(data);
      console.log('添加成功:', res);
      // 刷新商品列表
      sellerProducts.getSellerProductsList();
    } catch (error) {
      console.log('增加商品失败', error);
    }
  }

  return {
    createProducts
  }
})

//获取订单列表
export const useGetOrder = defineStore('getOrder', () => {
  const orderList = ref([])
  const getorders = async () => {
    try {
      const res = await getOrderList();
      console.log('获取订单成功:', res);
      orderList.value = res.data
    } catch (error) {
      console.log('获取订单失败', error);
    }
  }

  return {
    getorders,
    orderList
  }
})