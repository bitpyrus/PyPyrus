from fastapi import FastAPI
from backend.api import user_routes, notebook_routes

app = FastAPI(title="pypyrus")

app.include_router(user_routes.router, prefix="/users", tags=["Users"])
app.include_router(notebook_routes.router, prefix="/notebooks", tags=["Notebooks"])

@app.get("/")
def home():
    return {"message": "Welcome to the pypyrus"}
