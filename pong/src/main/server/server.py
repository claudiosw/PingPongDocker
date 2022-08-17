from flask import Flask
from flask_cors import CORS
# Import Blueprints
from src.main.routes.pong_routes import pong_routes_bp


app = Flask(__name__)
CORS(app)


# Register Blueprints
app.register_blueprint(pong_routes_bp)
