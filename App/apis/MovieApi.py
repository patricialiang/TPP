from flask_restful import Resource,reqparse

from App.models import UserModel

parser = reqparse.RequestParser()
parser.add_argument("u_token")

class MovieResource(Resource):
    def get(self):

        parse = parser.parse_args()
        u_token = parse.get("u_token")

        if u_token:
            users = UserModel.query.filter(UserModel.u_token.__eq__(u_token))
            if users.count()>0:
                user = users.first()

                if user.u_permission == 1:
                    return {"msg":"ok","data":"请观看电影"}


        data ={
            "msg":"ok",
        }
        return data


    def post(self):
        pass