from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message":"Hello, FastApi"}

@app.get("/hello/{name}")
def read_item(name: str):
    return {"message": f"Hello, {name}! Welcome to FastApi."}

@app.get("/items/")
def read_items(skip: int =0 , limit: int = 10):
    return {"skip":skip,"limit":limit}
