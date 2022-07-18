from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/")
def read_root():
    return { "Lux app": "Welcome to Lux app" }


# if __name__ == '__main__':
#     uvicorn.run("main:app", host="127.0.0.1", port=8001, reload=True)



# Docker Build
#docker build -t mydocker .
# docker build -t parth71196/bigdatata:mydocker .

# Docker Run
# docker run -p 8001:8001 mydocker

# Clean the device
#docker system prune

#docker login

#docker push parth71196/bigdatata:tagname

# docker build --platform=linux/arm64 -t parth71196/bigdatata:mydocker-amd64 .