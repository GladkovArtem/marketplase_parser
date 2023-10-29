import os
from time import time
from parser.views.users import users_app
from parser.views.urls import urls_app
from parser.views.comments import comments_app
from parser.views.get_product_list import get_product_list_app
from flask import Flask, g, render_template
from flask import request
from parser.models.database import db
import pymysql
from parser.views.auth import login_manager, auth
from flask_migrate import Migrate
from security import flask_bcrypt
from parser.admin import admin


cfg_name = os.environ.get("CONFIG_NAME") or "DevConfig"
app = Flask(__name__)
app.config.from_object(f"parser.configs.{cfg_name}")
count = 0
app.register_blueprint(users_app, url_prefix="/users")
app.register_blueprint(comments_app, url_prefix="/comments")
app.register_blueprint(urls_app, url_prefix="/urls")
app.register_blueprint(get_product_list_app, url_prefix="/get_product_list_app")
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:SuperPassword1@localhost:3306/parser"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SECRET_KEY"] = "abcdefg123456"
app.register_blueprint(auth, url_prefix="/auth")
login_manager.init_app(app)
db.init_app(app)
migrate = Migrate(app, db)
migrate.init_app(app, db)
flask_bcrypt.init_app(app)
admin.init_app(app)


@app.route('/', methods=['GET'])
def index():
    # name = request.args.get('name', None)
    # global count
    # count += 1
    # return f'Количество посещений: {count}!'
    return render_template("index.html")


@app.before_request
def process_before_request():
    g.start_time = time()


@app.after_request
def process_after_request(response):
    if hasattr(g, "start_time"):
        response.headers["process-time"] = time() - g.start_time
    return response


@app.errorhandler(404)
def handler_404(error):
    return '404'

