from flask import Flask
from instance.config import app_config
from app.api import version2 as v2

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(app_config)
    app.register_blueprint(v2)

    return app
