
<template>
    <div class="payment">
        <div class="payment-header">
            <h2>订单支付</h2>
        </div>

        <!-- 订单信息 -->
        <div class="order-section">
            <div class="order-info">
                <div class="info-item">
                    <span class="label">订单编号：</span>
                    <span class="value">{{ paymentInfo.orderNo }}</span>
                </div>
                <div class="info-item">
                    <span class="label">支付金额：</span>
                    <span class="value price">¥{{ paymentInfo.amount?.toFixed(2) }}</span>
                </div>
            </div>
        </div>

        <!-- 支付方式 -->
        <div class="payment-methods">
            <h3>选择支付方式</h3>
            <div class="methods-list">
                <div v-for="method in paymentMethods" :key="method.id" class="method-item"
                    :class="{ active: selectedMethod?.id === method.id }" @click="handleSelectMethod(method)">
                    <img :src="method.icon" :alt="method.name">
                    <span class="name">{{ method.name }}</span>
                </div>
            </div>
        </div>

        <!-- 支付按钮 -->
        <div class="payment-action">
            <div class="amount">
                <span>需支付：</span>
                <span class="price">¥{{ paymentInfo.amount?.toFixed(2) }}</span>
            </div>
            <el-button type="primary" :loading="paying" :disabled="!selectedMethod" @click="handlePay">
                立即支付
            </el-button>
        </div>

        <!-- 支付状态轮询 -->
        <el-dialog v-model="showPaymentStatus" :title="paymentStatusTitle" :close-on-click-modal="false"
            :close-on-press-escape="false" :show-close="false" width="360px">
            <div class="payment-status">
                <el-icon class="status-icon" :class="paymentStatus">
                    <Loading v-if="paymentStatus === 'pending'" />
                    <CircleCheckFilled v-else-if="paymentStatus === 'success'" />
                    <CircleCloseFilled v-else />
                </el-icon>
                <p class="status-text">{{ paymentStatusText }}</p>
            </div>
            <template #footer>
                <span class="dialog-footer">
                    <el-button v-if="paymentStatus === 'success'" type="primary" @click="handleViewOrder">
                        查看订单
                    </el-button>
                    <el-button v-else-if="paymentStatus === 'failed'" @click="handleRetry">
                        重新支付
                    </el-button>
                </span>
            </template>
        </el-dialog>
    </div>
</template>

<script setup>
import { ref, computed, onMounted, onBeforeUnmount } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import { ElMessage } from 'element-plus'
import { Loading, CircleCheckFilled, CircleCloseFilled } from '@element-plus/icons-vue'
import {
    getPaymentInfo,
    getPaymentMethods,
    createPayment,
    queryPaymentStatus
} from '@/api/shop'

const route = useRoute()
const router = useRouter()

// 支付信息
const paymentInfo = ref({})
const fetchPaymentInfo = async () => {
    try {
        const orderId = route.query.orderId
        if (!orderId) {
            ElMessage.error('订单信息有误')
            router.push('/')
            return
        }
        const res = await getPaymentInfo(orderId)
        paymentInfo.value = res.data
    } catch (error) {
        console.error('获取支付信息失败:', error)
        ElMessage.error('获取支付信息失败')
    }
}

// 支付方式
const paymentMethods = ref([])
const selectedMethod = ref(null)
const fetchPaymentMethods = async () => {
    try {
        const res = await getPaymentMethods()
        paymentMethods.value = res.data
    } catch (error) {
        console.error('获取支付方式失败:', error)
        ElMessage.error('获取支付方式失败')
    }
}

const handleSelectMethod = (method) => {
    selectedMethod.value = method
}

// 支付处理
const paying = ref(false)
const handlePay = async () => {
    if (!selectedMethod.value) {
        ElMessage.warning('请选择支付方式')
        return
    }

    try {
        paying.value = true
        const res = await createPayment({
            orderId: route.query.orderId,
            methodId: selectedMethod.value.id
        })
        // 开始轮询支付状态
        startPaymentStatusPolling(res.data.paymentId)
    } catch (error) {
        console.error('创建支付订单失败:', error)
        ElMessage.error('创建支付订单失败')
        paying.value = false
    }
}

// 支付状态轮询
const showPaymentStatus = ref(false)
const paymentStatus = ref('pending') // pending, success, failed
const statusPollingTimer = ref(null)

const paymentStatusTitle = computed(() => {
    const titles = {
        pending: '支付处理中',
        success: '支付成功',
        failed: '支付失败'
    }
    return titles[paymentStatus.value]
})

