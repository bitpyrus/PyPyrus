from fastapi import APIRouter
import os

router = APIRouter()


@router.post("/create")
def create_notebook(title: str):
    notebook_path = f"notebooks/{title}.ipynb"
    with open(notebook_path, "w") as f:
        f.write("{}")  # Empty JSON notebook file
    return {"message": f"Notebook '{title}' created"}
