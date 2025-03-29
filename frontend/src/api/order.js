import request from '@/utils/request'

// 创建订单
export function createOrder(data) {
  return request({
    url: '/order/create',
    method: 'post',
    data
  })
}

// 获取订单信息
export function getOrderInfo(orderId) {
  return request({
    url: `/order/${orderId}`,
    method: 'get'
  })
}

// 获取订单列表
export function getOrderList() {
  return request({
    url: '/api/sell_order/list',
    method: 'get',
  })
}

// 获取订单详情
export function getOrderDetail(id) {
  return request({
    url: `/orders/${id}`,
    method: 'get'
  })
}

// 取消订单
export function cancelOrder(orderId) {
  return request({
    url: `/order/${orderId}/cancel`,
    method: 'post'
  })
}

// 确认收货
export function confirmReceive(orderId) {
  return request({
    url: `/order/${orderId}/receive`,
    method: 'post'
  })
}

// 删除订单
export function deleteOrder(orderId) {
  return request({
    url: `/order/${orderId}`,
    method: 'delete'
  })
}

// 卖家 - 获取订单列表
export function getSellerOrders(params) {
  return request({
    url: '/seller/orders',
    method: 'get',
    params
  })
}

// 卖家 - 发货 修改订单状态
export function shipOrder(id, status) {
  return request({
    url: `/api/sell_order/updateStatus`,
    method: 'put',
    data: {
      orderid: id,
      status: status
    }
  })
}

// 创建支付
export function createPayment(data) {
  return request({
    url: '/payment/create',
    method: 'post',
    data
  })
}

// 查询支付状态
export function queryPaymentStatus(orderId) {
  return request({
    url: `/payment/${orderId}/status`,
    method: 'get'
  })
}

// 申请退款
export function applyRefund(orderId, data) {
  return request({
    url: `/order/${orderId}/refund`,
    method: 'post',
    data
  })
}

// 获取退款详情
export function getRefundInfo(orderId) {
  return request({
    url: `/order/${orderId}/refund`,
    method: 'get'
  })
}
