from fastapi import HTTPException, Header
from config.connection import supabase
from gotrue.errors import AuthApiError
import socket


def login(email: str, password: str):
    try:
        response = supabase.auth.sign_in_with_password({"email": email, "password": password})
        return {"access_token": response.session.access_token}
    except AuthApiError as e:
        if "Invalid login credentials" in str(e):
            raise HTTPException(status_code=401, detail="Credenciais de login inválidas. Verifique seu email e senha.")
        raise HTTPException(status_code=400, detail=f"Erro de autenticação: {str(e)}")
    except socket.gaierror:
        raise HTTPException(status_code=503, detail="Serviço indisponível. Verifique sua conexão de rede.")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro inesperado ao tentar autenticar: {str(e)}")


def logout(access_token: str):
    if not access_token:
        return {"error": {"status": 401, "message": "Token não fornecido"}}

    try:
        
        result = supabase.auth.sign_out()
        if isinstance(result, str): 
            return {"error": {"status": 400, "message": f"Resposta inesperada do Supabase: {result}"}}

        if hasattr(result, "error") and result.error:
            return {"error": {"status": 400, "message": result.error.message}}

        return {"message": "Logout realizado com sucesso"}

    except Exception as e:
        return {"error": {"status": 500, "message": "Erro inesperado ao fazer logout"}}



def get_logged_user(access_token: str):
    if not access_token:
        return {"error": {"status": 401, "message": "Token não fornecido"}}

    try:
        user_response = supabase.auth.get_user(access_token)
        user_data = user_response.user

        if not user_data:
            return {"error": {"status": 401, "message": "Usuário não autenticado"}}

        user_metadata = user_data.user_metadata
        role = user_metadata.get("role")

        if not role:
            raise HTTPException(status_code=403, detail="Usuário não possui role definido")

        
        return {
            "user": {
                "id": user_data.id,
                "email": user_data.email,
                "role":role
            }
        }

    except Exception as e:
        return {"error": {"status": 500, "message": "Erro inesperado ao obter usuário"}}

    



def verify_role(authorization: str = Header(None)):
    if not authorization:
        raise HTTPException(status_code=401, detail="Token não fornecido")

    try:
        # Garantir que o token tem o formato correto "Bearer <token>"
        parts = authorization.split(" ")
        if len(parts) != 2 or parts[0] != "Bearer":
            raise HTTPException(status_code=401, detail="Formato do token inválido")

        token = parts[1]

        # Consultar usuário no Supabase
        user_response = supabase.auth.get_user(token)

        # Se a resposta do Supabase for vazia ou None, o token é inválido
        if not user_response or not user_response.user:
            raise HTTPException(status_code=401, detail="Token inválido ou expirado")

        user_data = user_response.user
        user_metadata = user_data.user_metadata

        # Verificar se o usuário tem código de vendedor e role
        codigo_vendedor = user_metadata.get("codigo_vendedor")
        role = user_metadata.get("role")

        if not codigo_vendedor:
            raise HTTPException(status_code=403, detail="Usuário não possui código de vendedor")

        if not role:
            raise HTTPException(status_code=403, detail="Usuário não possui role definido")

        return {
            "id": user_data.id,
            "email": user_data.email,
            "codigo_vendedor": codigo_vendedor,
            "role": role
        }

    except HTTPException as e:
        raise e  # Manter códigos corretos (401, 403)
    
    except Exception as e:
        raise HTTPException(status_code=401, detail="Falha na autenticação.")



    
