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

[![](https://mermaid.ink/img/pako:eNrNl-1P00Acx_-V5V4DYYOVsdeExPiGxHdmiTnbgzWuvdlelQkkYORJRUAeRgQMIVE0Bhg6RxwY_5m12_4Lr9deV-TWRQxI37S9-_Su9_093O8mgIwVBNIAGUMqHDOgltFj9LJMZMQmvGf3Momh6mOsWVViI3djGVBf_-QsnN4ZygAhpkMNBZS9siTA8tA0n2JDoZh9PFffmxEwSINqjgLN50f1oxPRIFmsexN9bxzvCgAD59z-xsHbxuJXQb-ZVfN5-vAAKoqBTJOyznqlUT6wd0r27nT4CwUSRFS6LtlA_JH--8K2fVZ1ipVmsSykrbzSop3tsrNZukhPeTcqhVB11s5lbxzt20sbbWWn2LCL1X6U7KOKEDOzmC2Yo_bGnF0tXkQVJKsazFETFTSkE6bJce1sqzm_2twXqWwSSCwz-L_6y4ozPSNUI49N4r64My-vUp0jlKPTc9nY9BGonMNmYJHZb83iYRR8ffZTCdLCNlSpehdt5-q9NiM0Dbf0cAdL5w0ctl6b0SilWDLxI9EDaSTWD0pCUxuq3OJqZ6fO3nmYcxfy2II6UUkhwJyNUnN--QY1ph6h6qNYECVuj6-z5yz_pHA4lkSZjqsGNWz9VXx4XER8XJNuni-IdGO-NNLBl2RIAo9bmKufnAmpDq7GtbAeUifKhcjFY2dvvrm_FYYJGidUZlM21DxRsd7yueXlxq8ru7BJsPyoNXN1zT7cirKXx924vWRoiIxFm4NkUj6sL35u_Px4Jf-9HdHsrjIyYfI1RnpmK54jJemQNG-LIgSNYaMgtD0JArVzCDKifQgG7s24G3dvXoMIlul2hRPSn6WJwMHtpc2oYieUlarF9pJQ0k03AXk5z_CKEslIfRKUuF61WKtWI1BepXps-1rVx_9rKRo6AUxOdnfjSb8wTQcTcNhrD0MsmBn4etZe-XIBZH0-zLcjhp5v0AzFUb7BX5ra3zjfvfB27TY8--0QzlIfZ1lS_RO0T97Xqm_CSPhH2SedsYj1-D3BeH58p4Pg42QQE5eW8uqDs7PoYqALaMigRyKFHtlY6GQAySINZYALKmgUWjniklMUhRbB9wq6DNLEsFAXMLA1lgXpUZgz6ZvnCv6pL2jNQ_0-xhr_hL6C9AQYB-m-ZM9gbyo5MBCnNykej0tdoADS3fG-pNQjDdKm3oSUlPoGE1Nd4BkbItGTiiekwf5kf580kJISqf6p3zd7kgc?type=png)](https://mermaid.live/edit#pako:eNrNl-1P00Acx_-V5V4DYYOVsdeExPiGxHdmiTnbgzWuvdlelQkkYORJRUAeRgQMIVE0Bhg6RxwY_5m12_4Lr9deV-TWRQxI37S9-_Su9_093O8mgIwVBNIAGUMqHDOgltFj9LJMZMQmvGf3Momh6mOsWVViI3djGVBf_-QsnN4ZygAhpkMNBZS9siTA8tA0n2JDoZh9PFffmxEwSINqjgLN50f1oxPRIFmsexN9bxzvCgAD59z-xsHbxuJXQb-ZVfN5-vAAKoqBTJOyznqlUT6wd0r27nT4CwUSRFS6LtlA_JH--8K2fVZ1ipVmsSykrbzSop3tsrNZukhPeTcqhVB11s5lbxzt20sbbWWn2LCL1X6U7KOKEDOzmC2Yo_bGnF0tXkQVJKsazFETFTSkE6bJce1sqzm_2twXqWwSSCwz-L_6y4ozPSNUI49N4r64My-vUp0jlKPTc9nY9BGonMNmYJHZb83iYRR8ffZTCdLCNlSpehdt5-q9NiM0Dbf0cAdL5w0ctl6b0SilWDLxI9EDaSTWD0pCUxuq3OJqZ6fO3nmYcxfy2II6UUkhwJyNUnN--QY1ph6h6qNYECVuj6-z5yz_pHA4lkSZjqsGNWz9VXx4XER8XJNuni-IdGO-NNLBl2RIAo9bmKufnAmpDq7GtbAeUifKhcjFY2dvvrm_FYYJGidUZlM21DxRsd7yueXlxq8ru7BJsPyoNXN1zT7cirKXx924vWRoiIxFm4NkUj6sL35u_Px4Jf-9HdHsrjIyYfI1RnpmK54jJemQNG-LIgSNYaMgtD0JArVzCDKifQgG7s24G3dvXoMIlul2hRPSn6WJwMHtpc2oYieUlarF9pJQ0k03AXk5z_CKEslIfRKUuF61WKtWI1BepXps-1rVx_9rKRo6AUxOdnfjSb8wTQcTcNhrD0MsmBn4etZe-XIBZH0-zLcjhp5v0AzFUb7BX5ra3zjfvfB27TY8--0QzlIfZ1lS_RO0T97Xqm_CSPhH2SedsYj1-D3BeH58p4Pg42QQE5eW8uqDs7PoYqALaMigRyKFHtlY6GQAySINZYALKmgUWjniklMUhRbB9wq6DNLEsFAXMLA1lgXpUZgz6ZvnCv6pL2jNQ_0-xhr_hL6C9AQYB-m-ZM9gbyo5MBCnNykej0tdoADS3fG-pNQjDdKm3oSUlPoGE1Nd4BkbItGTiiekwf5kf580kJISqf6p3zd7kgc)

#### 1. **用户表（User）**
用户表存储所有用户信息，包括买家、卖家和管理员。
```sql
CREATE TABLE user (
    userid VARCHAR(64) PRIMARY KEY,  -- 用户ID
    username VARCHAR(50) NOT NULL,   -- 用户名
    password VARCHAR(100) NOT NULL,  -- 密码
    email VARCHAR(100) NOT NULL,     -- 邮箱
    phone VARCHAR(20),               -- 电话
    role ENUM('buyer', 'seller', 'admin') NOT NULL,  -- 用户角色：买家、卖家、管理员
    shipping_address VARCHAR(200),   -- 用户收货地址
    createtime DATETIME DEFAULT CURRENT_TIMESTAMP,   -- 创建时间
    updatetime DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP  -- 更新时间
);
```

#### 2. **订单表（Order）**
订单表存储买家所创建的订单。
```sql
CREATE TABLE order (
    orderid VARCHAR(64) PRIMARY KEY,      -- 订单ID
    userid VARCHAR(64),                   -- 买家ID，外键
    shoppingid VARCHAR(64),               -- 商店ID，外键
    payment DECIMAL(20, 2),               -- 支付金额
    status ENUM('pending', 'completed', 'cancelled') DEFAULT 'pending',  -- 订单状态
    postdate DATETIME,                    -- 发货日期
    paytime DATETIME,                     -- 支付时间
    closetime DATETIME,                   -- 关闭时间
    createtime DATETIME DEFAULT CURRENT_TIMESTAMP, -- 创建时间
    updatetime DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- 更新时间
    FOREIGN KEY (userid) REFERENCES user(userid) ON DELETE CASCADE,
    FOREIGN KEY (shoppingid) REFERENCES shopping(shopid) ON DELETE CASCADE
);
```

#### 3. **订单商品表（OrderItem）**
存储每个订单包含的商品信息。
```sql
CREATE TABLE orderitem (
    id INT PRIMARY KEY AUTO_INCREMENT,
    orderid VARCHAR(64),                  -- 订单ID，外键
    proid VARCHAR(64),                    -- 商品ID，外键
    productname VARCHAR(100),             -- 商品名称
    price DECIMAL(20, 2),                 -- 商品价格
    quantity INT NOT NULL,                -- 商品数量
    createtime DATETIME DEFAULT CURRENT_TIMESTAMP, -- 创建时间
    updatetime DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- 更新时间
    FOREIGN KEY (orderid) REFERENCES order(orderid) ON DELETE CASCADE,
    FOREIGN KEY (proid) REFERENCES product(proid) ON DELETE CASCADE
);
```

#### 4. **支付表（PayInfo）**
存储支付信息，跟订单进行关联。
```sql
CREATE TABLE payinfo (
    payid VARCHAR(64) PRIMARY KEY,        -- 支付ID
    orderid VARCHAR(64),                  -- 订单ID，外键
    userid VARCHAR(64),                   -- 用户ID，外键
    amount DECIMAL(20, 2),                -- 支付金额
    status ENUM('pending', 'completed', 'failed') DEFAULT 'pending', -- 支付状态
    createtime DATETIME DEFAULT CURRENT_TIMESTAMP,   -- 创建时间
    updatetime DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- 更新时间
    FOREIGN KEY (orderid) REFERENCES order(orderid) ON DELETE CASCADE,
    FOREIGN KEY (userid) REFERENCES user(userid) ON DELETE CASCADE
);
```

#### 5. **商品表（Product）**
商品表存储商品的详细信息，包括分类、库存、价格等。
```sql
CREATE TABLE product (
    proid VARCHAR(64) PRIMARY KEY,         -- 商品ID
    catid VARCHAR(64),                     -- 分类ID，外键
    name VARCHAR(100),                     -- 商品名称
    subtitle VARCHAR(100),                 -- 商品副标题
    description TEXT,                      -- 商品描述
    price DECIMAL(20, 2),                  -- 商品价格
    stock INT,                             -- 商品库存
    status ENUM('available', 'out_of_stock', 'discontinued') DEFAULT 'available', -- 商品状态
    createtime DATETIME DEFAULT CURRENT_TIMESTAMP,   -- 创建时间
    updatetime DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- 更新时间
    FOREIGN KEY (catid) REFERENCES category(catid) ON DELETE CASCADE
);
```

#### 6. **购物车表（Cart）**
存储买家购物车中的商品。
```sql
CREATE TABLE cart (
    carid VARCHAR(64) PRIMARY KEY,         -- 购物车ID
    userid VARCHAR(64),                    -- 用户ID，外键
    quantity INT,                          -- 商品数量
    createtime DATETIME DEFAULT CURRENT_TIMESTAMP,   -- 创建时间
    updatetime DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- 更新时间
    FOREIGN KEY (userid) REFERENCES user(userid) ON DELETE CASCADE
);
```

#### 7. **购物车商品表（CartItem）**
存储购物车中每个商品的详细信息。
```sql
CREATE TABLE cartitem (
    id INT PRIMARY KEY AUTO_INCREMENT,
    carid VARCHAR(64),                     -- 购物车ID，外键
    proid VARCHAR(64),                     -- 商品ID，外键
    quantity INT NOT NULL,                 -- 商品数量
    createtime DATETIME DEFAULT CURRENT_TIMESTAMP,  -- 创建时间
    updatetime DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- 更新时间
    FOREIGN KEY (carid) REFERENCES cart(carid) ON DELETE CASCADE,
    FOREIGN KEY (proid) REFERENCES product(proid) ON DELETE CASCADE
);
```

#### 8. **商店表（Shopping）**
卖家的商店信息。
```sql
CREATE TABLE shopping (
    shopid VARCHAR(64) PRIMARY KEY,       -- 商店ID
    userid VARCHAR(64),                   -- 卖家ID，外键
    shopname VARCHAR(100),                -- 商店名称
    shopdesc TEXT,                        -- 商店描述
    receivername VARCHAR(100),            -- 收货人
    receiverphone VARCHAR(20),            -- 收货电话
    receiveraddress VARCHAR(200),         -- 收货地址
    createtime DATETIME DEFAULT CURRENT_TIMESTAMP,  -- 创建时间
    updatetime DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- 更新时间
    FOREIGN KEY (userid) REFERENCES user(userid) ON DELETE CASCADE
);
```

#### 9. **商品分类表（Category）**
商品分类信息。
```sql
CREATE TABLE category (
    catid VARCHAR(64) PRIMARY KEY,        -- 分类ID
    name VARCHAR(100),                    -- 分类名称
    status ENUM('active', 'inactive') DEFAULT 'active',  -- 分类状态
    createtime DATETIME DEFAULT CURRENT_TIMESTAMP,  -- 创建时间
    updatetime DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP  -- 更新时间
);
```

### **补充说明：**
- 订单和商品通过 `order` 和 `orderitem` 进行关联，支付信息存储在 `payinfo` 表，且与订单相关联。
- 购物车表和购物车商品表分别存储了购物车的基本信息和商品信息，购物车与买家进行关联。
- 商品通过 `category` 分类，并存储在 `product` 表中，商品的状态、库存等信息可以根据实际需要进行更新。

## 