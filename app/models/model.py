from flask_sqlalchemy import SQLAlchemy
from flask import request, make_response
from werkzeug.utils import secure_filename
from datetime import datetime
from uuid import uuid4
import os
from werkzeug.security import generate_password_hash, check_password_hash


db = SQLAlchemy()

class DBHandler:
    def delete(instance):
        db.session.delete(instance)
        db.session.commit() 

    def add(instance):
        db.session.add(instance)
        db.session.commit()    

    def put(self):
        db.session.commit()


# class RoleModel(db.Model,Change):
#     __tablename__ = 'roles'
#
#     id = db.Column(db.Integer, primary_key=True)
#     role_name = db.Column(db.String(255))
#     def __init__(self, data):
#         self.role_name = data.get("role_name")
#
#     def to_json(self):
#         data = {
#             "id":self.id,
#             "role_name": self.role_name,
#         }
#         return data
#
#
# class ApiPermission(db.Model,Change):
#     __tablename__ = 'api_permissions'
#
#     id = db.Column(db.Integer, primary_key=True)
#     api_name = db.Column(db.String(255))
#     method = db.Column(db.String(10))
#     role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))
#     role = db.relationship('RoleModel', backref='permissions')
#     def __init__(self, data):
#         self.api_name = data.get("api_name")
#         self.method = data.get("method")
#         self.role_id = data.get("role_id")
#
#     def to_json(self):
#         data = {
#             "api_name": self.api_name,
#             "method": self.method,
#             "role_id": self.role_id,
#         }
#         return data
#
#
# class UserModel(db.Model, Change):
#     __tablename__ = "user"
#
#     id = db.Column(db.Integer, primary_key=True)
#     uuid = db.Column(db.String(36), nullable=False, default=str(uuid4()))
#     name = db.Column(db.String(255))
#     email = db.Column(db.String(255))
#     password = db.Column(db.String(255))
#     phone_number = db.Column(db.String(20))
#     id_proof_document = db.Column(db.LargeBinary())
#     created_at = db.Column(db.DateTime, default=datetime.utcnow)
#     modified_at = db.Column(db.DateTime, default=datetime.utcnow)
#     is_deleted = db.Column(db.Boolean, default=False)
#     role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))
#     role = db.relationship('RoleModel')
#     def __init__(self,data):
#         self.name=data.get("name")
#         self.email=data.get("email")
#         self.phone_number=data.get("phone_number")
#         self.set_password(data.get("password"))
#         self.role_id=data.get("role_id")
#
#         file = request.files.get("id_proof_document")
#         if file:
#             filename = secure_filename(file.filename)
#             try:
#                 file.save(os.path.join("media", filename))
#                 with open(os.path.join("media", filename), "rb") as f:
#                     self.id_proof_document = f.read()
#             except Exception as e:
#                 return make_response({"status":False,"details":str(e)})
#
#     @property
#     def role_name(self):
#         # Access the role_name from the associated RoleModel
#         if self.role:
#             return self.role.role_name
#         return None
#
#     def set_password(self, password):
#         hashed_password = generate_password_hash(password)
#         self.password = hashed_password
#
#     def check_password(self, password):
#         return check_password_hash(self.password, password)
#
#     def to_json(self):
#         data = {
#             "id": self.id,
#             "uuid": self.uuid,
#             "name": self.name,
#             "email": self.email,
#             "phone_number": self.phone_number,
#             "role_id":self.role_id,
#         }
#         return data
#
# class CategoryModel(db.Model,Change):
#     __tablename__="category"
#
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(50), nullable=False)
#     parent_id = db.Column(db.Integer, db.ForeignKey('category.id'))
#     children = db.relationship('CategoryModel', backref=db.backref('parent', remote_side=[id]))
#     products = db.relationship('ProductModel', backref='category', lazy=True)
#     created_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
#     modified_at=db.Column(db.DateTime,default=datetime.utcnow)
#
#     def __init__(self, data, parent=None):
#         self.name = data.get('name')
#         self.parent_id = data.get('parent_id')
#
#     def to_json(self):
#         data = {
#             'id': self.id,
#             'name': self.name,
#         }
#         if self.children:
#             data['sub_category'] = [child.to_json() for child in self.children]
#         return data
#
# class ProductModel(db.Model,Change):
#     __tablename__="product"
#
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(50), nullable=False)
#     price = db.Column(db.Float(),nullable=True, default=0)
#     category_id = db.Column(db.Integer, db.ForeignKey('category.id'))
#     created_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
#     modified_at=db.Column(db.DateTime,default=datetime.utcnow)
#
#     def __init__(self, data):
#         self.name = data.get('name')
#         self.price = data.get('price', 0)
#         self.category_id=data.get('category_id')
#         self.created_at = datetime.utcnow()
#
#     def to_json(self):
#         data={
#             "name":self.name,
#             "price":self.price,
#             "category_id":self.category_id,
#         }
#         return data
#
# class UserAddressModel(db.Model,Change):
#     __tablename__="user_address"
#
#     id = db.Column(db.Integer, primary_key=True)
#     user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
#     street = db.Column(db.String(200), nullable=False)
#     state = db.Column(db.String(50), nullable=False)
#     zip = db.Column(db.String(10), nullable=False)
#     created_at = db.Column(db.DateTime, default=datetime.utcnow)
#     modified_at = db.Column(db.DateTime, default=datetime.utcnow)
#
#     def __init__(self,data):
#         self.user_id=data.get('user_id')
#         self.street=data.get('street')
#         self.state=data.get('state')
#         self.zip=data.get('zip')
#
#     def to_json(self):
#         data={
#             "user_id":self.user_id,
#             "street":self.street,
#             "state":self.state,
#             "zip":self.zip
#         }
#         return data
#
# class OrderModel(db.Model,Change):
#     __tablename__ = 'user_order'
#
#     id = db.Column(db.Integer, primary_key=True)
#     user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
#     payment_status=db.Column(db.String(200),nullable=False)
#     address_id=db.Column(db.Integer,db.ForeignKey('user_address.id'))
#     category_id = db.Column(db.Integer, db.ForeignKey('category.id'))
#     total_price = db.Column(db.Float())
#     status = db.Column(db.String(20))
#     created_at = db.Column(db.DateTime, default=datetime.utcnow)
#     modified_at = db.Column(db.DateTime, default=datetime.utcnow)
#     order_items = db.relationship('OrderItemModel', backref='user_order')
#
#     def __init__(self, data):
#         self.user_id=data.get('user_id')
#         self.payment_status = data.get('payment_status')
#         self.category_id=data.get('category_id')
#         self.total_price=data.get('total_price')
#         self.address_id=data.get('address_id')
#         self.status=data.get('status')
#
#     def to_json(self,data):
#         data={
#             "user_id":data.user_id,
#             "total_price":data.total_price,
#             "payment_status":data.payment_status,
#             "status":data.status
#         }
#         return data
#
# class OrderItemModel(db.Model,Change):
#     __tablename__ = 'order_item'
#
#     id = db.Column(db.Integer, primary_key=True)
#     order_id = db.Column(db.Integer, db.ForeignKey('user_order.id'))
#     product_id = db.Column(db.Integer, db.ForeignKey('product.id'))
#     quantity = db.Column(db.Integer)
#     created_at = db.Column(db.DateTime, default=datetime.utcnow)
#     modified_at = db.Column(db.DateTime, default=datetime.utcnow)
#
#     def __init__(self,data):
#         self.order_id=data.get('order_id')
#         self.product_id=data.get('product_id')
#         self.quantity=data.get('quantity')
#
#     def to_json(self):
#         data={
#             "order_id":self.order_id,
#             "product_id":self.product_id,
#             "quantity":self.quantity
#         }
#         return data
