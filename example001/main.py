from fastapi import FastAPI
from routers.item import router as item_router

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

app.include_router(item_router)

