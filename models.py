from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, validators
from wtforms.validators import DataRequired, Length, email


class LoginForm(FlaskForm):
    email = StringField("email", validators=[DataRequired(), validators.Email()], render_kw={"class": "email-field"})
    password = PasswordField("password", validators=[DataRequired(), validators.Length(min=8)],
                             render_kw={"class": "pasword-field"})
    submit = SubmitField("submit", render_kw={"class": "submit-field"})


class SignUpForm(FlaskForm):
    name = StringField("name", validators=[DataRequired()], render_kw={"class": "input-field"})
    phone = StringField("phone", validators=[DataRequired(), validators.Length(min=8)],
                        render_kw={"class": "input-field"})
    email = StringField("email", validators=[DataRequired(), validators.Email()], render_kw={"class": "input-field"})
    password = StringField("password", validators=[DataRequired(), validators.Length(min=8)],
                           render_kw={"class": "input-field"})
    address = StringField("address", validators=[DataRequired(), validators.Length(min=8)],
                          render_kw={"class": "input-field"})
    submit = SubmitField("submit", render_kw={"class": "submit-field"})


# This class is used to update user profile. For empty fields, it will keep the old values.
class UpdateProfileForm(FlaskForm):
    name = StringField("name", validators=[DataRequired()], render_kw={"class": "input-field"})
    phone = StringField("phone", validators=[DataRequired(), validators.Length(min=8)],
                        render_kw={"class": "input-field"})
    email = StringField("email", validators=[DataRequired(), validators.Email()], render_kw={"class": "input-field"})
    address = StringField("address", validators=[DataRequired(), validators.Length(min=8)],
                          render_kw={"class": "input-field"})
    submit = SubmitField("submit", render_kw={"class": "submit-field"})

