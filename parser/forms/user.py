from flask_wtf import FlaskForm
from wtforms import StringField, validators, PasswordField, SubmitField


class UserBaseForm(FlaskForm):
    first_name = StringField("First Name")
    last_name = StringField("Last Name")
    username = StringField(
        "username", [validators.DataRequired()]
    )
    email = StringField(
        "Email Address", [validators.DataRequired(), validators.Email(), validators.Length(min=6, max=200)],
        filters=[lambda data: data and data.lower()]
    )


class RegistrationForm(UserBaseForm):
    password_ = PasswordField(
        "New Password", [validators.DataRequired(), validators.EqualTo("confirm", message="Passwords must match")]
    )
    confirm = PasswordField("Repeat Password", [validators.DataRequired()])
    submit = SubmitField("Register")


class LoginForm(FlaskForm):
    username = StringField(
        "username",
        [validators.DataRequired()],
    )
    password = PasswordField(
        "Password", [validators.DataRequired()],
    )
    submit = SubmitField("Login")
