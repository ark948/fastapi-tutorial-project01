from fastapi import FastAPI


app = FastAPI()

# path param
@app.get("/hi/{who}")
def greet(who):
    return f"Hello? {who}?"

# query param
@app.get("/hi2")
def greet2(who):
    return f"Hello? {who}?"

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("hello:app", reload=True)