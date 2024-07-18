from fastapi import FastAPI, Body, Header


app = FastAPI()

# path param
@app.get("/hi/{who}")
def greet(who):
    return f"Hello? {who}?"

# query param
@app.get("/hi2")
def greet2(who):
    return f"Hello? {who}?"

# using embed, we can use query params in body 
@app.post("/hi-post")
def greet(who:str = Body(embed=True)):
    return f"Hello {who}"

# passing argument as http header
@app.post("/hi-header")
def greet(who:str = Header()):
    return f"Hello {who}"

# return the user agent header
@app.post("/agent")
def get_agent(user_agent:str = Header()):
    return user_agent

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("hello:app", reload=True)