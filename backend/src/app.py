from aps.app import api, app
from flask import jsonify

# from backend.src.services.weather_end_point import blp
from .services.poke_end_points import poke_blp

api.register_blueprint(poke_blp)

@app.route('/api/hello', methods=['GET'])
def hello():
    """
    Health check endpoint
    """
    return jsonify({'message': 'Hello World!'})
