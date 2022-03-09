from flask import Flask,session,g
from flask_migrate import Migrate
from models import UserModel
import config
from exts import db,mail
from blueprints import user_bp,qa_bp
app = Flask(__name__)
app.config.from_object(config)
db.init_app(app)
mail.init_app(app)
migrate = Migrate(app,db)

app.register_blueprint(user_bp)
app.register_blueprint(qa_bp)

#钩子函数在app.py中写   在请求之前，就会执行
@app.before_request
def before_request():
    user_id = session.get("user_id")
    if user_id:
        try:
            user = UserModel.query.get(user_id)
            #给g绑定一个user变量它的值是user
            #setattr(g,"user",user)
            g.user = user

        except:
            g.user = None
#一个请求来了先执行before_request->视图函数->视图函数中返回模板->context_processor
#渲染的所有视图都会去执行这个装饰器下的函数
@app.context_processor
def context_processor():
    if hasattr(g,"user"):
        return {"user":g.user}
    else:
        return {}


if __name__ == '__main__':
    app.run()
