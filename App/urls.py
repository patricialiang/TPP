from flask_restful import Api

api = Api()
def init_urls(app):
    api.init_app(app=app)

