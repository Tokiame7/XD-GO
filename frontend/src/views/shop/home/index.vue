<template>
  <div class="home">
    <!-- 分类导航和轮播图区域 -->
    <div class="banner-section">
      <!-- 分类导航 -->
      <div class="category-nav">
        <ul class="category-list">
          <li v-for="category in categories" :key="category.id" class="category-item"
            @mouseenter="handleCategoryEnter(category)" @mouseleave="handleCategoryLeave">
            <div class="category-title">
              <i :class="category.icon"></i>
              <span>{{ category.name }}</span>
            </div>
            <!-- 二级分类 -->
            <div class="sub-categories" v-show="currentCategory?.id === category.id">
              <dl v-for="sub in category.children" :key="sub.id">
                <dt>{{ sub.name }}</dt>
                <dd>
                  <a v-for="item in sub.children" :key="item.id" @click="handleCategoryClick(item)">
                    {{ item.name }}
                  </a>
                </dd>
              </dl>
            </div>
          </li>
        </ul>
      </div>

      <!-- 轮播图 -->
      <div class="banner-carousel">
        <el-carousel height="400px" :interval="3000" :autoplay="true" indicator-position="outside" :initial-index="0"
          :loop="true" :pause-on-hover="true">
          <el-carousel-item v-for="banner in banners" :key="banner.id">
            <img :src="banner.image" :alt="banner.title" />
          </el-carousel-item>
        </el-carousel>
      </div>
    </div>

    <!-- 热销商品 -->
    <div class="section hot-products">
      <div class="section-header">
        <h2>热销商品</h2>
        <el-button text @click="handleViewMore()">
          查看更多<el-icon><arrow-right /></el-icon>
        </el-button>
      </div>
      <div class="product-list">
        <div v-for="product in goodsStore.goodsList" :key="product.createTime" class="product-card"
          @click="handleProductClick(product)">
          <div class="product-image">
            <img :src="product.imageUrl" :alt="product.productName">
            <div class="product-tag hot">热销</div>
          </div>
          <div class="product-info">
            <h3>{{ product.productName }}</h3>
            <p class="desc">{{ product.description }}</p>
            <div class="price">¥{{ product.price }}</div>
            <div class="sales">库存 {{ product.stock }}+</div>
          </div>
        </div>
      </div>
    </div>

  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useRouter } from 'vue-router'
import { ArrowRight } from '@element-plus/icons-vue'
import { useGoodsStore } from '@/stores/goods'


const router = useRouter()
const goodsStore = useGoodsStore()

// 分类相关
const categories = ref([])
const currentCategory = ref(null)

const handleCategoryEnter = (category) => {
  currentCategory.value = category
}

const handleCategoryLeave = () => {
  currentCategory.value = null
}

const handleCategoryClick = (category) => {
  router.push({
    path: '/category',
    query: { id: category.id }
  })
}

// 模拟分类数据
const mockCategories = [
  {
    id: 1,
    name: '手机数码',
    icon: 'el-icon-mobile-phone',
    children: [
      {
        id: 11,
        name: '手机',
        children: [
          { id: 111, name: '苹果' },
          { id: 112, name: '华为' },
          { id: 113, name: '小米' },
          { id: 114, name: 'OPPO' }
        ]
      },
      {
        id: 12,
        name: '电脑',
        children: [
          { id: 121, name: '笔记本' },
          { id: 122, name: '台式机' },
          { id: 123, name: '平板电脑' }
        ]
      }
    ]
  },
  {
    id: 2,
    name: '服装鞋包',
    icon: 'el-icon-shopping-bag-1',
    children: [
      {
        id: 21,
        name: '女装',
        children: [
          { id: 211, name: '连衣裙' },
          { id: 212, name: 'T恤' },
          { id: 213, name: '牛仔裤' }
        ]
      },
      {
        id: 22,
        name: '男装',
        children: [
          { id: 221, name: '衬衫' },
          { id: 222, name: '外套' },
          { id: 223, name: '休闲裤' }
        ]
      }
    ]
  },
  {
    id: 3,
    name: '家用电器',
    icon: 'el-icon-refrigerator',
    children: [
      {
        id: 31,
        name: '大家电',
        children: [
          { id: 311, name: '冰箱' },
          { id: 312, name: '洗衣机' },
          { id: 313, name: '空调' }
        ]
      },
      {
        id: 32,
        name: '厨房电器',
        children: [
          { id: 321, name: '微波炉' },
          { id: 322, name: '电饭煲' },
          { id: 323, name: '电水壶' }
        ]
      }
    ]
  }
]

