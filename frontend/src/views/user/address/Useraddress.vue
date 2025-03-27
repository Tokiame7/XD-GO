<template>
    <div class="address-container">
        <el-button type="primary" @click="handleAdd">新增地址</el-button>

        <el-table :data="addressList">
            <el-table-column prop="name" label="收货人" />
            <el-table-column prop="phone" label="联系电话" />
            <el-table-column prop="fullAddress" label="详细地址" />
            <el-table-column label="操作">
                <template #default="{ row }">
                    <el-button @click="handleEdit(row.id)">编辑</el-button>
                    <el-button @click="handleDelete(row.id)">删除</el-button>
                </template>
            </el-table-column>
        </el-table>
    </div>
</template>

<script setup>
import { onMounted, ref } from 'vue'
import { getAddressList, deleteAddress } from '@/api/user'
import { ElMessage } from 'element-plus'

const addressList = ref([])

// 获取地址列表
const loadAddress = async () => {
    const res = await getAddressList()
    addressList.value = res.data
}

// 删除地址
const handleDelete = async (id) => {
    await deleteAddress(id)
    ElMessage.success('删除成功')
    loadAddress()
}

onMounted(() => loadAddress())
</script>