from enum import Enum 
from fastapi import Body, FastAPI, Response, status, HTTPException
from pydantic import BaseModel

app = FastAPI()

class operation_type(Enum):
    multiplication= "multiplication"
    addition= "addition"
    subtraction = "subtraction"

class Post(BaseModel):
    operation_type: str
    x: int
    y: int

operation_list = ["multiplication", "addition", "subtraction"]


@app.get("/")
async def home():
    info = { "slackUsername": "peauli", "backend":  True, "age": 28, "bio": "I am a python backend developer in the HNG9 internship" }
    return info

@app.post("/posts")
def create_post(post:Post):
    print(post)
    result = 0
    if post.operation_type.lower() not in operation_list:
        return Response(status_code=status.HTTP_404_NOT_FOUND)

    if post.operation_type.lower() == operation_type.multiplication.name:
        result = post.x * post.y
        return {"slackUsername": "peauli", "result": result, "operation_type":operation_type.multiplication.value}
    elif post.operation_type.lower() == operation_type.addition.name:
        result = post.x + post.y
        return {"slackUsername": "peauli", "result": result, "operation_type":operation_type.addition.value}
    else:
        post.operation_type.lower() == operation_type.subtraction.name
        result = post.x - post.y
        return {"slackUsername": "peauli", "result": result, "operation_type":operation_type.subtraction.value}
