import requests #Importa la libreria requests per gestire le richieste HTTP
import json
def emotion_detector(text_to_analyze):
    #URL del servizio di Emotion Predic
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input_json = { "raw_document": { "text": text_to_analyze } }
    #Invio una POST all'API per la Emotion Predict
    response = requests.post(url, json=input_json, headers=header)
    formatted_response=json.loads(response.text)
    emotionText=formatted_response['emotionPredictions']
    emotionMentions=formatted_response['emotionPredictions'][0]['emotionMentions']
    #print (emotionMentions)
    textToReturn=emotionMentions[0]['span']['text']
    emotionList=formatted_response['emotionPredictions'][0]['emotion']
    anger_score=emotionList['anger']
    disgust_score=emotionList['disgust']
    fear_score=emotionList['fear']
    joy_score=emotionList['joy']
    sadness_score=emotionList['sadness']
    #Cerca il massimo
    dominant_emotion='anger'
    dominant_value=anger_score
    if (disgust_score > dominant_value):
        dominant_value = disgust_score
        dominant_emotion = 'disgust'
    if (fear_score > dominant_value):
        dominant_value = fear_score
        dominant_emotion = 'fear'
    if (joy_score > dominant_value):
        dominant_value = joy_score
        dominant_emotion = 'joy'
    if (sadness_score > dominant_value):
        dominant_value = sadness_score
        dominant_emotion = 'sadness'
    return {
        'anger': anger_score, 
        'disgust': disgust_score, 
        'fear': fear_score, 
        'joy': joy_score, 
        'sadness': sadness_score, 
        'dominant_emotion': dominant_emotion
        }