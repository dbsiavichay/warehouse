import logging

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import RedirectResponse

from src import initialize
from src.core.infra.middlewares import ErrorHandlingMiddleware
from src.movement.infra.routes import MovementRouter
from src.product.infra.routes import ProductRouter
from src.stock.infra.routes import StockRouter

product_router = ProductRouter()
stock_router = StockRouter()
movement_router = MovementRouter()

logging.basicConfig(level=logging.INFO, format="%(levelname)s:     %(message)s")


origins = ["http://localhost:3000"]

initialize()

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.add_middleware(ErrorHandlingMiddleware)

app.include_router(product_router.router, prefix="/products", tags=["products"])
app.include_router(stock_router.router, prefix="/stock", tags=["stock"])
app.include_router(movement_router.router, prefix="/movements", tags=["movements"])


@app.get("/")
async def root():
    return RedirectResponse("/docs")


if __name__ == "__main__":
    import uvicorn

    # Iniciar el servidor
    logging.info("Starting Warehouse API with dependency injection container")
    uvicorn.run(app, host="0.0.0.0", port=3000)
