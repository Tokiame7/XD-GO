import { defineStore } from "pinia"
import { getHotProducts } from "@/api/shop"
import { ref, computed } from "vue"


export const useGoodsStore = defineStore('goods', () => {
    const goodsList = ref([])
    const getGoodsList = async () => {
      // 这里获取商品数据并入库
      const { data } = await getHotProducts()
      console.log(data);
      goodsList.value = data.list
    }
    const curGood = (id) => computed(() => goodsList.value.find(item => item.productId === id))
    return {
      goodsList, getGoodsList, curGood
    }
})
