from flask import Flask,request
import numpy as np
import pandas as pd
import pickle

app = Flask(__name__)
pickle_in = open('classifier.pkl', 'rb')
classifer = pickle.load(pickle_in)

@app.route('/')
def welcome():
    return "welcome ALL"

@app.route('/predict')
def predict_note_authentication():

    variance = request.args.get("variance")
    skewness = request.args.get("skewness")
    curtosis = request.args.get("curtosis")
    entropy = request.args.get("entropy")
    prediction = classifer.predict([[variance, skewness,curtosis, entropy]])
    return "The prodicted value is " + str(prediction)
    

@app.route('/predict_file',methods=["POST"])
def predict_note_file():
    """Let's Authenticate the Banks Note 
    This is using docstrings for specifications.
    ---
    parameters:
      - name: file
        in: formData
        type: file
        required: true
      
    responses:
        200:
            description: The output values
        
    """
    df_test=pd.read_csv(request.files.get("file"))
    print(df_test.head())
    prediction=classifier.predict(df_test)
    
    return "The predicted value of text is " + str(list(prediction))



if __name__ == '__main__':
    app.run()