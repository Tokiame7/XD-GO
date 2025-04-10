export default {
  path: '/seller',
  component: () => import('@/layouts/SellerLayout.vue'),
  children: [
    {
      path: '',
      name: 'Myproducts',
      component: () => {
        console.log('正在加载我的商品页');
        return import('@/views/seller/seller_myproducts/index.vue')
      },
      meta: {
        title: '我的商品',
      },
    },
    {
      path: '/addproducts',
      name: 'Addproducts',
      component: () => {
        console.log('正在加载添加商品页');
        return import('@/views/seller/seller_addproducts/index.vue')
      },
      meta: {
        title: '添加商品',
      },
    },
    {
      path: '/sellerorders',
      name: 'SellerOrders',
      component: () => {
        console.log('正在加载订单页');
        return import('@/views/seller/seller_order/index.vue')
      },
      meta: {
        title: '我的订单',
      },
    }
  ],
}
