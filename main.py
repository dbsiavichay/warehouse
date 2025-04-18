import logging

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import RedirectResponse

from src.product.infra.routes import router as product_router

logging.basicConfig(level=logging.INFO, format="%(levelname)s:     %(message)s")


origins = ["http://localhost:3000"]

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

    uvicorn.run(app, host="0.0.0.0", port=3000)
