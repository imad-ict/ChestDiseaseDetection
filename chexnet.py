import numpy as np
from keras.models import load_model
from tensorflow.keras.preprocessing import image
from keras.applications.densenet import preprocess_input

class ChexNet:
    def __init__(self, weights_path):
        self.model = load_model(weights_path)

    def predict(self, img_path):
        img = image.load_img(img_path, target_size=(224, 224))
        img = img.convert('RGB')  # Convert image to RGB
        x = image.img_to_array(img)
        x = np.expand_dims(x, axis=0)
        x = preprocess_input(x)

        preds = self.model.predict(x)
        return preds[0]
