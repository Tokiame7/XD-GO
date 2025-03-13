# XD-GO

## The  structure demo of XD-GO

```absh
shopping-app/
│
├── backend/                    # Flask 后端代码
│   ├── app.py                  # 启动 Flask 应用
│   ├── config.py               # 配置文件
│   ├── extensions.py           # 数据库连接、JWT 配置等全局扩展
│   ├── migrations/             # 数据库迁移脚本（Flask-Migrate）
│   ├── buyer/                  # 买家模块
│   │   ├── __init__.py         # 买家模块初始化
│   │   ├── models.py           # 买家模块的数据库模型
│   │   ├── routes.py           # 买家模块的路由和控制器
│   │   ├── services.py         # 买家模块的服务层
│   │   └── utils.py            # 买家模块的工具函数
│   ├── seller/                 # 卖家模块
│   │   ├── __init__.py         # 卖家模块初始化
│   │   ├── models.py           # 卖家模块的数据库模型
│   │   ├── routes.py           # 卖家模块的路由和控制器
│   │   ├── services.py         # 卖家模块的服务层
│   │   └── utils.py            # 卖家模块的工具函数
│   ├── admin/                  # 系统管理员模块
│   │   ├── __init__.py         # 系统管理员模块初始化
│   │   ├── models.py           # 系统管理员模块的数据库模型
│   │   ├── routes.py           # 系统管理员模块的路由和控制器
│   │   ├── services.py         # 系统管理员模块的服务层
│   │   └── utils.py            # 系统管理员模块的工具函数
│   ├── common/                 # 公共模块，存放共享的功能或类
│   │   ├── models.py           # 存放共用的数据库模型
│   │   ├── helpers.py          # 存放通用工具函数
│   │   └── config.py           # 存放所有模块共用的配置
│
├── frontend/                   # Vue.js 前端代码
│   ├── src/
│   │   ├── assets/             # 静态资源
│   │   ├── components/         # 组件库
│   │   ├── views/              # 页面视图
│   │   ├── store/              # Vuex 状态管理
│   │   ├── router.js           # Vue Router 配置
│   │   ├── api/                # 与后端 API 交互
│   │   ├── services/           # 前端服务层，用于封装 API 请求
│   │   └── App.vue             # 根组件
│   ├── public/                 # 静态文件
│   └── package.json            # 前端项目配置
│
├── requirements.txt            # 后端依赖
├── README.md                   # 项目文档
└── .gitignore                  # Git 忽略文件

```

## 我们如何开发协作

- 前后端分离：前端和后端通过 API 完全分离开发，后端提供 RESTful API，前端通过 Axios 或 Fetch 调用。
- 功能模块化：每个团队专注于自己模块的开发，避免代码冲突和重复工作。
- 状态管理：Vuex 用于管理全局状态，特别是用户认证、购物车、订单等跨页面的数据。
- 接口文档：通过工具APIFOX为每个模块生成接口文档，确保各小组之间的 API 交互准确无误。
- 代码版本管理：使用 Git 进行代码管理，各小组分别在不同分支上开发，最后合并到主分支。

## 我们的数据模型
> 我们采用 MySQL 作为数据库，并设计了如下数据模型。

