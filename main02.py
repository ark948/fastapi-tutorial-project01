from typing import Annotated
from fastapi import FastAPI, Query

app = FastAPI()

# enforcing validation on optional query parameter q
# documentation made q to be no more than 50
# but i will make it less to test it
@app.get("/items/")
async def read_item(q: Annotated[str | None, Query(max_length=5)] = None):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results