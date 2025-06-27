# Emotion Detector (Flask + Webcam + CNN)

This is a real-time facial **Emotion Detection System** built using:
- Python
- Flask (for web interface)
- OpenCV (for webcam input)
- Keras/TensorFlow (for deep learning model)
- Trained on [FER2013 dataset](https://www.kaggle.com/datasets/msambare/fer2013)


----

## 🎯 Detected Emotions

- 😠 Angry
- 😢 Sad
- 😐 Neutral
- 😄 Happy
- 😨 Fear
- 🤢 Disgust
- 😲 Surprise

---

## 🧠 Tech Stack

- **Frontend**: HTML + CSS (Bootstrap)
- **Backend**: Flask (Python)
- **Deep Learning**: CNN trained on FER2013
- **Webcam**: Live webcam via OpenCV

---
<details>
## 🧰 Project Structure
emotion-detector/
├── app.py                # 🔥 Flask web app
├── camera.py             # 🎥 Webcam + emotion prediction logic
├── utils.py              # 🧠 Model loading & image preprocessing
├── train_model.py        # 🏋️ Train CNN model using FER2013 dataset
│
├── fer2013/              # 📂 Dataset directory (from Kaggle)
│   ├── train/
│   │   ├── angry/
│   │   ├── happy/
│   │   ├── ...
│   └── test/
│       ├── sad/
│       ├── surprise/
│       └── ...
│
├── model/
│   └── emotion_model.h5  # ✅ Trained CNN model file
│
├── templates/
│   └── index.html        # 🖼️ Web UI (HTML with webcam feed)
│
├── static/
│   └── styles.css        # 🎨 Custom styling
│
├── requirements.txt      # 📦 Python dependencies
└── README.md             # 📘 Project overview and instructions
</details>

---
emotion-detector/fer2013/train/
emotion-detector/fer2013/test/
---

## 📥 Setup Instructions

### 1. Clone the Repo

```bash
git clone https://github.com/your-username/emotion-detector-flask-cnn.git
cd emotion-detector-flask-cnn
```

## 📦 Requirements

Install via pip:

```bash
pip install -r requirements.txt
```
## Train the model - outputs model/emotion_model.h5
```bash
python train_model.py
```

## Run App
```bash
python app.py
```
Open http://localhost:5000 in your browser to use it!

##  Future Enhancements

Save emotion history per user
Display emoji overlay instead of text
Add age/gender estimation
Deploy on Render/Heroku


---

## 🛠️ .gitignore

```gitignore
__pycache__/
*.pyc
model/
fer2013/
venv/
.env
*.h5
*.csv
.DS_Store
