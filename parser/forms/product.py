from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, validators, SelectField, IntegerField


class CreateProductForm(FlaskForm):
    low_price = IntegerField(
        "Цена от:",
        [validators.DataRequired()],
    )
    max_price = IntegerField(
        "Цена до:",
        [validators.DataRequired()],
    )
    link = SelectField("")
    submit = SubmitField("Запросить список")

