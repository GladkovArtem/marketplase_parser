import os


class BaseConfig(object):
    DEBUG = False
    TESTING = False
    SQLALCHEMY_DATABASE_URI = "sqlite:////db.sqlite"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = '_qv3585a9i^w0dgdtcmj$osrna24$@+pzs5ga%h#efp&()mxg1'
    WTF_CSRF_ENABLED = True


class DevConfig(BaseConfig):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get("SQLALCHEMY_DATABASE_URI")


class TestingConfig(BaseConfig):
    TESTING = True


FLASK_ADMIN_SWATCH = 'cosmo'  # Список тем тут: https://bootswatch.com/)
