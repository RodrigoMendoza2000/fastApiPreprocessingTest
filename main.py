from fastapi import FastAPI
from preprocessing import Preprocessing

app = FastAPI()
preprocess_class = Preprocessing()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}


@app.get("/preprocess/{prompt}")
async def preprocess(prompt: str):
    return {"preprocessing: " f"{preprocess_class.transform_prompt_without_stem(prompt)}"}
