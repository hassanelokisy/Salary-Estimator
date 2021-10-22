import flask
from flask import Flask, jsonify, request
import json
import numpy as np 
import joblib

def load_pipeline():
    file_name = 'models/finalized_model.sav'
    with open(file_name, 'rb') as file :
        pipe = joblib.load(file)
    
    return pipe


app = Flask(__name__)
@app.route('/predict', methods=['GET'])
def predict():
    request_json = request.get_json()
    X = request_json['input']
    X = np.array(X).reshape(1. -1)
    pipe_line = load_pipeline()
    prediction = pipe_line.predict(X)[0]
    response = json.dumps({'response': prediction})
    return response, 200

if __name__ == '__main__':
    app.run(debug=True)
