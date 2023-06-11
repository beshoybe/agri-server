import numpy as np
import tensorflow as tf
from PIL import Image

def anlysis(path):
    labels = open('labels.txt', "r").readlines()

    # Load the TFLite model
    interpreter = tf.lite.Interpreter(model_path=r"model1.tflite")
    interpreter.allocate_tensors()

    # Get input and output tensors
    input_details = interpreter.get_input_details()
    output_details = interpreter.get_output_details()

    # Load the image
    image = Image.open(r'%s'%path).convert("RGB")
    image = image.resize((input_details[0]['shape'][1], input_details[0]['shape'][2]))

    # Prepare input data
    input_data = np.expand_dims(image, axis=0)
    input_data = input_data.astype(np.float32)

    # Set the input tensor
    interpreter.set_tensor(input_details[0]['index'], input_data)

    # Run inference
    interpreter.invoke()

    # Get the output tensor
    output_data = interpreter.get_tensor(output_details[0]['index'])

    # Process the output
    prediction = np.argmax(output_data[0])
    return labels[prediction-1]