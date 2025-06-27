import cv2
import numpy as np
from tensorflow.keras.models import load_model as keras_load_model

emotion_labels = ['Angry', 'Disgust', 'Fear', 'Happy', 'Sad', 'Surprise', 'Neutral']

def load_model():
    return keras_load_model("model/emotion_model.h5")

def predict_emotion(face_img, model):
    face_img = cv2.resize(face_img, (48, 48))
    face_img = face_img.astype("float") / 255.0
    face_img = np.expand_dims(face_img, axis=0)
    face_img = np.expand_dims(face_img, axis=-1)

    predictions = model.predict(face_img)
    max_index = np.argmax(predictions[0])
    return emotion_labels[max_index], predictions[0][max_index]
