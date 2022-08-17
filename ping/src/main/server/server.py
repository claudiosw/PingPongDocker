from flask import Flask
from flask_cors import CORS
# Import Blueprints
from src.main.routes.ping_routes import ping_routes_bp


app = Flask(__name__)
CORS(app)


# Register Blueprints
app.register_blueprint(ping_routes_bp)
