# routes/auth_routes.py
from fastapi import APIRouter, HTTPException, Header,Depends
from services.auth.auth_services import login,logout,get_logged_user
from pydantic import BaseModel, EmailStr, StringConstraints
from typing_extensions import Annotated

router = APIRouter(prefix="/auth", tags=["Site - Auth"])

class LoginRequest(BaseModel):
    email: EmailStr
    password: Annotated[str, StringConstraints(min_length=1, max_length=50)]

@router.post("/login")
async def login_route(data: LoginRequest):
    return login(data.email, data.password)


@router.post("/logout")
async def logout_route(authorization: str = Header(None)):
    if not authorization:
        raise HTTPException(status_code=401, detail="Token não fornecido")
    if not authorization.startswith("Bearer "):
        raise HTTPException(status_code=400, detail="Formato do token inválido")
    token = authorization.split(" ")[1]  # Extraindo apenas o token

    response = logout(token)
    if "error" in response:
        raise HTTPException(status_code=response["error"]["status"], detail=response["error"]["message"])
    return response


@router.get("/me")
async def me_route(authorization: str = Header(None)):
    if not authorization:
        raise HTTPException(status_code=401, detail="Token não fornecido")

    if not authorization.startswith("Bearer "):
        raise HTTPException(status_code=400, detail="Formato do token inválido")

    token = authorization.split(" ")[1]  # Extraindo o token do header
    response = get_logged_user(token)

    if "error" in response:
        raise HTTPException(status_code=response["error"]["status"], detail=response["error"]["message"])

    return response  # Retorna os dados do usuário logado
