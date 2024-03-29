from app.models.address import UserAddressModel
from datetime import datetime
from app.v1.service.data_service import DataService
import psycopg2


class AddressService:
    async def get_all_addresses(self):
        try:
            all_service = await DataService(UserAddressModel).get_all_data()
            return {"status": True, "detail": all_service}, 200
        except Exception as e:
            return {"status": False, "detail": str(e)}, 400

    def create_address(self,data):
        try:
            print(data)
            address_service=DataService(UserAddressModel).create_data(data)
            return {"status": True, "detail": "User Address Add Successfully"}, 200
        except Exception as e:
            return {"status": False, "detail": str(e)}, 400

    def get_address_by_id(self,id):
        try:
            address_service=DataService(UserAddressModel).get_all_data(id)
            return {"status": True, "detail": address_service}, 200
        except Exception as e:
            return {"status": False, "detail": str(e)}, 400

    def update_address(self,id, data):
        try:
            address = UserAddressModel.query.get(id)
            if not address:
                return {"status": False, "details": "Address Not found"}, 400
            address.state = data.get('state')
            address.street = data.get('street')
            address.user_id = data.get('user_id')
            address.zip = data.get('zip')
            address.modified_at = datetime.utcnow()
            UserAddressModel.put()
            data = address.to_json()
            return {"status": True, "detail": data}, 200
        except Exception as e:
            return {"status": False, "detail": str(e)}, 400

    def delete_address(self, id):
        try:
            conn = psycopg2.connect(
                host='localhost',
                port='5432',
                database='demo2',
                user='myuser',
                password='password'
            )
            cursor = conn.cursor()
            cursor.execute("DELETE FROM user_address WHERE id = %s", (id,))
            conn.commit()
            conn.close()
            # address_service = DataService(UserAddressModel).delete_data(id)
            return {"status": True, "detail": "Address Delete"}, 200
        except Exception as e:
            return {"status": False, "detail": str(e)}, 400

