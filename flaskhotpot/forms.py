from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField
from wtforms.fields.core import SelectField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from flaskhotpot.models import User
from flask_ckeditor import CKEditorField


class RegistrationForm(FlaskForm):
    username = StringField("아이디", validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField("이메일", validators=[DataRequired(), Email()])
    password = PasswordField("비밀번호", validators=[DataRequired()])
    confirm_password = PasswordField(
        "비밀번호 확인", validators=[DataRequired(), EqualTo("password")]
    )
    submit = SubmitField("가입하기")

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError("이미 존재한 유저이름입니다. 다른 유저 이름으로 사용하세요.")

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError("이미 존재한 이메일입니다. 다른 이메일으로 사용하세요.")


class LoginForm(FlaskForm):
    email = StringField("이메일", validators=[DataRequired(), Email()])
    password = PasswordField("비밀번호", validators=[DataRequired()])
    remember = BooleanField("Remember Me")
    submit = SubmitField("로그인")


class PostForm(FlaskForm):
    title = StringField("글 제목", validators=[DataRequired()])
    region = SelectField(
        "지역 이름",
        choices=[
            (1, "복쪽"),
            (2, "서쪽"),
            (3, "남쪽"),
            (4, "윈구이지역"),
            (5, "기타지역"),
        ],
    )
    content = CKEditorField("글 내용", validators=[DataRequired()])
    submit = SubmitField("제출")
