
from fastapi import FastAPI


app = FastAPI()


@app.get("/")
async def home():
    info = { "slackUsername": "peauli", "backend": True, "age": 28, "bio": "I am a backend developer in the HNG9 internship" }
    return info


