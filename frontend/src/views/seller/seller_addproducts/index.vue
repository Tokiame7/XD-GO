<template>
  <div>
    <!-- 商品列表 -->
    <template v-if="loading">
      <p>数据加载中，请稍候...</p>
    </template>
    <template v-else>
    <el-table :data="products" style="width: 100%" max-height="250">
    <el-table-column fixed prop="productName" label="商品名" width="150" />
    <el-table-column prop="productId" label="id" width="120" />
    <el-table-column prop="price" label="价格" width="80" />
    <el-table-column prop="stock" label="销量" width="80" />
    <el-table-column prop="category" label="分类" width="120" />
    <el-table-column prop="description" label="描述" width="350" />
    <el-table-column prop="createTime" label="创建时间" width="120" />
    <el-table-column prop="updateTime" label="更新时间" width="120" />
    <el-table-column prop="imageUrl" label="图片URL" width="300" />
    <el-table-column prop="sellerId" label="所属用户" width="120" />
    <el-table-column prop="catid" label="分类id" width="120" />
    <el-table-column fixed="right" label="Operations" min-width="120">
      <template #default="scope">
        <el-button
          link
          type="primary"
          size="small"
          @click.prevent="delepro(scope.row.productId)"
        >
          Remove
        </el-button>
        <el-button
          link
          type="primary"
          size="small"
          @click.prevent=""
        >
          Edit
        </el-button>
      </template>
     </el-table-column>
     </el-table>
      <el-button class="mt-4" style="width: 100%" @click="dialogVisible = true">
        Add Item
      </el-button>
      </template>
    <!-- 添加商品模态框 -->
    <!-- 弹出添加商品 -->
    <el-dialog v-model="dialogVisible" :modal="false">
      <!-- 模态框主内容 -->
    <el-form :model="form" label-width="auto" style="max-width: 600px">
      <!-- 第一个框 -->
    <el-form-item label="商品名称*">
      <el-input v-model="form.name" />
    </el-form-item>
    <el-form-item label="描述">
      <el-input v-model="form.description" />
    </el-form-item>
    <el-form-item label="价格*(>0)">
      <el-input v-model.number="form.price" />
    </el-form-item>
    <el-form-item label="库存*(>0)">
      <el-input v-model.number="form.stock" />
    </el-form-item>
    <el-form-item label="图片url">
      <el-input v-model="form.image" />
    </el-form-item>
    <el-form-item label="catid*">
      <el-input v-model="form.catid" />
      <text>cat_clothing、</text>
      <text>cat_electronics</text>
    </el-form-item>
     <!-- 选项框 -->
    <!-- <el-form-item label="商品分类*">
      <el-checkbox-group v-model="form.type">
        <el-checkbox value="Online activities" name="type">
          Clothing
        </el-checkbox>
        <el-checkbox value="Promotion activities" name="type">
          Electronics
        </el-checkbox>
      </el-checkbox-group>
    </el-form-item> -->
<!-- 多内容框 /文件框-->
    <el-form-item label="其他">
      <el-input v-model="form.desc" type="textarea" />
    </el-form-item>

    <el-form-item>
      <el-button type="primary" @click="onSubmit">创建商品</el-button>
      <el-button @click="resetForm">清除内容</el-button>
    </el-form-item>

  </el-form>
    <!-- 底部按键 -->
    <template #footer>
      <div class="dialog-footer">
        <el-button @click="dialogVisible = false">取消</el-button>
        <el-button type="primary" @click="dialogVisible = false">
          确认
        </el-button>
      </div>
    </template>
  </el-dialog>
  </div>
</template>

<script setup>
import { ref, reactive, onMounted , watchEffect } from 'vue';
import { useSellerProucts,useDeleteProduct,useAddProduct } from '@/stores/seller_products';

const params = ref({
  page: 1,
  pageSize: 10,
  search: '',
  sellerid: 'seller_001'
});

// 先创建实例
const sellerProducts = useSellerProucts(); 
const addproduct = useAddProduct();
const deleproduct = useDeleteProduct();

const loading = ref(true);//加载对象
const products = ref([])//当前响应式对象
const dialogVisible = ref(false)//模态框状态
//初始化的空表单
const initialform = {
  name: '',
  productId: '',
  description: '',
  price: 0,
  stock: 0,
  createTime: '',
  updateTime: '',
  category: '',
  image:'',
  catid:'',
  sellerId:''
}
//初始化响应
const form = reactive({...initialform});

//提交表单
const onSubmit = () => {
  //此处实现提交后端
 addproduct.createProducts(form)
  console.log('submit!',form)
  //提交后把表单重置
  resetForm();
}

//重置表单函数
const resetForm = () => {
  // 使用 Object.assign 重置表单数据
  Object.assign(form, initialform);
};

//整个组件挂载后的行为
onMounted(() => {
  sellerProducts.getSellerProductsList();
});

//监听数据变化同步数据变化 立即执行一次
watchEffect(() => {
    console.log('sellerProductsList 发生变化:', sellerProducts.sellerProductsList);
    if (sellerProducts.sellerProductsList.length > 0) {
        products.value = sellerProducts.sellerProductsList;
        loading.value = false;//不要忘记加载
    }
});

//删除商品
const delepro = (proid)=>{
  deleproduct.DeleteProduct(proid);
}
</script>

<style scoped>
</style>