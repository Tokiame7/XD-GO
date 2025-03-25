<template>
    <div class="not-found">
        <el-empty description="页面不存在">
            <template #image>
                <el-image src="@/assets/404.png" />
            </template>
            <el-button type="primary" @click="router.push('/')">返回首页</el-button>
        </el-empty>
    </div>
</template>

<script setup>
import { useRouter } from 'vue-router'

const router = useRouter()
</script>

<style lang="scss" scoped>
.not-found {
    display: flex;
    justify-content: center;
    align-items: center;
    min-height: 500px;

    :deep(.el-empty) {
        .el-image {
            width: 300px;
            height: 300px;
        }

        .el-empty__description {
            margin-top: 20px;
            font-size: 20px;
            color: #666;
        }

        .el-button {
            margin-top: 20px;
        }
    }
}
</style>
