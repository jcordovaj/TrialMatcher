from contextlib import asynccontextmanager
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fhir_context import fhir_request_ctx
from mcp_instance import mcp  # Crearemos este archivo a continuación
import uvicorn

@asynccontextmanager
async def lifespan(app: FastAPI):
    """Gestiona el inicio y cierre del servidor MCP."""
    async with mcp.session_manager.run():
        yield

app = FastAPI(title="TrialMatcher MCP Server", lifespan=lifespan)

# CONFIGURACIÓN CRÍTICA: Permite que PromptOpinion (dominio externo) 
# hable con tu servidor local sin bloqueos de seguridad.
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.middleware("http")
async def extract_fhir_headers(request: Request, call_next):
    """
    Middleware que captura los headers de cada mensaje y los 
    pone a disposición de las herramientas.
    """
    token = fhir_request_ctx.set(request)
    try:
        response = await call_next(request)
    finally:
        fhir_request_ctx.reset(token)
    return response

# Montamos el MCP en la raíz. Esto resuelve errores 404/405.
app.mount("/", mcp.streamable_http_app())

if __name__ == "__main__":
    # Comando para ejecutar: python main.py
    uvicorn.run(app, host="0.0.0.0", port=8000)
