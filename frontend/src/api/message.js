import request from '@/utils/request'

// 获取消息列表
export function getMessageList(params) {
  return request({
    url: '/message/list',
    method: 'get',
    params
  })
}

// 标记消息已读
export function readMessage(id) {
  return request({
    url: `/message/${id}/read`,
    method: 'put'
  })
}

// 标记全部已读
export function readAllMessages() {
  return request({
    url: '/message/read-all',
    method: 'put'
  })
}

// 删除消息
export function deleteMessage(id) {
  return request({
    url: `/message/${id}`,
    method: 'delete'
  })
}

// 删除已读消息
export function deleteReadMessages() {
  return request({
    url: '/message/delete-read',
    method: 'delete'
  })
}

// 获取消息设置
export function getMessageSetting() {
  return request({
    url: '/message/setting',
    method: 'get'
  })
}

// 更新消息设置
export function updateMessageSetting(data) {
  return request({
    url: '/message/setting',
    method: 'put',
    data
  })
}

// 获取未读消息数量
export function getUnreadCount() {
  return request({
    url: '/message/unread-count',
    method: 'get'
  })
}
