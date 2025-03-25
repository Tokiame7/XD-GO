export default {
  path: '/seller',
  component: () => import('@/layouts/SellerLayout.vue'),
    children :[
    {
      path:'/',
      name: 'Myproducts',
      component: () => import('@/views/seller/seller_myproducts/index.vue'),
      meta: {
        title: '我的商品',
      },
    },
    {
      path:'/addproducts',
      name: 'Addproducts',
      component: () => import('@/views/seller/seller_addproducts/index.vue'),
      meta: {
        title: '添加商品',
      },
    }
  ],
}
