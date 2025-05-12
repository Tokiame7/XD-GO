<template>
    <div class="order-success-container">
        <div class="success-content">
            <!-- 成功提示 -->
            <div class="success-header">
                <el-icon class="success-icon">
                    <CircleCheckFilled />
                </el-icon>
                <h2 class="success-title">订单提交成功</h2>
                <p class="success-desc">感谢您的购买，我们会尽快为您发货</p>
            </div>

            <!-- 订单信息 -->
            <div class="order-info" v-if="orderInfo">
                <div class="info-item">
                    <span class="label">订单编号：</span>
                    <span class="value">{{ orderInfo.orderNo }}</span>
                    <el-button link type="primary" @click="handleCopy(orderInfo.orderNo)">复制</el-button>
                </div>
                <div class="info-item">
                    <span class="label">支付方式：</span>
                    <span class="value">{{ orderInfo.paymentMethod === 'wechat' ? '微信支付' : '支付宝' }}</span>
                </div>
                <div class="info-item">
                    <span class="label">支付金额：</span>
                    <span class="value price">¥{{ orderInfo.totalAmount }}</span>
                </div>
            </div>

            <!-- 收货信息 -->
            <div class="delivery-info" v-if="orderInfo">
                <h3>收货信息</h3>
                <div class="info-content">
                    <div class="info-row">
                        <span class="label">收货人：</span>
                        <span class="value">{{ orderInfo.address.name }}</span>
                    </div>
                    <div class="info-row">
                        <span class="label">联系电话：</span>
                        <span class="value">{{ orderInfo.address.phone }}</span>
                    </div>
                    <div class="info-row">
                        <span class="label">收货地址：</span>
                        <span class="value">{{ orderInfo.address.fullAddress }}</span>
                    </div>
                </div>
            </div>

            <!-- 操作按钮 -->
            <div class="action-buttons">
                <el-button @click="router.push('/order/index')">查看订单</el-button>
                <el-button type="primary" @click="router.push('/')">继续购物</el-button>
            </div>
        </div>
    </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useRouter, useRoute } from 'vue-router'
import { ElMessage } from 'element-plus'
import { CircleCheckFilled } from '@element-plus/icons-vue'
import { getOrderDetail } from '@/api/shop'

const router = useRouter()
const route = useRoute()

// 订单信息
const orderInfo = ref(null)

// 获取订单详情
const fetchOrderDetail = async () => {
    try {
        const orderId = route.query.orderId
        const response = await getOrderDetail(orderId)
        orderInfo.value = response.data
    } catch (error) {
        console.error('获取订单详情失败:', error)
        ElMessage.error('获取订单详情失败')
    }
}

// 页面加载时获取订单详情
onMounted(() => {
    fetchOrderDetail()
})

// 复制订单号
const handleCopy = async (text) => {
    try {
        await navigator.clipboard.writeText(text)
        ElMessage.success('复制成功')
    } catch (err) {
        ElMessage.error('复制失败，请手动复制')
    }
}
</script>

<style lang="scss" scoped>
.order-success-container {
    max-width: 800px;
    margin: 40px auto;
    padding: 0 20px;

    .success-content {
        background-color: #fff;
        border-radius: 8px;
        box-shadow: 0 2px 12px 0 rgba(0, 0, 0, 0.1);
        padding: 40px;
    }

    .success-header {
        text-align: center;
        margin-bottom: 40px;

        .success-icon {
            font-size: 56px;
            color: #67c23a;
            margin-bottom: 16px;
        }

        .success-title {
            font-size: 24px;
            color: #67c23a;
            margin: 0 0 8px;
        }

        .success-desc {
            font-size: 14px;
            color: #666;
            margin: 0;
        }
    }

    .order-info {
        background-color: #f5f7fa;
        border-radius: 4px;
        padding: 20px;
        margin-bottom: 30px;

        .info-item {
            display: flex;
            align-items: center;
            margin-bottom: 12px;

            &:last-child {
                margin-bottom: 0;
            }

            .label {
                color: #666;
                margin-right: 8px;
            }

            .value {
                color: #333;

                &.price {
                    color: #f56c6c;
                    font-size: 16px;
                    font-weight: bold;
                }
            }
        }
    }

    .delivery-info {
        margin-bottom: 40px;

        h3 {
            font-size: 16px;
            margin: 0 0 16px;
            padding-bottom: 12px;
            border-bottom: 1px solid #ebeef5;
        }

        .info-content {
            color: #666;

            .info-row {
                margin-bottom: 12px;

                &:last-child {
                    margin-bottom: 0;
                }

                .label {
                    display: inline-block;
                    width: 80px;
                }

                .value {
                    color: #333;
                }
            }
        }
    }

    .action-buttons {
        text-align: center;

        .el-button {
            min-width: 120px;
            margin: 0 10px;
        }
    }
}
</style>
