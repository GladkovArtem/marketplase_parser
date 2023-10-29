from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required
from parser.models import Url
from parser.forms.product import CreateProductForm
import parser_main_function
import time


get_product_list_app = Blueprint("get_product_list_app", __name__)


@get_product_list_app.route("/create/", methods=["GET", "POST"], endpoint="create")
@login_required
def create_request():
    error = None
    form = CreateProductForm(request.form)
    form.link.choices = [(link.id, link.link) for link in Url.query.order_by("link")]
    if request.method == "POST" and form.validate_on_submit():
        low_price = form.low_price.data
        max_price = form.max_price.data
        url = str(Url.query.get(form.link.data))
        parser_main_function.parser(url=url, low_price=low_price, top_price=max_price)
        flash('Загрузка выполнена, файл вы можете найти в каталоге "загрузки"!  Оставьте отзыв или комментарий о работе сервиса!')
        return redirect(url_for('get_product_list_app.create'))

    return render_template("product/create.html", form=form, error = error)


