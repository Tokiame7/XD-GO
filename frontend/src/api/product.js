import request from '@/utils/request'

// 获取商品列表
export function getProductList(params) {
  return request({
    url: '/products',
    method: 'get',
    params
  })
}

// 获取商品详情
export function getProductDetail(id) {
  return request({
    url: `/products/${id}`,
    method: 'get'
  })
}

// 获取商品分类
export function getCategories() {
  return request({
    url: '/categories',
    method: 'get'
  })
}

// 卖家 - 创建商品
export function createProduct(data) {
  return request({
    url: '/seller/products',
    method: 'post',
    data
  })
}

// 卖家 - 更新商品
export function updateProduct(id, data) {
  return request({
    url: `/seller/products/${id}`,
    method: 'put',
    data
  })
}

// 卖家 - 删除商品
export function deleteProduct(id) {
  return request({
    url: `/seller/products/${id}`,
    method: 'delete'
  })
}
