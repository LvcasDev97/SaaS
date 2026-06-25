from fastapi import FastAPI
from app.routers import users, products, sales

app = FastAPI()

# Inclui os routers
app.include_router(users.router)
app.include_router(products.router)
app.include_router(sales.router)

@app.get("/dashboard")
def get_dashboard():
    return {"msg": "Área aberta, sem autenticação"}
