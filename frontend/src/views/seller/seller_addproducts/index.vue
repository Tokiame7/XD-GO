<template>
  <div>
    <!-- 商品列表 -->
    <div v-if="loading">
      <p>Pageloading,waiting...</p>
    </div>
    <div v-else>
      <el-table :data="products" style="width: 100%" max-height="1000">
        <el-table-column fixed prop="productName" label="Product'name" width="150" />
        <el-table-column prop="productId" label="id" width="120" />
        <el-table-column prop="price" label="Price" width="80" />
        <el-table-column prop="stock" label="Stock" width="80" />
        <el-table-column prop="category" label="Category" width="120" />
        <el-table-column prop="description" label="Description" width="350" />
        <el-table-column prop="createTime" label="CreateTime" width="120" />
        <el-table-column prop="updateTime" label="UpdateTime" width="120" />
        <el-table-column prop="imageUrl" label="ImageUrl" width="300" />
        <el-table-column prop="sellerId" label="Owner" width="120" />
        <el-table-column prop="catid" label="Categoryid" width="120" />
        <el-table-column fixed="right" label="Operations" min-width="120">
          <template #default="scope">
            <el-button link type="primary" size="small" @click.prevent="delepro(scope.row.productId)">
              Remove
            </el-button>
            <el-button link type="primary" size="small" @click="updatePro(scope.row)">
              Edit
            </el-button>
          </template>
        </el-table-column>
      </el-table>
    </div>
    <el-button class="mt-4" style="width: 100%" @click="dialogVisible = true">
      Add Item
    </el-button>
    <!-- 添加商品模态框 -->
    <!-- 弹出添加商品 -->
    <el-dialog v-model="dialogVisible" :modal="false">
      <!-- 模态框主内容 -->
      <el-form :model="form" label-width="auto" style="max-width: 600px">
        <!-- 第一个框 -->
        <el-form-item label="ProductName*">
          <el-input v-model="form.name" />
        </el-form-item>
        <el-form-item label="Description">
          <el-input v-model="form.description" />
        </el-form-item>
        <el-form-item label="Price*(>0)">
          <el-input v-model.number="form.price" />
        </el-form-item>
        <el-form-item label="Stock*(>0)">
          <el-input v-model.number="form.stock" />
        </el-form-item>
        <el-form-item label="Imageurl">
          <el-input v-model="form.image" />
        </el-form-item>
        <el-form-item label="catid*">
          <el-input v-model="form.catid" />
          <div>Can Choose:</div>
          <div v-for="cat in catId" :key="cat.categoryId" class="Catids">
            <div>
              {{ cat.categoryId }}、
            </div>
          </div>
        </el-form-item>
        <!-- 多内容框 /文件框-->
        <el-form-item label="Other">
          <el-input v-model="form.desc" type="textarea" />
        </el-form-item>

        <el-form-item>
          <el-button type="primary" @click="onSubmit">Create</el-button>
          <el-button @click="resetForm">Delete</el-button>
        </el-form-item>

      </el-form>
      <!-- 底部按键 -->
      <template #footer>
        <div class="dialog-footer">
          <el-button @click="dialogVisible = false">esc</el-button>
          <el-button type="primary" @click="dialogVisible = false">
            confirm
          </el-button>
        </div>
      </template>
    </el-dialog>
    <el-dialog v-model="dialogVisible_2" :modal="false">
      <!-- 模态框主内容 -->
      <el-form :model="upform" label-width="auto" style="max-width: 600px">
        <!-- 第一个框 -->
        <el-form-item label="ProductName">
          <el-input v-model="upform.productName" />
        </el-form-item>
        <el-form-item label="Description">
          <el-input v-model="upform.description" />
        </el-form-item>
        <el-form-item label="Price(>0)">
          <el-input v-model.number="upform.price" />
        </el-form-item>
        <el-form-item label="Stock(>0)">
          <el-input v-model.number="upform.stock" />
        </el-form-item>
        <el-form-item label="Imageurl">
          <el-input v-model="upform.imageUrl" />
        </el-form-item>
        <!-- 多内容框 /文件框-->
        <el-form-item label="Other">
          <el-input v-model="form.desc" type="textarea" />
        </el-form-item>

        <el-form-item>
          <el-button type="primary" @click="onSubmitUpdate">OK</el-button>
        </el-form-item>

      </el-form>
      <!-- 底部按键 -->
      <template #footer>
        <div class="dialog-footer">
          <el-button @click="dialogVisible_2 = false">esc</el-button>
          <el-button type="primary" @click="dialogVisible_2 = false">
            confirm
          </el-button>
        </div>
      </template>
    </el-dialog>
  </div>
</template>

<script setup>
<<<<<<< HEAD
console.log('nihao');

import { ref, reactive, onMounted, watch } from 'vue';
import { useSellerProucts, useDeleteProduct, useAddProduct, useGetshopCatid, useUpdateProduct } from '@/stores/seller_products';

=======
import { ref, reactive, onMounted , watchEffect } from 'vue';
import { useSellerProucts,useDeleteProduct,useAddProduct,useGetshopCatid, useUpdateProduct } from '@/stores/seller_products';
>>>>>>> ee05095d67472dd70aacbb705bd9fe5c4d334ee9

// 先创建实例
const sellerProducts = useSellerProucts();
const addproduct = useAddProduct();
const deleproduct = useDeleteProduct();
const getshopCatid = useGetshopCatid();
const updateproduct = useUpdateProduct();
const loading = ref(true);//加载对象
const products = ref([])//当前响应式对象
const dialogVisible = ref(false)//模态框状态
const dialogVisible_2 = ref(false)
const catId = ref([])//所有catid
//初始化的空表单 增加商品栏
const initialform = {
  name: '',
  productId: '',
  description: '',
  price: 0,
  stock: 0,
  createTime: '',
  updateTime: '',
  category: '',
  image: '',
  catid: '',
  sellerId: ''
}
//初始化响应
const form = reactive({ ...initialform });
const upform = reactive({});
//提交表单
const onSubmit = () => {
  //此处实现提交后端
  addproduct.createProducts(form)
  console.log('submit!', form)
  //提交后把表单重置
  resetForm();
}

const onSubmitUpdate = () => {
  updateproduct.upDateproduct(upform);
  console.log('商品更新成功', upform);
}
//重置表单函数
const resetForm = () => {
  // 使用 Object.assign 重置表单数据
  Object.assign(form, initialform);
};

//覆盖将要提交的更新表格
const updatePro = (uppro) => {
  Object.assign(upform, uppro);
  dialogVisible_2.value = true;
};

//删除商品
const delepro = (proid) => {
  deleproduct.DeleteProduct(proid);
}

//整个组件挂载后的行为
onMounted(() => {
  sellerProducts.getSellerProductsList();
  getshopCatid.getcatid();
  products.value = sellerProducts.sellerProductsList;
  catId.value = getshopCatid.catidList;
  loading.value = false
});
//监听数据变化同步数据变化 立即执行一次
watch(() => sellerProducts.sellerProductsList, (val) => {
  products.value = val
  loading.value = false
}, { immediate: true })

watch(() => getshopCatid.catidList, (val) => {
  catId.value = val
}, { immediate: true })

</script>

<style scoped></style>