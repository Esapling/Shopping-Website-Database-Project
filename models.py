from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, validators
from wtforms.validators import DataRequired, Length, email


class LoginForm(FlaskForm):
    email = StringField("email", validators=[DataRequired(), validators.Email()] ,render_kw={"class":"email-field"})
    password = PasswordField("password", validators=[DataRequired(), validators.Length(min=8)], render_kw={"class":"pasword-field"})
    submit = SubmitField("submit", render_kw={"class": "submit-field"})