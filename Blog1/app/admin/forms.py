from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms import PasswordField
from wtforms import SubmitField
from wtforms import BooleanField
from wtforms.validators import DataRequired

class AdminLoginForm(FlaskForm):
    name = StringField('用户名', validators=[DataRequired("请填写用户名！")])
    password = PasswordField("密码",validators=[DataRequired("请填写密码！")],)
    remberme = BooleanField("记住我")
    submit = SubmitField("登录")


