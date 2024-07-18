from fastapi import FastAPI
from pydantic import BaseModel, HttpUrl

app = FastAPI()

# url field will be validated to be a URL
class Image(BaseModel):
    url: HttpUrl
    name: str


class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None
    tags: set[str] = set()
    image: Image | None = None


@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item):
    results = {"item_id": item_id, "item": item}
    return results


@app.post("/images/multiple/")
async def create_multiple_images(images: list[Image]):
    return images



class Offer(BaseModel):
    name: str
    description: str | None = None
    price: float
    items: list[Item]


@app.post("/offers/")
async def create_offer(offer: Offer):
    return offer


# using dicts is also possible
# would be useful if you want to receive keys that you don't already know
@app.post("/index-weights/")
async def create_index_weights(weights: dict[int, float]):
    return weights