<template>
  <!-- 我的商品 -->
  <div class="section my-products">
    <div class="section-header">
      <h2>MyProducts</h2>
    </div>
    <div class="product-list">
      <!-- v-for 渲染每一个 myProducts数组中元素，id 每一个的id便于维护dom ， class = 样式 ，点击事件传入方法product为当前商品-->
      <div v-for="product in sellerProducts.sellerProductsList" :key="product.productId" class="product-card"
        @click="handleProductClick(product.productId)">
        <div class="product-image">
          <img :src="product.imageUrl" :alt="product.productName">
          <div class="product-tag hot">HOT</div><!-- 热销位置样式 -->
        </div>
        <div class="product-info">
          <h3>{{ product.productName }}</h3>
          <p class="desc">{{ product.description }}</p>
          <div class="price">¥{{ product.price.toFixed(2) }}</div>
          <div class="sales">MonthStock {{ product.stock }}+</div>
        </div>
      </div>
    </div>
  </div>
  <el-dialog
    v-model="centerDialogVisible"
    width="500"
    align-center
  >
    <!-- 可以在这里添加展示商品详情的部分 -->
    <div v-if="getsellerproductDetail.sellerProductDetail">
      <h2>ProductsDetail</h2>
      <p>{{ getsellerproductDetail.sellerProductDetail.detail.goods_name }}</p>
      <p>Price: ¥{{ getsellerproductDetail.sellerProductDetail.detail.price }}</p>
      <!-- 其他详情信息 -->
      </div>
    <template #footer>
      <div class="dialog-footer">
        <el-button type="primary" @click="centerDialogVisible = false">
          OK
        </el-button>
      </div>
    </template>
  </el-dialog>
</template>

<script setup>
import { ref, onMounted,watch } from 'vue'
import { useSellerProucts ,useGetproductDetail} from '@/stores/seller_products'


//pinia打包 创建实例方法
const sellerProducts = useSellerProucts()
const getsellerproductDetail = useGetproductDetail();//数据体（detail）返回的是getsellerproductDetail.detail
const centerDialogVisible = ref(false)
//onM...组件挂载后紧跟的操作
onMounted(()=>{
  sellerProducts.getSellerProductsList()
})

//当商品变化时立即执行一次获取商品
watch(sellerProducts.sellerProductsList,()=>{
  sellerProducts.getSellerProductsList()
},
{immediate:true}
)

//点击图片获得卖家商品详细数据 传入当前商品id
const handleProductClick = (id) =>{
  getsellerproductDetail.getSellerProductDetail(id);
  centerDialogVisible.value = true;
}

</script>

<style lang="scss" scoped>
@mixin text-ellipsis {
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
}

.section {
  //display: flex;
  margin-bottom: 40px;

  @media (max-width: 768px) {
    margin-bottom: 20px;
  }

  .section-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 20px;

    h2 {
      margin: 0;
      font-size: 24px;
    }
  }

  .product-list {
    display: grid;

    grid-template-columns: repeat(5, 1fr);
    gap: 20px;


    @media (max-width: 2048px) {
      grid-template-columns: repeat(4, 1fr);
      gap: 15px;
    }

    @media (max-width: 1024px) {
      grid-template-columns: repeat(3, 1fr);
      gap: 15px;
    }

    @media (max-width: 768px) {
      grid-template-columns: repeat(2, 1fr);
      gap: 10px;
    }

    @media (max-width: 480px) {
      grid-template-columns: repeat(1, 1fr);
    }

    .product-card {
      background-color: #fff;
      border-radius: 8px;
      overflow: hidden;
      cursor: pointer;
      transition: transform 0.3s, box-shadow 0.3s;

      &:hover {
        transform: translateY(-4px);
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
      }

      .product-image {
        position: relative;
        padding-top: 100%; // 关键：保持宽高比
        width: 100%; // 确保填满父容器

        img {
          position: absolute;
          top: 0;
          left: 0;
          width: 100%;
          height: 100%;
          object-fit: cover; // 裁剪图片以填充容器
        }

        .product-tag {
          position: absolute;
          top: 12px;
          right: 12px;
          padding: 4px 8px;
          border-radius: 4px;
          color: #fff;
          font-size: 12px;

          &.hot {
            background-color: #f56c6c;
          }
        }
      }

      .product-info {
        padding: 12px;

        h3 {
          margin: 0 0 8px;
          font-size: 14px;
          @include text-ellipsis;
        }

        .desc {
          margin: 0 0 8px;
          font-size: 12px;
          color: #999;
          @include text-ellipsis;
        }

        .price {
          color: #f56c6c;
          font-size: 16px;
          font-weight: bold;
        }

        .sales {
          margin-top: 4px;
          font-size: 12px;
          color: #999;
        }
      }
    }
  }
}
</style>