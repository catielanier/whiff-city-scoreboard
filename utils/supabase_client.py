from supabase import create_client, Client

from utils.constants import SUPABASE_KEY, SUPABASE_URI

def get_client() -> Client:
    supabase: Client = create_client(SUPABASE_URI, SUPABASE_KEY)
    return supabase
