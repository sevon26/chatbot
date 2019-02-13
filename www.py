from application import app
from api.wechat import route_api

app.register_blueprint(route_api, url_prefix='/api')
