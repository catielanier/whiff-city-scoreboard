import os
from dotenv import load_dotenv

load_dotenv()

SUPABASE_KEY: str = os.getenv("SUPABASE_KEY")
SUPABASE_URI: str = os.getenv("SUPABASE_URI")
SECRET: str = os.getenv("SECRET")
ENVIRONMENT: str = os.getenv("ENVIRONMENT")