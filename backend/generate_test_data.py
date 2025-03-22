from backend import create_app, db
from backend.models import *
import datetime

app = create_app()


def generate_sample_data():
    with app.app_context():
        # 清空现有数据（可选）
        # db.drop_all()
        # db.create_all()

        # 创建用户
        admin_user = User(
            userid='admin_001',
            username='admin',
            password='admin123',
            email='admin@example.com',
            role='admin'
        )
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
        db.session.add_all([admin_user, buyer_user, seller_user])
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
        db.session.add_all([electronics_category, clothing_category])
        db.session.commit()  # 提交分类数据

        # 创建商品
        laptop_product = Product(
            proid='pro_laptop',
            name='Laptop',
            price=999.99,
            stock=100,
            description='High-performance laptop for everyday use',
            catid=electronics_category.catid
        )
        tshirt_product = Product(
            proid='pro_tshirt',
            name='T-Shirt',
            price=19.99,
            stock=200,
            description='Comfortable cotton t-shirt',
            catid=clothing_category.catid
        )
        db.session.add_all([laptop_product, tshirt_product])
        db.session.commit()  # 提交商品数据

        # 创建商店
        tech_shop = Shop(
            shopid='shop_tech',
            userid=seller_user.userid,
            shopname='Tech Store',
            shopdesc='Specializing in electronics and gadgets'
        )
        fashion_shop = Shop(
            shopid='shop_fashion',
            userid=seller_user.userid,
            shopname='Fashion Boutique',
            shopdesc='Latest fashion trends'
        )
        db.session.add_all([tech_shop, fashion_shop])
        db.session.commit()  # 提交商店数据

        # 创建购物车
        buyer_cart = Cart(
            carid='cart_buyer',
            userid=buyer_user.userid
        )
        db.session.add(buyer_cart)
        db.session.commit()  # 提交购物车数据

        # 添加商品到购物车
        cart_item_laptop = CartItem(
            carid=buyer_cart.carid,
            proid=laptop_product.proid,
            quantity=1
        )
        cart_item_tshirt = CartItem(
            carid=buyer_cart.carid,
            proid=tshirt_product.proid,
            quantity=2
        )
        db.session.add_all([cart_item_laptop, cart_item_tshirt])
        db.session.commit()  # 提交购物车商品数据

        # 创建订单
        order_pending = Order(
            orderid='order_pending',
            userid=buyer_user.userid,
            shopid=tech_shop.shopid,
            status='pending'
        )
        order_shipped = Order(
            orderid='order_shipped',
            userid=buyer_user.userid,
            shopid=fashion_shop.shopid,
            status='shipped'
        )
        db.session.add_all([order_pending, order_shipped])
        db.session.commit()  # 提交订单数据

        # 添加订单商品
        order_item_laptop = OrderItem(
            orderid=order_pending.orderid,
            proid=laptop_product.proid,
            productname=laptop_product.name,
            price=laptop_product.price,
            quantity=1
        )
        order_item_tshirt = OrderItem(
            orderid=order_shipped.orderid,
            proid=tshirt_product.proid,
            productname=tshirt_product.name,
            price=tshirt_product.price,
            quantity=3
        )
        db.session.add_all([order_item_laptop, order_item_tshirt])
        db.session.commit()  # 提交订单商品数据


if __name__ == "__main__":
    generate_sample_data()
    print("Sample data generated successfully!")
