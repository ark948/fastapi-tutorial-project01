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

@app.get("/items02/")
async def read_item_with_required_q_ellipsis(q: Annotated[str, Query(min_length=3)] = ...):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results

# older version
# async def read_items(q: str | None = Query(default=None, max_length=50)):