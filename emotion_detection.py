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
    return textToReturn