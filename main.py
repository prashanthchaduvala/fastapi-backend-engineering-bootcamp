from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return{'message': "Hello FastAPI"}



@app.get("/welcome/{name}")
def welcome(name: str):
    return {"message": f"welcome to FastAPi, {name}!"}
    