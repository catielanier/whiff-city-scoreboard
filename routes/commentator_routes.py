from flask import Blueprint, request, jsonify, Response
from postgrest import APIResponse
from supabase import Client

from utils.supabase_client import get_client

supabase: Client = get_client()

commentator_routes: Blueprint = Blueprint("commentator_routes", __name__)


@commentator_routes.route("/", methods=["GET"])
def get_commentators() -> Response:
    commentator_info: APIResponse = supabase.table("commentator_info").select("*").execute()
    return jsonify({
        "status": 200,
        "commentator_info": commentator_info.data
    })