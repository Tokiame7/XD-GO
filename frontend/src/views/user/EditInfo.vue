<template>
    <div class="edit-container">
        <el-form :model="form" :rules="rules" ref="formRef" label-width="100px">
            <!-- 公共字段 -->
            <el-form-item label="联系电话" prop="phone">
                <el-input v-model="form.phone" />
            </el-form-item>

            <el-form-item label="电子邮箱" prop="email">
                <el-input v-model="form.email" />
            </el-form-item>

            <!-- 买家专属字段 -->
            <el-form-item v-if="userStore.userInfo.role === 'buyer'" label="收货地址" prop="shipping_address">
                <el-input v-model="form.shipping_address" type="textarea" />
            </el-form-item>

            <el-form-item>
                <el-button type="primary" @click="submit">提交修改</el-button>
                <el-button @click="router.back()">取消</el-button>
            </el-form-item>
        </el-form>
    </div>
</template>

<script setup>
import { reactive, ref } from 'vue'
import { useUserStore } from '@/stores/user'
import { updateUserInfo } from '@/api/user'
import { ElMessage } from 'element-plus'
import { useRouter } from 'vue-router'

const userStore = useUserStore()
const router = useRouter()
const formRef = ref()

// 初始化表单数据
const form = reactive({
    phone: userStore.userInfo.phone || '',
    email: userStore.userInfo.email || '',
    shipping_address: userStore.userInfo.shipping_address || ''
})

// 验证规则
const rules = reactive({
    phone: [
        { required: true, message: '请输入联系电话', trigger: 'blur' },
        { pattern: /^1[3-9]\d{9}$/, message: '手机号格式不正确' }
    ],
    email: [
        { required: true, message: '请输入邮箱地址', trigger: 'blur' },
        { type: 'email', message: '邮箱格式不正确' }
    ],
    shipping_address: [
        { required: userStore.userInfo.role === 'buyer', message: '请输入收货地址' }
    ]
})

// 提交处理
const submit = async () => {
    try {
        await formRef.value.validate()

        const payload = {
            phone: form.phone,
            email: form.email
        }

        // 买家才需要发送地址
        if (userStore.userInfo.role === 'buyer') {
            payload.shipping_address = form.shipping_address
        }

        const res = await updateUserInfo(payload)

        if (res.code === 200) {
            // 更新本地存储
            updateUserInfo(payload)
            ElMessage.success('修改成功')
            router.push('/user')
        }
    } catch (error) {
        ElMessage.error(error.message || '修改失败')
    }
}
</script>

<style scoped>
.edit-container {
    max-width: 800px;
    margin: 20px auto;
    padding: 20px;
    background: #fff;
    border-radius: 8px;
    box-shadow: 0 2px 12px rgba(0, 0, 0, 0.1);
}
</style>
