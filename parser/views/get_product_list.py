from flask import Blueprint, render_template, request, current_app, redirect, url_for
from flask_login import login_required, current_user
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import joinedload
from werkzeug.exceptions import NotFound
from parser.models.database import db
from parser.models import User, Url
from parser.forms.product import CreateProductForm
import parser_main_function


get_product_list_app = Blueprint("get_product_list_app", __name__)


@get_product_list_app.route("/create/", methods=["GET", "POST"], endpoint="create")
@login_required
def create_request():
    error = None
    form = CreateProductForm(request.form)
    form.link.choices = [(link.link,link.id) for link in Url.query.order_by("link")]
    if request.method == "POST" and form.validate_on_submit():
        low_price = form.low_price.data
        max_price = form.max_price.data
        url = form.link.data
        parser_main_function.parser(url=url, low_price=low_price, top_price=max_price)

        return redirect(url_for('get_product_list_app.create'))

    return render_template("product/create.html", form=form, error = 'Загрузка выполнена, файл вы можете найти в каталоге "загрузки"!  Оставьте отзыв или комментарий о работе сервиса!')




