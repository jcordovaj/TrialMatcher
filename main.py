from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from mcp_instance import mcp

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Esto inicializa el motor de MCP correctamente
    async with mcp.session_manager.run():
        yield

app = FastAPI(lifespan=lifespan)

# Configuración crítica de CORS para PromptOpinion
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Montamos la app MCP en la raíz
app.mount("/", mcp.streamable_http_app())
