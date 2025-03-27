<template>
  <!-- 我的商品 -->
  <div class="section my-products">
    <div class="section-header">
      <h2>我的商品</h2>
      <!-- <el-button text @click="handleViewMore()">
          查看更多<el-icon><arrow-right /></el-icon>
        </el-button> -->
    </div>
    <div>
      <button class='newtest' @click="sellerProducts.getSellerProductsList()">
        显示我已添加的商品
      </button>
    </div>
    <div class="product-list">
      <!-- v-for 渲染每一个 myProducts数组中元素，id 每一个的id便于维护dom ， class = 样式 ，点击事件传入方法product为当前商品-->
      <div v-for="product in sellerProducts.sellerProductsList" :key="product.productId" class="product-card"
        @click="handleProductClick(product)">
        <div class="product-image">
          <img :src="product.imageUrl" :alt="product.productName">
          <div class="product-tag hot">热销</div><!-- 热销位置样式 -->
        </div>
        <div class="product-info">
          <h3>{{ product.productName }}</h3>
          <p class="desc">{{ product.description }}</p>
          <div class="price">¥{{ product.price.toFixed(2) }}</div>
          <div class="sales">月销 {{ product.stock }}+</div>
        </div>
      </div>
    </div>
  </div>

</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useRouter } from 'vue-router'
import { ArrowRight } from '@element-plus/icons-vue'
import { useSellerProucts } from '@/stores/seller_products'


const params = ref(1,1,'','seller_001')
const sellerProducts = useSellerProucts()
console.log(sellerProducts)

//sellerProducts.getSellerProductsList()
</script>

<style lang="scss" scoped>
@mixin text-ellipsis {
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
}

.section {
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

  &.flash-sale {
    .countdown {
      display: flex;
      align-items: center;
      gap: 4px;

      .time-block {
        background-color: #333;
        color: #fff;
        padding: 4px 8px;
        border-radius: 4px;
        font-size: 16px;
        font-weight: bold;
      }
    }

    .flash-sale-card {
      .progress {
        margin-top: 8px;
      }
    }
  }

  .product-list {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 20px;

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
        padding-top: 100%;

        img {
          position: absolute;
          top: 0;
          left: 0;
          width: 100%;
          height: 100%;
          object-fit: cover;
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

          &.discount {
            background-color: #e6a23c;
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

          .original {
            margin-left: 8px;
            color: #999;
            font-size: 12px;
            text-decoration: line-through;
            font-weight: normal;
          }
        }

        .sales {
          margin-top: 4px;
          font-size: 12px;
          color: #999;
        }
      }
    }
  }

  .brand-list {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 20px;

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

    .brand-card {
      background-color: #fff;
      border-radius: 8px;
      overflow: hidden;
      cursor: pointer;
      transition: transform 0.3s, box-shadow 0.3s;

      &:hover {
        transform: translateY(-4px);
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
      }

      img {
        width: 100%;
        height: 120px;
        object-fit: cover;
      }

      .brand-info {
        padding: 12px;
        text-align: center;

        h3 {
          margin: 0 0 8px;
          font-size: 16px;
        }

        p {
          margin: 0 0 8px;
          font-size: 12px;
          color: #666;
        }

        .discount {
          color: #f56c6c;
          font-size: 14px;
          font-weight: bold;
        }
      }
    }
  }

  .load-more {
    text-align: center;
    margin-top: 20px;
  }
}
</style>