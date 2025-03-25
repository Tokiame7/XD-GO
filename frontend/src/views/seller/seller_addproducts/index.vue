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
        <tr v-for="(product, index) in products" :key="index">
          <td><input type="checkbox" v-model="selectedProducts" :value="product" /></td>
          <td>
            <template v-if="product.isEditing">
              <input v-model="product.name" placeholder="商品名称" />
            </template>
            <template v-else>
              {{ product.name }}
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
              <button @click="saveProduct(index)">保存</button>
              <button @click="cancelEdit(index)">取消</button>
            </template>
            <template v-else>
              <button @click="editProduct(index)">编辑</button>
              <button @click="deleteProduct(index)">删除</button>
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
          <el-button type="primary" @click="handleConfirm">
            保存
          </el-button>
        </div>
      </template>
    </el-dialog>
  </div>
</template>

<script setup>
import { ref, reactive } from 'vue';
// 定义响应式数据
const products = ref([]);//定义空列表
const selectedProducts = ref([]);
const selectAll = ref(false);
const newProduct = ref({ name: '', price: 0, stock: 0 });

// 表单区域
const showAddModal = ref(false);
const form = reactive({
  name: '',
  price: '',
  stock: ''
})
const handleConfirm = () => {
  console.log('提交form:', form);

}

// // 获取商品数据
// const fetchProducts = async () => {
//   try {
//     const response = await axios.get('/api/products');
//     products.value = response.data;
//   } catch (error) {
//     console.error('获取商品数据失败:', error);
//   }
// };

// // 保存商品数据
// const saveProducts = async () => {
//   try {
//     await axios.post('/api/products', products.value);
//   } catch (error) {
//     console.error('保存商品数据失败:', error);
//   }
// };




// 切换全选状态
const toggleSelectAll = () => {
  if (selectAll.value) {
    selectedProducts.value = [...products.value];
  } else {
    selectedProducts.value = [];
  }
};

// 编辑商品
const editProduct = (index) => {
  products.value[index].isEditing = true;
};

// 保存商品修改
const saveProduct = (index) => {
  products.value[index].isEditing = false;
};

// 取消编辑
const cancelEdit = (index) => {
  // 恢复原始值（这里可以根据需求实现更复杂的逻辑，比如备份原始值）
  products.value[index].isEditing = false;
};

// 删除商品
const deleteProduct = (index) => {
  products.value.splice(index, 1);
};

// 添加商品
const addProduct = () => {
  products.value.push({ ...newProduct.value, isEditing: false });
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