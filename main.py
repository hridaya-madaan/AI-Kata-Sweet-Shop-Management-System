from fastapi import FastAPI
from .database import Base, engine
from .routers import auth, products, orders

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Sweet Kata Shop API")

app.include_router(auth.router)
app.include_router(products.router)
app.include_router(orders.router)

@app.get("/")
def root():
    return {"message": "Sweet Kata Shop Backend Running"}