// 轮播图相关
const banners = ref([])

// 模拟轮播图数据
const mockBanners = [
  {
    id: 1,
    title: '双十一大促',
    image: 'src\\assets\\images\\slideshow_pictures\\3231741507987.jpg'
  },
  {
    id: 2,
    title: '新品发布',
    image: 'src\\assets\\images\\slideshow_pictures\\3241741507988.jpg'
  },
  {
    id: 3,
    title: '限时特惠',
    image: 'src\\assets\\images\\slideshow_pictures\\3251741507989.jpg'
  },
  {
    id: 4,
    title: '正在特卖',
    image: 'src\\assets\\images\\slideshow_pictures\\3271741507990.jpg'
  },
  {
    id: 5,
    title: '不到叫啥',
    image: 'src\\assets\\images\\slideshow_pictures\\3261741507991.jpg'
  }
]

// 商品点击
const hotProducts = ref([])
const handleProductClick = (product) => {
  router.push(`/product/${product.productId}`)
}

// 查看更多
const handleViewMore = () => {
  router.push({ path: '/category' })
}

// 生命周期
onMounted(() => {
  // fetchCategories()
  // fetchBanners()
  categories.value = mockCategories
  banners.value = mockBanners
  goodsStore.getGoodsList()
  // fetchHotProducts()
})
</script>

<style lang="scss" scoped>
// Mixins
@mixin text-ellipsis {
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
}

.home {
  width: 100%;
  max-width: 1200px;
  margin: 0 auto;
  padding: 20px;

  @media (max-width: 768px) {
    padding: 10px;
  }

  .banner-section {
    display: flex;
    margin-bottom: 20px;
    height: 400px;
    width: 100%;
    gap: 20px;

    @media (max-width: 1024px) {
      height: auto;
      flex-direction: column;
      gap: 10px;
    }

    .category-nav {
      width: 200px;
      min-width: 200px;
      background-color: #fff;
      position: relative;

      @media (max-width: 1024px) {
        width: 100%;
        min-width: 100%;
      }

      .category-list {
        list-style: none;
        padding: 0;
        margin: 0;

        @media (max-width: 1024px) {
          display: flex;
          flex-wrap: wrap;
          gap: 10px;
        }

        .category-item {
          padding: 12px 20px;
          cursor: pointer;
          position: relative;

          @media (max-width: 1024px) {
            padding: 8px 15px;
            flex: 1;
            min-width: 120px;
            text-align: center;
          }

          .category-title {
            display: flex;
            align-items: center;
            gap: 8px;

            @media (max-width: 1024px) {
              justify-content: center;
            }
          }

          .sub-categories {
            position: absolute;
            left: 200px;
            top: 0;
            width: 400px;
            min-height: 100%;
            background-color: #fff;
            box-shadow: 2px 0 8px rgba(0, 0, 0, 0.1);
            padding: 20px;
            z-index: 10;

            @media (max-width: 1024px) {
              left: 0;
              top: 100%;
              width: 100%;
              min-height: auto;
            }

            @media (max-width: 768px) {
              position: fixed;
              top: 50%;
              left: 50%;
              transform: translate(-50%, -50%);
              width: 90%;
              max-height: 80vh;
              overflow-y: auto;
            }
          }
        }
      }
    }

    .banner-carousel {
      flex: 1;
      width: calc(100% - 220px);

      @media (max-width: 1024px) {
        width: 100%;
        height: 200px;
      }

      :deep(.el-carousel__item) {
        img {
          width: 100%;
          height: 100%;
          object-fit: cover;
          display: block;
        }
      }
    }
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
}
</style>
