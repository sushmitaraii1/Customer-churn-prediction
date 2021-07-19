import os
import uvicorn
import pickle
from pydantic import BaseModel


from fastapi import FastAPI

app = FastAPI(title='Customer churn analysis', version='1.0',
              description='Testing')

LABELS = {"yes": 1, "no": 0}

def load_model():
    model = pickle.load(open("./models/customer_churn_prediction.pkl","rb"))
    return model

def tes_pipeline(query):
    model = load_model()
    prediction = model.predict(query)
    for key, value in LABELS.items():
        if value == prediction[0]:
            churn = key
    return churn


class Data(BaseModel):
    Account_Length:float
    Voicemail_Message:float
    Customer_Service_Calls:float
    International_Plan:float
    Day_Calls:float
    Day_Charge:float
    Evening_Calls:float
    Evening_Charge:float
    Night_Calls:float
    Night_Charge:float
    International_Calls:float
    International_Charge:float
    Area_Code:float



@app.get('/')
@app.get('/home')
def read_home():
    """
     Home endpoint which can be used to test the availability of the application.
     """
    return {'message': 'System is healthy'}

@app.post("/predict")
def predict(data: Data):
    data_dict = data.dict()
    values = list(data_dict.values())
    model = load_model()
    print(values)

    res = tes_pipeline(
        [values]
    )
    
    return {"res":res}


if __name__ == '__main__':
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)