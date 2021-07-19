import os
import streamlit
import requests
import json

def run():
    streamlit.title("Customer Churn prediction")
    Account_Length = streamlit.text_input("Account Length")
    Voicemail_Message = streamlit.text_input("Voicemail_Message")
    Customer_Service_Calls = streamlit.text_input("Customer_Service_Calls")
    International_Plan = streamlit.text_input("International_Plan")
    Day_Calls = streamlit.text_input("Day_Calls")
    Day_Charge = streamlit.text_input("Day_Charge")
    Evening_Calls = streamlit.text_input("Evening_Calls")
    Evening_Charge = streamlit.text_input("Evening_Charge")
    Night_Calls = streamlit.text_input("Night_Calls")
    Night_Charge = streamlit.text_input("Night_Charge")
    International_Calls = streamlit.text_input("International_Calls")
    International_Charge = streamlit.text_input("International_Charge")
    Area_Code = streamlit.text_input("Area_Code")


    data = {
        'Account_Length':Account_Length,
        'Voicemail_Message':Voicemail_Message,
        'Customer_Service_Calls':Customer_Service_Calls,
        'International_Plan':International_Plan,
        'Day_Calls':Day_Calls,
        'Day_Charge':Day_Charge,
        'Evening_Calls':Evening_Calls,
        'Evening_Charge':Evening_Charge,
        'Night_Calls':Night_Calls,
        'Night_Charge':Night_Charge,
        'International_Calls':International_Calls,
        'International_Charge':International_Charge,
        'Area_Code':Area_Code,
    
    }

    if streamlit.button("Predict"):

        #servicename:port_address/endpoint for docker
            response = requests.post("http://localhost:8000/predict", json=data)
            prediction =response.text
            streamlit.success(f"The prediction from model: {prediction}")

if __name__ == '__main__':
    run()