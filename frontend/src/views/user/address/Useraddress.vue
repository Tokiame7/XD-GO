<template>
    <div class="address-container">

      <!--   <el-button type="primary" @click="handleAdd">新增地址</el-button> -->

        <el-table :data="addressList">
            <el-table-column prop="name" label="收货人" />
            <el-table-column prop="phone" label="联系电话" />

             <!-- <el-table-column prop="fullAddress" label="详细地址" /> -->

            <el-table-column prop="shipping_address" label="收货地址" /> <!--直接显示单个地址 -->
            <el-table-column label="操作">
                <template #default="{ row }">
                    <el-button @click="handleEdit(row.id)">编辑</el-button>

                  <!--  <el-button @click="handleDelete(row.id)">删除</el-button> -->

                </template>
            </el-table-column>
        </el-table>
    </div>
</template>

<script setup>
import { onMounted, ref } from 'vue'
import { getAddressList } from '@/api/user' // 删除 deleteAddress 导入
import { ElMessage } from 'element-plus'

const addressList = ref([])

// 获取地址列表
// 修改后的获取地址方法
const loadAddress = async () => {
    const res = await getAddressList()
    addressList.value = [{
        id: 'default',
        fullAddress: res.data.shipping_address || '暂无收货地址'
    }]
}


onMounted(() => loadAddress())
</script>