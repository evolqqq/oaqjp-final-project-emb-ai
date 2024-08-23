import requests

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    input= {"raw_document": {"text": text_to_analyze}}
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    try:
        response = requests.post(url, headers=headers, json=input)
        if response.status_code == 200:
            data = response.json()
            if 'emotionPredictions' in data:
                emotion_scores = data['emotionPredictions'][0]['emotion']
                
                anger_score = emotion_scores.get('anger', 0)
                disgust_score = emotion_scores.get('disgust', 0)
                fear_score = emotion_scores.get('fear', 0)
                joy_score = emotion_scores.get('joy', 0)
                sadness_score = emotion_scores.get('sadness', 0)
                dominant_emotion = max(emotion_scores, key=emotion_scores.get)
            else:
                return {
                    'anger': "None",
                    'disgust': "None",
                    'fear': "None",
                    'joy': "None",
                    'sadness': "None",
                    'dominant_emotion': "None"
                }
        else:
            return {
                'anger': "None",
                'disgust': "None",
                'fear': "None",
                'joy': "None",
                'sadness': "None",
                'dominant_emotion': "None"
            }
    except requests.exceptions.RequestException as e:
        # Handle network-related errors
        print(f"Request error: {e}")
        return {
            'anger': "Error",
            'disgust': "Error",
            'fear': "Error",
            'joy': "Error",
            'sadness': "Error",
            'dominant_emotion': "Error"
        }
    return {
        'anger': anger_score,
        'disgust': disgust_score,
        'fear': fear_score,
        'joy': joy_score,
        'sadness': sadness_score,
        'dominant_emotion': dominant_emotion
    }
