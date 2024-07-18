# validation and metadata for path parameters

from typing import Annotated
from fastapi import FastAPI, Path, Query

app = FastAPI()

@app.get("/items/{item_id}")
async def read_item(
    item_id: Annotated[int, Path(title="The ID of the item to get")],
    q: Annotated[str | None, Query(alias="item-query")] = None,
    ):
    results = {"item_id": item_id}
    if q:
        results.update({"q": q})
    return results


@app.get("/items02/{item_id}")
async def read_item02(
    q: str,
    item_id: Annotated[int, Path(title="The ID of the item to get")]
    ):
    results = {"item_id": item_id}
    if q:
        results.update({"q": q})
        return results
    
# another trick
# is to just declare the parameters and kwargs
@app.get("/items03/{item_id}")
async def read_items03(*, item_id: int = Path(title="The ID of the item to get"), q: str):
    results = {"item_id": item_id}
    if q:
        results.update({"q": q})
    return results

# you can declare number contraints
# e.g. with ge=1 (greater than 1), item_id will need to be greater than or equal to 1
@app.get("items04/{item_id}")
async def read_items04(item_id: Annotated[int, Path(title="ID to get item", ge=1)], q: str):
    return {"item_id": item_id}

# there are more than just ge
# gt, ge, lt, le
# they can be use together
# also works for float

@app.get("items05/{item_id}")
async def read_items05(
    *,
    item_id: Annotated[int, Path(title="ID to get item", ge=0, le=1000)],
    q: str,
    size: Annotated[float, Query(gt=0, lt=10.5)],
):
    return 'someshit'