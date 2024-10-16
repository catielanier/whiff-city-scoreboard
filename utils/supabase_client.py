import os
from dotenv import load_dotenv
from supabase import create_client, Client


load_dotenv()
SUPABASE_URI: str = os.getenv("SUPABASE_URI")
SUPABASE_KEY: str = os.getenv("SUPABASE_KEY")


def get_client() -> Client:
    supabase: Client = create_client(SUPABASE_URI, SUPABASE_KEY)
    return supabase
