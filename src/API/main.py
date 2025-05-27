from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes import falhas, arvore_falhas,auth

app = FastAPI(
    title="API de Dados Volkswagen",
    description="API para consulta de dados processados da Volkswagen",
    version="1.0.0"
)

# Configuração do CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Em produção, especifique as origens permitidas
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Inclusão das rotas
app.include_router(falhas.router, prefix="/dados")
app.include_router(arvore_falhas.router)
app.include_router(auth.router)


@app.get("/")
async def root():
    """Endpoint raiz da API"""
    return {"message": "API de Dados Volkswagen - Endpoint raiz"}



if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app,host="0.0.0.0", port=8000)
