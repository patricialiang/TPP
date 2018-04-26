from flask_restful import reqparse, Resource

from App.models import UserModel

parser = reqparse.RequestParser()
parser.add_argument("username",type=str,required=True,help="用户名")
parser.add_argument("password",type=str,required=True,help="密码")


class UserLoginResource(Resource):

    def post(self):

        parse = parser.parse_args()
        username = parse.get("username")
        password = parse.get("password")
        users = UserModel.query.filter(u_name=)














