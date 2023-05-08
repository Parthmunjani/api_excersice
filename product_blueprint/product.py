from flask import make_response,request
from model import ProductModel
from flask_restful import Resource,marshal_with
from datetime import datetime

class ProductView(Resource):
    def get(self):
        try:
            products = ProductModel.query.all()
            if not products:
                return make_response({"status":False,"detail":"No Data In Table"})
            data = [product.to_json(product) for product in products]
            return make_response({"status":True,"detail":data})
        except Exception as e:
            return make_response({"status":False,"detail":str(e)})
    
    def post(self):
        try:
            data=request.get_json()
            create_user = ProductModel(data)
            ProductModel.add(create_user)
            data=create_user.to_json(create_user)
            return make_response({"status":True,"detail":"Product Add Successfully"})
        except Exception as e:
            return make_response({"status":False,"detail":str(e)})
        
class ProductDetails(Resource):
    def get(self,id):
        try:
            products = ProductModel.query.get(id) 
            if not products:
                return make_response({"status": False, "details": "Preoduct Not Added"})
            data=products.to_json(products)
            return make_response({"status":True,"detail":data})
        except Exception as e:
            return make_response({"status":False,"detail":str(e)})
        
    def put(self,id):
        try:
            product=ProductModel.query.get(id)
            data=request.get_json()
            product.price = data.get('price')
            product.name = data.get('name')
            product.category_id=data.get('category_id')
            product.modified_at=datetime.utcnow()
            ProductModel.put()
            data=product.to_json(product)
            return make_response({"status":True,"detail":data})
        except Exception as e:
            return make_response({"status":False,"detail":str(e)})
        
    def delete(self,id):
        try:
            user = ProductModel.query.get_or_404(id)
            ProductModel.delete(user)
            return make_response({"Status":True,"detail":"Product Data Delete"})
        except Exception as e:
            return make_response({"status":False,"detail":str(e)})