from supabase import create_client, Client
from datetime import datetime
from config import settings
import json

supabase: Client = create_client(settings.SUPABASE_URL, settings.SUPABASE_API_KEY)

def log_event(status=None, service=None, error_description=None, level_type="ERROR", latency_ms=None, context=None):
  
 

    try:
        
        level_type = level_type.upper()
        if level_type not in ["SUCCESS", "WARNING", "ERROR"]:
            level_type = "ERROR"

        
        data = {
            "status": status,
            "service": service,
            "error_description": error_description if level_type == "ERROR" else None, 
            "level_type": level_type,
            "latency_ms": latency_ms,
            "context":context
        }

       
        try:
            json.dumps(data)
        except TypeError as e:
            print(f"[LOGGER] Erro de serialização JSON: {e} | Dados: {data}")
            return

        
        response = supabase.table("logs").insert(data).execute()

            

    except Exception as e:
        print(f"[LOGGER] Erro ao inserir log: {e}")

