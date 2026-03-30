from enum import Enum
from fastapi import APIRouter

router = APIRouter()

class ModelName(str, Enum):
    vgg = "vgg"
    densenet = "densenet"
    mobilenet = "mobilenet"

@router.get("/models/{model_name}")
async def get_model(model_name: ModelName):
    if model_name is ModelName.vgg:
        return {"model_name": model_name, "message": "Deep Learning FTW!"}

    if model_name.value == "densenet":
        return {"model_name": model_name, "message": "LeCNN all the images"}

    return {"model_name": model_name, "message": "Have some residuals"}

@router.get("/")
async def root():
    return {"message": "Hello World"}


## Order Matters
## The first one will always be used since the path matches first.
@router.get("/users")
async def read_user2():
    return ["Bean", "Elfo"]

@router.get("/users")
async def read_users():
    return ["Rick", "Morty"]


## Order Matters
## path operations are evaluated in order, you need to make
## sure that the path for /users/me is declared before the one for /users/{user_id}:
## Otherwise, the path for /users/{user_id} would match also for /users/me,
## "thinking" that it's receiving a parameter user_id with a value of "me".


@router.get("/users/me")
async def read_user_me():
    return {"user_id": "the current user"}

@router.get("/users/{user_id}")
async def read_user(user_id: str):
    return {"user_id": user_id}
