import wtforms
from wtforms.validators import length,email,EqualTo
from wtforms import ValidationError
from models import EmailCaptchaModel,UserModel

class LoginForm(wtforms.Form):
    email = wtforms.StringField(validators=[email()])
    password = wtforms.StringField(validators=[length(min=6, max=20)])
#这里的验证表单中的字段需要和前端register.html中Input标签中的name字段对齐，也就是对前端form表单中数据的验证，这里使用的是wtforms
class RegisterForm(wtforms.Form):
    username = wtforms.StringField(validators=[length(min=3,max=20)])
    email = wtforms.StringField(validators=[email()])
    captcha = wtforms.StringField(validators=[length(min=4, max=4)])
    password = wtforms.StringField(validators=[length(min=6,max=20)])
    password_confirm = wtforms.StringField(validators=[EqualTo("password")])
    #进一步在验证form中对数据进行校验
    def validate_captcha(self,field):
        captcha = field.data
        email = self.email.data
        captcha_model = EmailCaptchaModel.query.filter_by(email=email).first()
        if not captcha_model or captcha_model.captcha.lower() != captcha.lower():
            raise ValidationError("验证码输入有误！")
    #验证用户输入的注册邮箱是否之前就被注册过了
    def validate_email(self,field):
        email = field.data
        user_model = UserModel.query.filter_by(email=email).first()
        if user_model:
            raise ValidationError("该邮箱已经注册！")

class QuestionForm(wtforms.Form):
    title = wtforms.StringField(validators=[length(min=3, max=200)])
    content = wtforms.StringField(validators=[length(min=5)])

class CommentForm(wtforms.Form):
    content = wtforms.StringField(validators=[length(min=1)])
