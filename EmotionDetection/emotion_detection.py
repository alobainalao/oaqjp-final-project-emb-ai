import requests
import json

def emotion_detector(text_to_analyse):
    # Define the URL for the sentiment analysis API
    url ='https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'

    # Create the payload with the text to be analyzed
    myobj = { "raw_document": { "text": text_to_analyse } }

    # Set the headers with the required model ID for the API
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}

    # Make a POST request to the API with the payload and headers
    response = requests.post(url, json=myobj, headers=header)

    # Check if the response status code is 400 (Bad Request)
    if response.status_code == 400:
        # Return a dictionary with None values for all keys if there's a Bad Request error
        return { 
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }

    # Parse the response from the API
    emotions = json.loads(response.text)['emotionPredictions'][0]['emotion']
    dominant_emotion = max(emotions, key=emotions.get)
    emotions['dominant_emotion'] = dominant_emotion

    return emotions
