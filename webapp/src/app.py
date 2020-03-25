from flask import Flask
from flask import request

import pandas as pd
from joblib import load
import numpy as np

app = Flask(__name__)
model = load('model.joblib')

@app.route('/')
def predict():
    # Request.args is itself a dictionary of key -> scalar_value. 
    # However, it needs to be reshaped into key -> [scalar_value] 
    # before being converted to a Pandas dataframe.
    X = dict()
    defaults = {"startYear": -1, "runtimeMinutes": -1, "directorAverage": -1, 
                "writerAverage": -1, "principalAverage": -1, "isAction": 0, 
                "isAdult": 0, "isAdventure": 0, "isAnimation": 0, "isBiography": 0, "isComedy": 0, 
                "isCrime": 0, "isDocumentary": 0, "isDrama": 0, "isFamily": 0, "isFantasy": 0, 
                "isFilm-Noir": 0, "isGame-Show": 0, "isHistory": 0, "isHorror": 0, "isMusic": 0, 
                "isMusical": 0, "isMystery": 0, "isNews": 0, "isReality-TV": 0, "isRomance": 0, 
                "isSci-Fi": 0, "isShort": 0, "isSport": 0, "isTalk-Show": 0, "isThriller": 0, 
                "isWar": 0, "isWestern": 0} 

    missing_fields = list()

    # The "defaults" dictionary stores mappings from each expected feature to the default value.
    # For each expected feature (a key in "defaults",) 
    # the program would see if it can find that feature in request. 
    # If an expected field is missing, the backend would look for it in default.
    # If the default for that feature is -1 (implies required field,) 
    # the program shall take note of that. 
    # It would eventually return a bad request code and explain what fields are missing.
    for key in defaults.keys():
        if key not in request.args.keys() or request.args[key] == "":
            if defaults[key] == -1:
                missing_fields.append(key)
            else:
                X[key] = [defaults[key]]
        
        else: # Convert on-off to binary manually.
            if request.args[key] == "on":
                X[key] = [1]
            else:
                X[key] = [request.args[key]]

    X_df = pd.DataFrame.from_dict(X)

    if len(missing_fields) != 0:
        return {"message": 
                "This API requires the following feature(s) but could not find them in your GET request.", 
                "missing_fields": missing_fields}, 400
       
    raw_prediction = model.predict(X_df)
    prediction = np.argmax(raw_prediction)

    if prediction == 1:
        message_text = "Above average."        
    elif prediction == 0:
        message_text = "Below average."
    else:
        return {"message": 
                "Got unexpected response from model.predict." 
                + "You might need to update the message logic to reflect outcomes of your model.", 
                "rawOutcome": raw_prediction}, 500

    return {"message": message_text}, 200