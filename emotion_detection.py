import requests
import json

def output_formatter(r):
    formatted_response = json.loads(r)
    anger_score     = formatted_response['emotionPredictions']['emotion']['anger']
    disgust_score   = formatted_response['emotionPredictions']['emotion']['disgust']
    fear_score      = formatted_response['emotionPredictions']['emotion']['fear']
    joy_score       = formatted_response['emotionPredictions']['emotion']['joy']
    sadness_score   = formatted_response['emotionPredictions']['emotion']['sadness']

    value_to_key = {
        anger_score: "anger",
        disgust_score: "disgust",
        fear_score: "fear",
        joy_score: "joy",
        sadness_score: "sadness"
    }

    dominant_score = max([anger_score, disgust_score, fear_score, joy_score, sadness_score])

    output = {
        'anger'             : anger_score,
        'disgust'           : disgust_score,
        'fear'              : fear_score,
        'joy'               : joy_score,
        'sadness'           : sadness_score,
        'dominant_emotion'  : value_to_key[dominant_score]
    }

    return output

def emotion_detector(text_to_analyze: str) -> dict:
    url = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
    input_json = { "raw_document": { "text": text_to_analyze } }
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    response = requests.post(url, json=input_json, headers=headers)
    out = output_formatter(response.text)
    return out

if __name__ == "__main__":
    print(emotion_detector("I love this new technology."))
