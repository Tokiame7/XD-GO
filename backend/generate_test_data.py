from backend import create_app, db
from backend.models import *
import os
from datetime import datetime

app = create_app()


def generate_sample_data():
    with app.app_context():
        # 清空现有数据（可选）
        db.drop_all()
        db.create_all()

        # 创建用户
        buyer_user = User(
            userid='buyer_001',
            username='john_doe',
            password='buyer123',
            email='john@example.com',
            role='buyer',
            shipping_address='123 Main St, New York, NY'
        )
        seller_user = User(
            userid='seller_001',
            username='jane_smith',
            password='seller123',
            email='jane@example.com',
            role='seller'
        )
        admin_user = User(
            userid='admin_001',
            username='admin',
            password='admin123',
            email='admin@example.com',
            role='admin'
        )
        db.session.add_all([buyer_user, seller_user, admin_user])
        db.session.commit()  # 提交用户数据

        # 创建商品分类
        electronics_category = Category(
            catid='cat_electronics',
            name='Electronics'
        )
        clothing_category = Category(
            catid='cat_clothing',
            name='Clothing'
        )
        home_appliances_category = Category(
            catid='cat_home_appliances',
            name='Home Appliances'
        )
        db.session.add_all([electronics_category, clothing_category, home_appliances_category])
        db.session.commit()  # 提交分类数据

        # 创建商品并为每个商品分配图片
        products = [
            Product(
                proid='pro_laptop',
                name='Laptop',
                price=999.99,
                stock=100,
                description='High-performance laptop for everyday use',
                catid=electronics_category.catid,
                image='https://pic1.imgdb.cn/item/67e2a8e50ba3d5a1d7e34984.jpg',
                userid=seller_user.userid
            ),
            Product(
                proid='pro_tshirt',
                name='T-Shirt',
                price=19.99,
                stock=200,
                description='Comfortable cotton t-shirt',
                catid=clothing_category.catid,
                image='https://pic1.imgdb.cn/item/67e2a8e50ba3d5a1d7e34983.jpg',
                userid=seller_user.userid
            ),
            Product(
                proid='pro_phone',
                name='Smartphone',
                price=499.99,
                stock=50,
                description='Latest model smartphone with amazing features',
                catid=electronics_category.catid,
                image='https://pic1.imgdb.cn/item/67e2a8e50ba3d5a1d7e34982.jpg',
                userid=seller_user.userid
            ),
            Product(
                proid='pro_jacket',
                name='Winter Jacket',
                price=79.99,
                stock=150,
                description='Warm and cozy winter jacket',
                catid=clothing_category.catid,
                image='https://pic1.imgdb.cn/item/67e2a8e50ba3d5a1d7e34981.jpg',
                userid=seller_user.userid
            ),
            Product(
                proid='pro_tablet',
                name='Tablet',
                price=349.99,
                stock=80,
                description='Lightweight tablet with a high-resolution display',
                catid=electronics_category.catid,
                image='https://pic1.imgdb.cn/item/67e2a8e40ba3d5a1d7e34980.jpg',
                userid=seller_user.userid
            ),
            Product(
                proid='pro_vacuum',
                name='Vacuum Cleaner',
                price=129.99,
                stock=60,
                description='Efficient and quiet vacuum cleaner',
                catid=home_appliances_category.catid,
                image='https://pic1.imgdb.cn/item/67e2a8e40ba3d5a1d7e34979.jpg',
                userid=seller_user.userid
            )
        ]
        db.session.add_all(products)
        db.session.commit()  # 提交商品数据

        # 创建购物车
        buyer_cart = Cart(
            carid='cart_buyer',
            userid=buyer_user.userid
        )
        db.session.add(buyer_cart)
        db.session.commit()  # 提交购物车数据

        # 添加商品到购物车
        cart_items = [
            CartItem(
                carid=buyer_cart.carid,
                proid=products[0].proid,
                quantity=1
            ),
            CartItem(
                carid=buyer_cart.carid,
                proid=products[1].proid,
                quantity=2
            ),
            CartItem(
                carid=buyer_cart.carid,
                proid=products[5].proid,
                quantity=1
            )
        ]
        db.session.add_all(cart_items)
        db.session.commit()  # 提交购物车商品数据

        # 创建订单
        orders = [
            Order(
                orderid='order_pending',
                userid=buyer_user.userid,
                sellerid=seller_user.userid,
                status='pending',
            ),
            Order(
                orderid='order_shipped',
                userid=buyer_user.userid,
                sellerid=seller_user.userid,
                status='shipped'
            ),
            Order(
                orderid='order_completed',
                userid=buyer_user.userid,
                sellerid=seller_user.userid,
                status='delivered'
            )
        ]
        db.session.add_all(orders)
        db.session.commit()  # 提交订单数据

        # 添加订单商品
        order_items = [
            OrderItem(
                orderid=orders[0].orderid,
                proid=products[0].proid,
                productname=products[0].name,
                price=products[0].price,
                quantity=1
            ),
            OrderItem(
                orderid=orders[1].orderid,
                proid=products[1].proid,
                productname=products[1].name,
                price=products[1].price,
                quantity=3
            ),
            OrderItem(
                orderid=orders[2].orderid,
                proid=products[5].proid,
                productname=products[5].name,
                price=products[5].price,
                quantity=1
            )
        ]
        db.session.add_all(order_items)
        db.session.commit()  # 提交订单商品数据


if __name__ == "__main__":
    generate_sample_data()
    print("Sample data generated successfully!")
