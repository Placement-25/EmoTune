from deepface import DeepFace


def detect_emotion(image_path):
    result = DeepFace.analyze(img_path=image_path, actions=['emotion'])
    return result[0]['dominant_emotion']
