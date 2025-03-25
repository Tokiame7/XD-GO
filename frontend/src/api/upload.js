import request from '@/utils/request'

// 上传文件
export function uploadFile(data) {
  return request({
    url: '/upload/file',
    method: 'post',
    headers: {
      'Content-Type': 'multipart/form-data'
    },
    data
  })
}

// 上传图片
export function uploadImage(data) {
  return request({
    url: '/upload/image',
    method: 'post',
    headers: {
      'Content-Type': 'multipart/form-data'
    },
    data
  })
}

// 上传头像
export function uploadAvatar(data) {
  return request({
    url: '/upload/avatar',
    method: 'post',
    headers: {
      'Content-Type': 'multipart/form-data'
    },
    data
  })
}
