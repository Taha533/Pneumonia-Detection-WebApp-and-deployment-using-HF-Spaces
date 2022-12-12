import gradio as gr
import tensorflow as tf
from tensorflow import keras

model = keras.models.load_model("pneumonia.h5")
class_names = ["Normal","Pneumonia"]
def predict_image(img):
    img_4d=img.reshape(-1,224,224,3)
    prediction=model.predict(img_4d)[0]
    return {class_names[i]: float(prediction[i]) for i in range(2)}


image = gr.inputs.Image(shape=(224,224))
label = gr.outputs.Label(num_top_classes=2)

gr.Interface(fn=predict_image, inputs=image, outputs=label,interpretation='default').launch(inline = False)