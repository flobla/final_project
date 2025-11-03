"""Emotion Detection"""
import json
import requests  # Import the requests library to handle HTTP requests

def emotion_detector(text_to_analyse):
    """ emotion_detector that takes a string input"""
    url = 'https://sn-watson-emotion.labs.skills.network/v1/'\
        'watson.runtime.nlp.v1/NlpService/EmotionPredict'
     # Create a dictionary with the text to be analyzed
    myobj = { "raw_document": { "text": text_to_analyse } }
    # Set the headers required for the API request
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    # Sending a POST request to the sentiment analysis API
    response = requests.post(url, json=myobj, headers=header,timeout=5)
    if response.status_code == 400: 
        return {
             'anger': None,
             'disgust': None,
             'fear': None,
             'joy': None,
             'sadness': None,
             'dominant_emotion': None
        }
    formatted_response = json.loads (response.text)
    emotion_scores = formatted_response['emotionPredictions'][0]['emotion']
    dominant_emotion = max(emotion_scores, key=emotion_scores.get)
    emotion_scores['dominant_emotion'] = dominant_emotion
    return emotion_scores