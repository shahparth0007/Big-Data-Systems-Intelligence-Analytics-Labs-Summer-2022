from fastapi import FastAPI
import uvicorn

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/test")
async def root():
    return {"message": "Test Hello World"}

# if __name__ == '__main__':
#     uvicorn.run("main:app", host="127.0.0.1", port=8001, reload=True)