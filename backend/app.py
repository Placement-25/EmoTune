from flask import Flask, request, jsonify
from flask_cors import CORS
from pymongo import MongoClient
from model import detect_emotion
import cv2
import numpy as np
import os

app = Flask(__name__)
CORS(app)

client = MongoClient("mongodb://localhost:27017/")
db = client["emotune"]
logs = db["emotion_logs"]


@app.route('/analyze', methods=['POST'])
def analyze_emotion():
    file = request.files['image']
    img_bytes = np.frombuffer(file.read(), np.uint8)
    img = cv2.imdecode(img_bytes, cv2.IMREAD_COLOR)

    # Save temporarily for DeepFace
    temp_path = 'temp.jpg'
    cv2.imwrite(temp_path, img)

    try:
        emotion = detect_emotion(temp_path)
        logs.insert_one({"emotion": emotion})
        return jsonify({"emotion": emotion})
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    finally:
        os.remove(temp_path)


if __name__ == '__main__':
    app.run(debug=True)
