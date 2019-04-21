from config import config
from flask import Flask


def create_app(env):
    app = Flask(__name__)
    app.config.from_object(config[env])

    # SSL
    if app.config["SSL_REDIRECT"]:
        from flask_sslify import SSLify
        SSLify(app, permanent=True)

    from .www import www
    app.register_blueprint(www)

    from .api import api
    app.register_blueprint(api, url_prefix="/api")

    return app
