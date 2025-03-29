<template>
  <div>
  <template v-if="loading">
    <p>数据加载中，请稍候...</p>
  </template>
  <template v-else>
    <el-table :data="OrderList" stripe style="width: 100%">
      <el-table-column prop="orderid" label="订单id" width="180" />
      <el-table-column prop="totalprice" label="总价格" width="180" />
      <el-table-column prop="status" label="status" width ='180' />
      <el-table-column prop="createtime" label="创建时间" />
      <el-table-column fixed="right" label="操作" min-width="120">
        <template #default="scope">
        <el-button
          link
          type="primary"
          size="small"
          @click.prevent="Editorder(scope.row.orderid,scope.row.status)"
        >
          发货
        </el-button>
      </template>



      </el-table-column>
    </el-table>

  </template>
  </div>
</template>
<script setup>

import { shipOrder } from '@/api/seller';
import { useGetOrder,useShiporder } from '@/stores/seller_products';
import { ref ,reactive ,watchEffect} from 'vue'
const loading = ref(true);//加载对象
const OrderList = ref([])
const GetOrder = useGetOrder()
const Shiporder = useShiporder()

//整个组件挂载后的行为
onMounted(() => {
  GetOrder.getorders();
  OrderList.value = GetOrder.orderList;
});

const Editorder = (id,status)=>{
  console.log(id,status)
  Shiporder.shipOrderstatus(id,status);
}

//监听数据变化同步数据变化
watchEffect(() => {
    console.log('orderlist 发生变化:', GetOrder.orderList);
    if (GetOrder.orderList.length > 0) {
        loading.value = false;//不要忘记加载
    }
});
  </script>