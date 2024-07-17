from fastapi import FastAPI
from enum import Enum
from pydantic import BaseModel

class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None

class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello world"}

# request body
@app.post("/items/")
async def create_item(item: Item):
    item_dict = item.dict()
    if item.tax:
        price_with_tax = item.price + item.tax
        item_dict.update({"price_with_tax": price_with_tax})
    return item_dict

# request body + path parameter
# ** to unpack the variable
@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item):
    return {"item_id": item_id, **item.dict()}

# request body + path + query parameter
@app.put("/items/{item_id}")
async def upadte_item2(item_id: int, item: Item, q: str | None = None):
    result = {"item_id": item_id, **item.dict()}
    if q:
        result.update({"q": q})
    return result

fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]

@app.get("/items/")
async def read_item(skip: int = 0, limit: int = 10):
    return fake_items_db[skip : skip + limit]


# Optional parameters
# pipe means 'or', q may either be string or None
# q is also optional and will be None by default
# here is item_id is path parameter
# and q is query paramter
@app.get("/items/{item_id}")
async def read_item(item_id: str, needy: str, skip: int = 0, limit: int | None = None):
    item = {"item_id": item_id, "needy": needy, "skip": skip, "limit": limit}
    return item
    # item = {"item_id": item_id}
    # if q:
    #     item.update({"q": q})
    # if not short:
    #     item.update(
    #         {"description": "This is an amazing item that has a long description"}
    #     )
    # return item

# e.g.
# http://127.0.0.1:8000/users/14/items/152?q=shit&short=true
@app.get("/users/{user_id}/items/{item_id}")
async def read_user_item(user_id: int, item_id: str, q: str | None = None, short: bool = False):
    item = {"item_id": item_id, "owner_id": user_id}
    if q:
        item.update({"q": q})
    if not short:
        item.update(
            {"description": "This is an amazing item that has a long description"}
        )
    return item


@app.get("/users/me")
async def read_user_me():
    return {"user_id", "the current user"}


@app.get("/users/{user_id}")
async def read_user(user_id: str):
    return {"user_id", user_id}

@app.get("/models/{model_name}")
async def get_model(model_name: ModelName):
    if model_name is ModelName.alexnet:
        return {"model_name": model_name, "message": "Deep Learning FTW!"}

    if model_name.value == "lenet":
        return {"model_name": model_name, "message": "LeCNN all the images"}

    return {"model_name": model_name, "message": "Have some residuals"}


