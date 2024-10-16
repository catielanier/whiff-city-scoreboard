from flask import Blueprint, request, jsonify, Response
from postgrest import APIResponse
from supabase import Client

from utils.supabase_client import get_client

supabase: Client = get_client()

scoreboard_routes: Blueprint = Blueprint("scoreboard_routes", __name__)


@scoreboard_routes.route("/", methods=["GET"])
def get_scoreboard() -> Response:
    player_scores: APIResponse = supabase.table("player_scores").select("*").execute()
    commentator_info: APIResponse = supabase.table("commentator_info").select("*").execute()
    return jsonify({
        "status": 200,
        "player_scores": player_scores.data,
        "commentator_info": commentator_info.data
    })
