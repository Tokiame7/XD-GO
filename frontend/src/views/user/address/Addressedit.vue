<template>
    <div class="address-form">
        <el-form :model="form" label-width="80px">
            <el-form-item label="收货人">
                <el-input v-model="form.name" />
            </el-form-item>
            <el-form-item label="联系电话">
                <el-input v-model="form.phone" />
            </el-form-item>
            <el-form-item label="详细地址">
                <el-input v-model="form.detail" type="textarea" />
            </el-form-item>
            <el-form-item>
                <el-button type="primary" @click="submit">提交</el-button>
            </el-form-item>
        </el-form>
    </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import { getAddressDetail, addAddress, updateAddress } from '@/api/user'

const route = useRoute()
const router = useRouter()
const isEdit = ref(false)

const form = ref({
    name: '',
    phone: '',
    detail: ''
})

// 提交处理
const submit = async () => {
    if (isEdit.value) {
        await updateAddress(route.params.id, form.value)
    } else {
        await addAddress(form.value)
    }
    router.push('/address')
}

// 初始化数据
onMounted(async () => {
    if (route.params.id) {
        const res = await getAddressDetail(route.params.id)
        form.value = res.data
        isEdit.value = true
    }
})
</script>