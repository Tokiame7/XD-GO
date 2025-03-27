<template>
  <div>
    <!-- 顶部按钮 -->
    <div class="button-container">
      <button @click="showAddModal = true" class="add-product-button">添加商品</button>
    </div>
    <!-- 商品列表 -->
    <table>
      <thead>
        <tr>
          <th><input type="checkbox" v-model="selectAll" @change="toggleSelectAll" /></th>
          <th>商品名称</th>
          <th>价格</th>
          <th>库存</th>
          <th>操作</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="product in sellerProducts.sellerProductsList" :key="product.productId">
          <td><input type="checkbox" v-model="selectedProducts" :value="product" /></td>
          <td>
            <template v-if="product.isEditing">
              <input v-model="product.productName" placeholder="商品名称" />
            </template>
            <template v-else>
              {{ product.productName }}
            </template>
          </td>
          <td>
            <template v-if="product.isEditing">
              <input v-model="product.price" placeholder="价格" type="number" />
            </template>
            <template v-else>
              {{ product.price }}
            </template>
          </td>
          <td>
            <template v-if="product.isEditing">
              <input v-model="product.stock" placeholder="库存" type="number" />
            </template>
            <template v-else>
              {{ product.stock }}
            </template>
          </td>
          <td>
            <template v-if="product.isEditing">
              <button @click="saveProduct(product.productId)">保存</button>
              <button @click="cancelEdit(product.productId)">取消</button>
            </template>
            <template v-else>
              <button @click="editProduct(product.productId)">编辑</button>
              <button @click="deleteProduct(product.productId)">删除</button>
            </template>
          </td>
        </tr>
      </tbody>
    </table>
    <!-- 添加商品模态框 -->
    <!-- 弹出添加商品 -->
    <el-dialog v-model="showAddModal" title="编辑商品" width="80%">
      <el-form :model="form">
        <el-form-item label="商品名称">
          <el-input v-model="form.name" autocomplete="off" />
        </el-form-item>
        <el-form-item label="商品价格">
          <el-input v-model="form.price" autocomplete="off" />
        </el-form-item>
        <el-form-item label="商品库存">
          <el-input v-model="form.stock" autocomplete="off" />
        </el-form-item>
      </el-form>
      <template #footer>
        <div class="dialog-footer">
          <el-button @click="showAddModal = false">取消</el-button>
          <el-button type="primary" @click="handleConfirm()">
            保存
          </el-button>
        </div>
      </template>
    </el-dialog>
  </div>
</template>

<script setup>
import { ref, reactive, onMounted } from 'vue';
import { useSellerProucts } from '@/stores/seller_products';
import { update } from 'lodash-es';
import seller from '@/router/modules/seller';

const params = ref({
  page: 1,
  pageSize: 10,
  search: '',
  sellerid: 'seller_001'
});
// 定义响应式数据
const selectedProducts = ref([]);
const selectAll = ref(false);
const sellerProducts = useSellerProucts(); // 先创建实例

onMounted(() => {
  sellerProducts.getSellerProductsList().then(() => {
    // 为每个商品对象添加 isEditing 属性
    sellerProducts.sellerProductsList.forEach(product => {
      product.isEditing = false;
    });
  });
});

// 在编辑页面上 商品列表的组成 = 原本数据库 + 是否被编辑对象 
const New_Edit_ProductList = ref([]);
const newProduct = ref({
  proid: '',
  name: '',
  price: '',
  stock: '',
  description: '',
  catid: '',
  userid: '',
  image: '',
  createtime: '',
  updatetime: ''
});

// 表单区域
const showAddModal = ref(false);
const form = reactive({
  name: '',
  price: '',
  stock: ''
});

const handleConfirm = () => {
  console.log('提交form:', form);
  // 这里可以调用保存表单数据的接口
};

// 切换全选状态
const toggleSelectAll = () => {
  if (selectAll.value) {
    selectedProducts.value = [...sellerProducts.sellerProductsList];
  } else {
    selectedProducts.value = [];
  }
};

// 编辑商品
const editProduct = (productId) => {
  const product = sellerProducts.sellerProductsList.find(p => p.productId === productId);
  if (product) {
    product.isEditing = true;
  }
};

// 保存商品修改
const saveProduct = (productId) => {
  const product = sellerProducts.sellerProductsList.find(p => p.productId === productId);
  if (product) {
    product.isEditing = false;
    // 发送数据到后端时移除 isEditing 属性
    const productToSend = { ...product };
    delete productToSend.isEditing;
    // 这里可以调用保存商品修改的接口
    console.log('发送到后端的数据:', productToSend);
  }
};

// 取消编辑
const cancelEdit = (productId) => {
  const product = sellerProducts.sellerProductsList.find(p => p.productId === productId);
  if (product) {
    product.isEditing = false;
  }
};

// 删除商品
const deleteProduct = (productId) => {
  const index = sellerProducts.sellerProductsList.findIndex(p => p.productId === productId);
  if (index !== -1) {
    sellerProducts.sellerProductsList.splice(index, 1);
  }
};

// 添加商品
const addProduct = () => {
  New_Edit_ProductList.value.push({ ...newProduct.value, isEditing: false });
  newProduct.value = { name: '', price: 0, stock: 0 };
  showAddModal.value = false;
};
</script>

<style scoped>
.button-container {
  margin-bottom: 2px;
}

table {
  width: 100%;
  border-collapse: collapse;
}

th,
td {
  border: 1px solid #ccc;
  padding: 8px;
  text-align: center;
}

.modal {
  display: fixed;
  z-index: 1;
  left: 0;
  top: 0;
  width: 100%;
  height: 100%;
  overflow: auto;
  background-color: rgba(0, 0, 0, 0.4);
}

.modal-content {
  background-color: #fefefe;
  margin: 15% auto;
  padding: 20px;
  border: 1px solid #888;
  width: 80%;
}

.close {
  color: #aaa;
  float: right;
  font-size: 28px;
  font-weight: bold;
}

.close:hover,
.close:focus {
  color: black;
  text-decoration: none;
  cursor: pointer;
}

.add-product-button {
  background-color: #003366;
  color: white;
  border: none;
  padding: 10px 20px;
  cursor: pointer;
  border-radius: 4px;
}

.add-product-button:active {
  background-color: #336699;
}
</style>