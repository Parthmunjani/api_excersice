from model import UserModel
from flask import make_response,request
from flask_restful import Resource
from datetime import datetime
from werkzeug.utils import secure_filename

class Index(Resource):
    def get(self):
        return make_response({"status":True,"details":"How Are You"})

class UserView(Resource):
    def get(self): 
        try:
            users = UserModel.query.all()
            if not users:
                return make_response({"status":False,"detail":"No Data In Table"})
            data = [user.to_json(user) for user in users]
            return make_response({"status":True,"detail":data})
        except Exception as e:
            return make_response({"status":False,"detail":str(e)})
            
    def post(self):
        if request.content_type == 'application/json':
            data = request.json
        else:
            data = request.form
        try:
            file = request.files.get("id_proof_document")
            if not file:
                return make_response({"status": False, "detail": "Document is required"})
            if file:
                filename = secure_filename(file.filename)
                if filename.split('.')[-1] != 'pdf':
                    return make_response({"status":False,"details":'Only PDF documents are allowed'})
            
            create_user = UserModel(data)
            UserModel.add(create_user)
            data=create_user.to_json(create_user)
            return make_response({"status":True,"detail":"User Create Successfully"})
        except Exception as e:
            return make_response({"status":False,"detail":str(e)})
                       
class UpdateUser(Resource):
    def get(self,id):
        try:
            users = UserModel.query.get(id) 
            if not users:
                return make_response({"status": False, "details": "User Not Register"})
            data=users.to_json(users)
            return make_response({"status":True,"detail":data})
        except Exception as e:
            return make_response({"status":False,"detail":str(e)})
            
    def put(self,id):
        if request.content_type == 'application/json':
            data = request.json
        else:
            data = request.form
        try:
            user = UserModel.query.filter_by(id=id).first()
            if not user:
                return make_response({"status":False,"details":"User Not Register"})
            user.name = data.get('name')
            user.email = data.get('email')
            user.phone_number=data.get('phone_number')
            user.modified_at=datetime.utcnow()
            UserModel.put()
            data=user.to_json(user)
            return make_response({"status":True,"detail":data})
        except Exception as e:
            return make_response({"status":False,"detail":str(e)})

    def delete(self,id):
        try:
            user = UserModel.query.get_or_404(id)
            UserModel.delete(user)
            return make_response({"Status":True,"detail":"User Data Delete"})
        except Exception as e:
            return make_response({"status":False,"detail":str(e)})