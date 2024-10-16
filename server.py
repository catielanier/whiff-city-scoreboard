import os
from flask import Flask, send_from_directory
from flask_cors import CORS
from dotenv import load_dotenv

# load blueprints
from routes.user_routes import user_routes

# load constants
load_dotenv()
ENVIRONMENT: str = os.getenv("ENVIRONMENT")
DEBUG: bool = ENVIRONMENT != "prod"

app = Flask(__name__)
app.config.from_object(__name__)

CORS(app, resources={r'/*': {'origins': '*'}})

if not DEBUG:
    @app.route("/")
    def serve_svelte_app():
        return send_from_directory('dist', 'index.html')

# configure routes
app.register_blueprint(user_routes, url_prefix="/api/users")

if __name__ == "__main__":
    app.run()