#### 数据库UML图
[![](https://mermaid.ink/img/pako:eNq1VVtvmzAY_SvIT5uURIbmBm9pgtpIzUWETNsUqbLABWtgM9uoS5P89xlIUnIhTbWMJ-NzbB8fn89eAY_5GFgA8wFBAUfxgmrqm89sR1sV7ez71nP6jz3nS7v5VUsF5sQ_xVqwwCiK8SmqQwUnSIhXxv0KGMeIRKeYkY0MGS3Nao_nI42zCJ9jK7oISZIQGjwj3-dYiHfaoOfa7nBkax7HSGJJymL3YJr4B-BmQYtGXzEeJs6PKnM8JEnV9g6N-UchU2cymPfdKh0JZ9fqsPvDUe9JQXUjG0e8Ejgcu5qQzPv13uXa313Nx8LjJJGE0at8uH-a3GskRsHtDJg4g-qMqoydD-mlAGeYCFlSxvKgCYlkKm6rfOjao7L6zOkqURd3c-mkFeannvzkgf9OEZVELm9YNI5bXTBXn9MNVHzG9QvKjjz_L6bNHifT6XD8UGXccVKvSbhe3I0sOUxEXtJZd1bWN9tA_oas1_U6W2-L1drOJE4JeUQsjb3SM-DeijJhfxNvSbsL0cruHhwwTt52C-2gspg8CYrLqERkN2ch80PaXs_J0gJHkSiFvrS7szMdKSvxiKgTZSSogRhz9S766pHOk7AAMsTKbGCppo9fUBrJBVjQjaKiVLLZknrAkjzFNcBZGoTAekGRUH_FSW3f-X1vguhPxuLdEPULrBX4AyxDb3T0JtRhp9Vt3nXhXbsGlsDSO7BhmNDomF0DNk3YMTY18JbPABum3mpDw2jqbdNomdDc_AVunFH5?type=png)](https://mermaid.live/edit#pako:eNq1VVtvmzAY_SvIT5uURIbmBm9pgtpIzUWETNsUqbLABWtgM9uoS5P89xlIUnIhTbWMJ-NzbB8fn89eAY_5GFgA8wFBAUfxgmrqm89sR1sV7ez71nP6jz3nS7v5VUsF5sQ_xVqwwCiK8SmqQwUnSIhXxv0KGMeIRKeYkY0MGS3Nao_nI42zCJ9jK7oISZIQGjwj3-dYiHfaoOfa7nBkax7HSGJJymL3YJr4B-BmQYtGXzEeJs6PKnM8JEnV9g6N-UchU2cymPfdKh0JZ9fqsPvDUe9JQXUjG0e8Ejgcu5qQzPv13uXa313Nx8LjJJGE0at8uH-a3GskRsHtDJg4g-qMqoydD-mlAGeYCFlSxvKgCYlkKm6rfOjao7L6zOkqURd3c-mkFeannvzkgf9OEZVELm9YNI5bXTBXn9MNVHzG9QvKjjz_L6bNHifT6XD8UGXccVKvSbhe3I0sOUxEXtJZd1bWN9tA_oas1_U6W2-L1drOJE4JeUQsjb3SM-DeijJhfxNvSbsL0cruHhwwTt52C-2gspg8CYrLqERkN2ch80PaXs_J0gJHkSiFvrS7szMdKSvxiKgTZSSogRhz9S766pHOk7AAMsTKbGCppo9fUBrJBVjQjaKiVLLZknrAkjzFNcBZGoTAekGRUH_FSW3f-X1vguhPxuLdEPULrBX4AyxDb3T0JtRhp9Vt3nXhXbsGlsDSO7BhmNDomF0DNk3YMTY18JbPABum3mpDw2jqbdNomdDc_AVunFH5)

#### 1. **用户表（User）**
用户表存储所有用户信息，包括买家、卖家和管理员。
```sql
CREATE TABLE user (
    userid VARCHAR(64) PRIMARY KEY,  -- 用户ID
    username VARCHAR(50) NOT NULL,   -- 用户名
    password VARCHAR(100) NOT NULL,  -- 密码
    email VARCHAR(100) NOT NULL,     -- 邮箱
    phone VARCHAR(20),               -- 电话
    role ENUM('buyer', 'seller', 'admin') NOT NULL,  -- 用户角色（买家、卖家、管理员）
    shipping_address VARCHAR(200),   -- 收货地址
    createtime DATETIME DEFAULT CURRENT_TIMESTAMP,   -- 创建时间
    updatetime DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP  -- 更新时间
);

```

#### 2. **订单表（Order）**
订单表存储买家所创建的订单。
```sql
CREATE TABLE `order` (
    orderid VARCHAR(64) PRIMARY KEY,   -- 订单ID
    userid VARCHAR(64),                -- 买家ID
    shopid VARCHAR(64),                -- 商店ID
    status ENUM('pending', 'shipped', 'delivered') DEFAULT 'pending',  -- 订单状态（待发货、已发货、已完成）
    createtime DATETIME DEFAULT CURRENT_TIMESTAMP,   -- 创建时间
    updatetime DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- 更新时间
    FOREIGN KEY (userid) REFERENCES user(userid),   -- 外键关联用户表
    FOREIGN KEY (shopid) REFERENCES shopping(shopid)  -- 外键关联商店表
);

```

#### 3. **订单商品表（OrderItem）**
存储每个订单包含的商品信息。
```sql
CREATE TABLE orderitem (
    id INT PRIMARY KEY AUTO_INCREMENT,  -- 订单商品ID
    orderid VARCHAR(64),                -- 订单ID
    proid VARCHAR(64),                  -- 商品ID
    productname VARCHAR(100),           -- 商品名称
    price DECIMAL(10, 2),               -- 商品价格
    quantity INT,                       -- 商品数量
    createtime DATETIME DEFAULT CURRENT_TIMESTAMP,   -- 创建时间
    updatetime DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- 更新时间
    FOREIGN KEY (orderid) REFERENCES `order`(orderid),  -- 外键关联订单表
    FOREIGN KEY (proid) REFERENCES product(proid)      -- 外键关联商品表
);

```


#### 4. **商品表（Product）**
商品表存储商品的详细信息，包括分类、库存、价格、图片等。
```sql
CREATE TABLE product (
    proid VARCHAR(64) PRIMARY KEY,   -- 商品ID
    name VARCHAR(100) NOT NULL,      -- 商品名称
    price DECIMAL(10, 2) NOT NULL,   -- 商品价格
    stock INT NOT NULL,              -- 商品库存
    description TEXT,                -- 商品描述
    catid VARCHAR(64),               -- 商品分类ID
    image BLOB,                      -- 商品图片（二进制数据）
    createtime DATETIME DEFAULT CURRENT_TIMESTAMP,   -- 创建时间
    updatetime DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- 更新时间
    FOREIGN KEY (catid) REFERENCES category(catid)  -- 外键关联分类表
);

```

#### 5. **购物车表（Cart）**
存储买家购物车中的商品。
```sql
CREATE TABLE cart (
    carid VARCHAR(64) PRIMARY KEY,   -- 购物车ID
    userid VARCHAR(64),              -- 用户ID
    createtime DATETIME DEFAULT CURRENT_TIMESTAMP,   -- 创建时间
    updatetime DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- 更新时间
    FOREIGN KEY (userid) REFERENCES user(userid)   -- 外键关联用户表
);

```

#### 6. **购物车商品表（CartItem）**
存储购物车中每个商品的详细信息。
```sql
CREATE TABLE cartitem (
    id INT PRIMARY KEY AUTO_INCREMENT,  -- 购物车商品ID
    carid VARCHAR(64),                  -- 购物车ID
    proid VARCHAR(64),                  -- 商品ID
    quantity INT,                       -- 商品数量
    createtime DATETIME DEFAULT CURRENT_TIMESTAMP,   -- 创建时间
    updatetime DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- 更新时间
    FOREIGN KEY (carid) REFERENCES cart(carid),   -- 外键关联购物车表
    FOREIGN KEY (proid) REFERENCES product(proid)  -- 外键关联商品表
);

```

#### 7. **商店表（Shopping）**
卖家的商店信息。
```sql
CREATE TABLE shopping (
    shopid VARCHAR(64) PRIMARY KEY,    -- 商店ID
    userid VARCHAR(64),                -- 卖家ID
    shopname VARCHAR(100),             -- 商店名称
    shopdesc TEXT,                     -- 商店描述
    createtime DATETIME DEFAULT CURRENT_TIMESTAMP,   -- 创建时间
    updatetime DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- 更新时间
    FOREIGN KEY (userid) REFERENCES user(userid)  -- 外键关联用户表
);

```

#### 8. **商品分类表（Category）**
商品分类信息。
```sql
CREATE TABLE category (
    catid VARCHAR(64) PRIMARY KEY,     -- 分类ID
    name VARCHAR(100),                 -- 分类名称
    createtime DATETIME DEFAULT CURRENT_TIMESTAMP,   -- 创建时间
    updatetime DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP  -- 更新时间
);

```

