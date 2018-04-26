import uuid

from flask_restful import Resource, reqparse, fields, marshal_with

from App.ext import db
from App.models import UserModel

parser = reqparse.RequestParser()
parser.add_argument("username",type=str,required=True,help="用户名")
parser.add_argument("password",type=str,required=True,help="密码")
parser.add_argument("email",type=str,required=True,help="邮箱")

user_fields = {
    "u_name":fields.String,
    "u_email":fields.String(attribute="email"),
    "u_token":fields.String
}

result_fields = {
    "returnCode":fields.String,
    "returnValue":fields.Nested(user_fields),
    "msg":fields.String,
}

class UserResource(Resource):
    def get(self):
        pass
    @marshal_with(result_fields)
    def post(self):
        parse = parser.parse_args()
        username = parse.get("username")
        password = parse.get("password")
        email = parse.get("email")

        user = UserModel()
        user.u_name = username
        user.u_password = password
        user.u_email = email
        user.u_token = str(uuid.uuid4())

        try:
            db.session.add(user)
            db.session.commit()







            # msg = Message(subject="Subject",recipients = [email],sender="")

        except Exception as e:

            return {"returnCode":"200","msg":str(e)}
        return {"returnCode":"200","msg":"ok","returnValue":user}

    def patch(self):
        pass