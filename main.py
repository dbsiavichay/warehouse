import logging
import os

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import RedirectResponse

from src.di import initialize_dependencies
from src.product.infra.routes import router as product_router

logging.basicConfig(level=logging.INFO, format="%(levelname)s:     %(message)s")


origins = ["http://localhost:3000"]

# Configuración de la base de datos
DB_CONNECTION_STRING = os.environ.get("DATABASE_URL", "sqlite:///./warehouse.db")

# Inicializar dependencias
initialize_dependencies(DB_CONNECTION_STRING)

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
# app.add_middleware(ErrorHandlingMiddleware)

app.include_router(product_router, prefix="/products", tags=["products"])


@app.get("/")
async def root():
    return RedirectResponse("/docs")


if __name__ == "__main__":
    import uvicorn

    # Iniciar el servidor
    logging.info("Starting Warehouse API with dependency injection container")
    uvicorn.run(app, host="0.0.0.0", port=3000)
