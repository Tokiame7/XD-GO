// 导入一个defineStore 方法
import { defineStore} from 'pinia'
import { ref }  from 'vue'//ref 让数据变为响应式数据 ref()\ref([]) 可以是单个数据、数组、对象
//pinia 就是打包数据和方法让这些数据在几个组件间被统一管理

const exampleList = [
    {
    id: 1,
    name: 'iPhone 15 Pro Max',
    description: '超强A17芯片，4800万像素主摄',
    price: 9999.00,
    monthSales: 3500,
    image: 'src\\assets\\images\\product_pictures\\badminton.jpg',
    discount: 0.95
    },
    {
    id: 2,
    name: '华为 Mate 60 Pro',
    description: '麒麟芯片，超长续航，卫星通讯',
    price: 6999.00,
    monthSales: 5000,
    image: 'src\\assets\\images\\product_pictures\\cucumber.jpg',
    discount: 0.9
    },
    {
        id: 3,
        name: '小米14 Pro',
        description: '徕卡光学，骁龙8 Gen 3，超清屏幕',
        price: 4999.00,
        monthSales: 4200,
        image: 'src\\assets\\images\\product_pictures\\egg-1504992_1280.webp',
        discount: 0.88
      },
      {
        id: 4,
        name: 'MacBook Pro 14',
        description: 'M3 Max芯片，14核GPU，专业级性能',
        price: 14999.00,
        monthSales: 1200,
        image: 'src\\assets\\images\\product_pictures\\heels.jpg',
        discount: 0.92
      },
      {
        id: 5,
        name: '华为 MateBook X Pro',
        description: '3.1K原色全面屏，12代酷睿i7',
        price: 8999.00,
        monthSales: 800,
        image: 'src\\assets\\images\\product_pictures\\lipstick.jpg',
        discount: 0.85
      },
      {
        id: 6,
        name: '戴尔 XPS 13 Plus',
        description: '英特尔EVO认证，4K OLED屏幕',
        price: 9999.00,
        monthSales: 600,
        image: 'src\\assets\\images\\product_pictures\\orange.jpg',
        discount: 0.9
      },
      {
        id: 7,
        name: 'iPad Pro 12.9',
        description: 'M2芯片，mini-LED屏幕，专业性能',
        price: 7999.00,
        monthSales: 2000,
        image: 'src\\assets\\images\\product_pictures\\pillow.jpg',
        discount: 0.93
      },
      {
        id: 8,
        name: '小米平板6 Pro',
        description: '骁龙8+，2.8K分辨率，120Hz高刷',
        price: 3499.00,
        monthSales: 3000,
        image: 'src\\assets\\images\\product_pictures\\pingpong.jpg',
        discount: 0.87
      }
]

export const useSellerProucts = defineStore ('sellreproducts' , () => {//第一个属性是唯一属性
    //定义数据
    const sellerProductsList = ref([])

    //定义修改数据的方法(action 同步+异步)

    const getSellerProductsList = () => {
        sellerProductsList.value = exampleList//之后和API对接 暂时以example代替
    } 
    //导出需要的数据和方法
    return {
        sellerProductsList ,
        getSellerProductsList
    }
})

