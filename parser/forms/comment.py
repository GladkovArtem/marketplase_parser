from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, validators, SelectMultipleField


class CreateCommentForm(FlaskForm):
    title = StringField(
        "Title",
        [validators.DataRequired()],
    )
    body = TextAreaField(
        "Body",
        [validators.DataRequired()],
    )
    submit = SubmitField("Publish")

    tag = SelectMultipleField("Tags", coerce=int)
