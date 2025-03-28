from datetime import datetime

from backend import db


class User(db.Model):
    __tablename__ = 'user'
    userid = db.Column(db.String(64), primary_key=True)
    username = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    phone = db.Column(db.String(20))
    role = db.Column(db.Enum('buyer', 'seller', 'admin'), nullable=False)
    shipping_address = db.Column(db.String(200))
    createtime = db.Column(db.DateTime, default=datetime.utcnow)
    updatetime = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)


class Category(db.Model):
    __tablename__ = 'category'
    catid = db.Column(db.String(64), primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    createtime = db.Column(db.DateTime, default=datetime.utcnow)
    updatetime = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)


class Product(db.Model):
    __tablename__ = 'product'
    proid = db.Column(db.String(64), primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Numeric(10, 2), nullable=False)
    stock = db.Column(db.Integer, nullable=False)
    description = db.Column(db.Text)
    catid = db.Column(db.String(64), db.ForeignKey('category.catid'))
    userid = db.Column(db.String(64), db.ForeignKey('user.userid'))
    image = db.Column(db.String(255))  # 修改为 String 类型，存储图片 URL
    createtime = db.Column(db.DateTime, default=datetime.utcnow)
    updatetime = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    # 添加关系
    user = db.relationship('User', backref=db.backref('products', lazy=True))


class Cart(db.Model):
    __tablename__ = 'cart'
    carid = db.Column(db.String(64), primary_key=True)
    userid = db.Column(db.String(64), db.ForeignKey('user.userid'))
    createtime = db.Column(db.DateTime, default=datetime.utcnow)
    updatetime = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)


class CartItem(db.Model):
    __tablename__ = 'cartitem'
    id = db.Column(db.Integer, primary_key=True)
    carid = db.Column(db.String(64), db.ForeignKey('cart.carid'))
    proid = db.Column(db.String(64), db.ForeignKey('product.proid'))
    quantity = db.Column(db.Integer, nullable=False)
    createtime = db.Column(db.DateTime, default=datetime.utcnow)
    updatetime = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)


class Order(db.Model):
    __tablename__ = 'order'
    orderid = db.Column(db.String(64), primary_key=True)
    userid = db.Column(db.String(64), db.ForeignKey('user.userid'))
    sellerid = db.Column(db.String(64), db.ForeignKey('user.userid'))
    status = db.Column(db.Enum('pending', 'shipped', 'delivered'), default='pending')
    totalprice = db.Column(db.Numeric(10, 2), nullable=False, default=0.00)
    createtime = db.Column(db.DateTime, default=datetime.utcnow)
    updatetime = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    items = db.relationship('OrderItem', backref='order', lazy=True)


class OrderItem(db.Model):
    __tablename__ = 'orderitem'
    id = db.Column(db.Integer, primary_key=True)
    orderid = db.Column(db.String(64), db.ForeignKey('order.orderid'))
    proid = db.Column(db.String(64), db.ForeignKey('product.proid'))
    productname = db.Column(db.String(100))
    price = db.Column(db.Numeric(10, 2))
    quantity = db.Column(db.Integer, nullable=False)
    createtime = db.Column(db.DateTime, default=datetime.utcnow)
    updatetime = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