const paymentStatusText = computed(() => {
    const texts = {
        pending: '正在处理您的支付，请稍候...',
        success: '您的订单已支付成功！',
        failed: '支付失败，请重试'
    }
    return texts[paymentStatus.value]
})

const startPaymentStatusPolling = (paymentId) => {
    showPaymentStatus.value = true
    paymentStatus.value = 'pending'

    const pollStatus = async () => {
        try {
            const res = await queryPaymentStatus(paymentId)
            if (res.data.status === 'success') {
                paymentStatus.value = 'success'
                clearStatusPolling()
            } else if (res.data.status === 'failed') {
                paymentStatus.value = 'failed'
                clearStatusPolling()
            }
        } catch (error) {
            console.error('查询支付状态失败:', error)
            paymentStatus.value = 'failed'
            clearStatusPolling()
        }
    }

    // 每3秒查询一次，最多轮询10分钟
    statusPollingTimer.value = setInterval(pollStatus, 3000)
    setTimeout(() => {
        if (paymentStatus.value === 'pending') {
            paymentStatus.value = 'failed'
            clearStatusPolling()
        }
    }, 10 * 60 * 1000)
}

const clearStatusPolling = () => {
    if (statusPollingTimer.value) {
        clearInterval(statusPollingTimer.value)
        statusPollingTimer.value = null
    }
    paying.value = false
}

// 支付成功后查看订单
const handleViewOrder = () => {
    router.push({
        path: '/order',
        query: { orderId: route.query.orderId }
    })
}

// 支付失败后重试
const handleRetry = () => {
    showPaymentStatus.value = false
    paymentStatus.value = 'pending'
}

// 初始化
onMounted(() => {
    fetchPaymentInfo()
    fetchPaymentMethods()
})

// 组件销毁前清理定时器
onBeforeUnmount(() => {
    clearStatusPolling()
})
</script>

<style lang="scss" scoped>
.payment {
    background-color: #fff;
    border-radius: 4px;
    padding: 20px;

    .payment-header {
        margin-bottom: 20px;

        h2 {
            margin: 0;
            font-size: 20px;
        }
    }

    .order-section {
        margin-bottom: 30px;
        padding: 20px;
        background-color: #f5f7fa;
        border-radius: 4px;

        .order-info {
            .info-item {
                display: flex;
                align-items: center;
                margin-bottom: 12px;

                &:last-child {
                    margin-bottom: 0;
                }

                .label {
                    color: #666;
                    margin-right: 12px;
                }

                .value {
                    &.price {
                        color: #f56c6c;
                        font-size: 20px;
                        font-weight: bold;
                    }
                }
            }
        }
    }

    .payment-methods {
        margin-bottom: 30px;

        h3 {
            margin: 0 0 16px;
            font-size: 16px;
        }

        .methods-list {
            display: grid;
            grid-template-columns: repeat(4, 1fr);
            gap: 16px;

            .method-item {
                border: 1px solid #dcdfe6;
                border-radius: 4px;
                padding: 20px;
                text-align: center;
                cursor: pointer;
                transition: all 0.3s;

                &:hover {
                    border-color: #409eff;
                }

                &.active {
                    border-color: #409eff;
                    background-color: #ecf5ff;
                }

                img {
                    width: 40px;
                    height: 40px;
                    margin-bottom: 8px;
                }

                .name {
                    display: block;
                    font-size: 14px;
                }
            }
        }
    }

    .payment-action {
        display: flex;
        justify-content: flex-end;
        align-items: center;
        padding: 20px;
        background-color: #f5f7fa;
        border-radius: 4px;

        .amount {
            margin-right: 20px;
            font-size: 16px;

            .price {
                color: #f56c6c;
                font-size: 24px;
                font-weight: bold;
            }
        }

        .el-button {
            width: 140px;
        }
    }
}

.payment-status {
    text-align: center;
    padding: 20px 0;

    .status-icon {
        font-size: 48px;
        margin-bottom: 16px;

        &.pending {
            color: #409eff;
            animation: rotating 2s linear infinite;
        }

        &.success {
            color: #67c23a;
        }

        &.failed {
            color: #f56c6c;
        }
    }

    .status-text {
        margin: 0;
        font-size: 16px;
        color: #666;
    }
}

@keyframes rotating {
    from {
        transform: rotate(0deg);
    }

    to {
        transform: rotate(360deg);
    }
}

:deep(.el-dialog__header) {
    text-align: center;
    margin-right: 0;
}

:deep(.el-dialog__footer) {
    text-align: center;
    padding-top: 0;
}
</style>
