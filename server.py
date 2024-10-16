from flask import Flask, send_from_directory
from flask_cors import CORS
from flask_socketio import SocketIO

# load blueprints
from routes.user_routes import user_routes
from routes.scoreboard_routes import scoreboard_routes

# load constants
from utils.constants import ENVIRONMENT

DEBUG: bool = ENVIRONMENT != "prod"

app = Flask(__name__)
app.config.from_object(__name__)

CORS(app, resources={r'/*': {'origins': '*'}})

socket: SocketIO = SocketIO(app, cors_allowed_origins="*")

if not DEBUG:
    @app.route("/")
    def serve_svelte_app():
        return send_from_directory('dist', 'index.html')

# configure routes
app.register_blueprint(user_routes, url_prefix="/api/users")
app.register_blueprint(scoreboard_routes, url_prefix="/api/scoreboard")

if __name__ == "__main__":
    socket.run(app, debug=DEBUG)