from flask import Flask,Blueprint
from flask_restful import Api
from app.models.model import db
from flask_migrate import Migrate
from app.v1.views.user import Users,User,AuthLogin,TokenRefresh
from app.v1.views.category import Category,Categories
from app.v1.views.product import  Product,Products
from app.v1.views.address import Addresses,Address
from app.v1.views.order import *
from app.v1.views.order_item import OrderItemDetails
from flask_jwt_extended import JWTManager
from flasgger import Swagger

jwt = JWTManager()
app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='postgresql://postgres:123@localhost/demo'
app.config['JWT_SECRET_KEY'] = '1313'
api = Api(app)
jwt = JWTManager(app)


db.init_app(app)
jwt.init_app(app)
migrate=Migrate(app,db)
swagger = Swagger(app)

"""with app.app_context():
    db.create_all()"""
    
data_blueprint=Blueprint('data',__name__)

api=Api(data_blueprint)
app.register_blueprint(data_blueprint,url_prefix='/')

api.add_resource(TokenRefresh,'/refresh')
api.add_resource(AuthLogin, '/auth/login')
api.add_resource(Users,'/user')
api.add_resource(User,'/user/<int:id>')
api.add_resource(Categories,'/category')
api.add_resource(Category,'/category/<int:id>')
api.add_resource(Products,'/product')
api.add_resource(Product,'/product/<int:id>')
api.add_resource(Addresses,'/address')
api.add_resource(Address,'/address/<int:id>')
api.add_resource(Orders,'/order')
api.add_resource(Order,'/order/<int:id>')
api.add_resource(OrderStatus,'/order/<int:id>/status')
api.add_resource(OrderItemDetails,'/order_item')
api.add_resource(OrderStatusCounts, '/order/count/<int:id>')