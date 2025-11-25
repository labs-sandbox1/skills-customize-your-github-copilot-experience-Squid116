# Starter code for FastAPI REST API assignment

from fastapi import FastAPI
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI()

# Example Pydantic model
class Item(BaseModel):
    id: int
    name: str
    description: Optional[str] = None

# In-memory database
items_db: List[Item] = []

@app.get("/")
def read_root():
    return {"message": "Welcome to FastAPI!"}

# Add your CRUD endpoints below

# Example:
# @app.post("/items/")
# def create_item(item: Item):
#     items_db.append(item)
#     return item
