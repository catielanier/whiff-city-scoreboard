import os
from flask import Flask, send_from_directory
from flask_cors import CORS
from dotenv import load_dotenv
from supabase import create_client, Client

# load blueprints
from routes.user_routes import user_routes

# load constants
load_dotenv()
SUPABASE_URI: str = os.getenv("SUPABASE_URI")
SUPABASE_KEY: str = os.getenv("SUPABASE_KEY")
ENVIRONMENT: str = os.getenv("ENVIRONMENT")
DEBUG: bool = ENVIRONMENT != "prod"

app = Flask(__name__)
app.config.from_object(__name__)

CORS(app, resources={r'/*': {'origins': '*'}})

supabase: Client = create_client(SUPABASE_URI, SUPABASE_KEY)

if not DEBUG:
    @app.route("/")
    def serve_svelte_app():
        return send_from_directory('dist', 'index.html')

# configure routes
app.register_blueprint(user_routes, url_prefix="/api/users")

if __name__ == "__main__":
    app.run()