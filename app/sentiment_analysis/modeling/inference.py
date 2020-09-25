# import tensorflow as tf
# from tensorflow.keras.preprocessing.sequence import pad_sequences
import os
import json
import requests

result = {
    0: "Negative",
    1: "Positive"
}

def infer_sentiment(input_string):
    try:
        model_dir = os.path.dirname(os.path.abspath(__file__))

        with open(os.path.join(model_dir,"config.json"),'r') as f:
            model_config = json.load(f)

        model_folder = model_config['model_folder']
        model_version = model_config['serving_version']
        model_path = os.path.join(model_dir,model_folder,model_version)

        #loading the tokenizer
        with open(os.path.join(model_path,"tokenizer.json"),"r") as f:
            tokenizer_json = json.load(f)
        
        tokenizer = tf.keras.preprocessing.text.tokenizer_from_json(tokenizer_json)

        #preprocessing the input string
        preprocessed_string = pad_sequences(tokenizer.texts_to_sequences([input_string]),maxlen=200,truncating='post',padding='pre')
        preprocessed_json = {
            "instances": preprocessed_string.tolist()
        }


        #predicting using the model served by TFServing
        #model predicting code

        response = requests.post(url="http://tfxserving:8501/v1/models/cnn:predict",json=preprocessed_json)

        if response.status_code != 200:
            raise Exception(f"Invalid status code: {response.status_code}")
        prediction_json = json.loads(response.content)
        
        return result[int(round(prediction_json['predictions'][0][0]))]


    except Exception as e:
        raise Exception(e)