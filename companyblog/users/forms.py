# companyblog/users/forms.py
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, ValidationError
from wtforms.validators import DataRequired, Email, EqualTo
from flask_wtf.file import FileField, FileAllowed
from flask_login import current_user

from companyblog.models import User

class LoginForm(FlaskForm):
	email = StringField("email", validators=[DataRequired(), Email()])
	password = StringField("password", validators=[DataRequired()])
	submit = SubmitField("Login")

class RegistrationForm(FlaskForm):
	email = StringField("email", validators=[DataRequired(), Email()])
	username = StringField("username", validators=[DataRequired()])
	password = StringField("password", validators=[DataRequired(), EqualTo("pass_confirm", message="Passwords must match!")])
	pass_confirm = StringField("confirm_password", validators=[DataRequired()])
	submit = SubmitField("Register")

	def check_email(self, email):
		if User.query.filter_by(email=email.data).first():
			raise ValidationError("Your email has already been registered!")

	def check_username(self, username):
		if User.query.filter_by(username=username.data).first():
			raise ValidationError("Your username has already been registered!")

class UpdateUserForm(FlaskForm):
	email = StringField("email", validators=[DataRequired(), Email()])
	username = StringField("username", validators=[DataRequired()])
	picture = FileField("update_profile_picture", validators=[FileAllowed(['jpg','png'])])
	submit = SubmitField("Update User")

	def check_email(self, email):
		if User.query.filter_by(email=email.data).first():
			raise ValidationError("Your email has already been registered!")

	def check_username(self, username):
		if User.query.filter_by(username=username.data).first():
			raise ValidationError("Your username has already been registered!")
