from flask import Blueprint, render_template
from parser.models import Url


urls_app = Blueprint("urls_app", __name__)


@urls_app.route("/", endpoint="list")
def urls_list():
    urls = Url.query.all()
    return render_template("url/list.html", urls=urls)
