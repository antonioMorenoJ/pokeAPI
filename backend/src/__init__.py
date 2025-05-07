from flask import Flask
from flask_smorest import Api
from flask_cors import CORS
from .services.poke_end_points import poke_blp as poke_end_points

def creat_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    CORS(app)

    api = Api(app)
    api.register_blueprint(poke_end_points)
    return app