<template>
<template v-if="loading">
    <p>数据加载中，请稍候...</p>
  </template>
<template v-else>
    <el-table :data="OrderList" stripe style="width: 100%">
      <el-table-column prop="orderid" label="订单id" width="180" />
      <el-table-column prop="totalPrice" label="订单名" width="180" />
      <el-table-column prop="status" label="status" />
      <el-table-column prop="createtime" label="创建时间" />
      <el-table-column prop="orderItems" label="订单详细" />
    </el-table>
  </template>
</template>
  <script setup>

import { useGetOrder } from '@/stores/seller_products';
import { ref ,reactive ,watchEffect} from 'vue'
const loading = ref(true);//加载对象
const OrderList = ref([])
const GetOrder = useGetOrder()
//整个组件挂载后的行为
onMounted(() => {
  GetOrder.getorders();
  OrderList.value = GetOrder.orderList;
});
//监听数据变化同步数据变化
watchEffect(() => {
    console.log('orderlist 发生变化:', GetOrder.orderList);
    if (GetOrder.orderList.length > 0) {
        tableData.value = GetOrder.orderList;
        loading.value = false;//不要忘记加载
    }
});
  </script>