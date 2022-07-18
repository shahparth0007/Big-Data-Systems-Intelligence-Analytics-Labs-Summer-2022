from fastapi import FastAPI
import uvicorn
# import tensorflow as tf
# from tensorflow.keras.models import load_model

app = FastAPI()

# fashion_mnist = tf.keras.datasets.fashion_mnist
# (train_images, train_labels), (test_images, test_labels) = fashion_mnist.load_data()

@app.get("/")
async def root():
    return {"message": "Hello World"}

# @app.get("/test")
# async def root():
#     savedModel=load_model('gfgModel.h5')
#     predictions = savedModel.predict(test_images)
#     return str(predictions[1])

# if __name__ == '__main__':
#     uvicorn.run("main:app", host="127.0.0.1", port=8001, reload=True)