from App.ext import db
from App.model_utils import BaseModel


class Letter(db.Model):
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    letter = db.Column(db.String(2))

class City(db.Model):
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    regionName = db.Column(db.String(16))
    pinyin = db.Column(db.String(16))
    cityCode = db.Column(db.String(16))
    letter = db.Column(db.String(2))











class UserModel(BaseModel,db.Model):
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    u_name = db.Column(db.String,unique=True)
    u_password = db.Column(db.String(256))
    u_email = db.Column(db.String(64),unique=True)
    is_active = db.Column(db.Boolean,default=False)
    u_token = db.Column(db.String(256))
    u_permission = db.Column(db.Integer,default=1)






