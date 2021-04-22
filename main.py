from fastapi import FastAPI, Query

app = FastAPI()


@app.get("/items/")

async def read_items(q: str = Query("hello world")):

    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results
