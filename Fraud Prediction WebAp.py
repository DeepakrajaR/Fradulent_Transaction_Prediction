# -*- coding: utf-8 -*-
"""
Created on Thu Dec 14 16:29:17 2023

@author: deepa
"""

import numpy as np
import pickle
import streamlit as st

#loading the saved model
loaded_model = pickle.load(open('C:/Users/deepa/trained_model.sav', 'rb'))

#Creating a function for Prediction
def fraud_prediction(input_data):
    # Define input_data as a list or array of numeric values
    input_data = [1, 9839.64, 757869, 1662094, -9839.64, 0.0, 0, 0, 0, 1, 0]

    # Rest of your code remains the same
    input_data_as_numpy_array = np.asarray(input_data)
    input_data_reshaped = input_data_as_numpy_array.reshape(1, -1)

    # Assuming loaded_model is previously defined and trained
    prediction = loaded_model.predict(input_data_reshaped)
    print(prediction)

    if prediction[0] == 0:
        return "It's a Fair Transaction, No fraud detected"
    else:
        return "Fraudulent Transaction Detected!"
    

def main():
    
    # Title
    st.title('Fraudulent Transaction Predicion')
    									
    #getting user input
    step = st.text_input('Number of hours')
    amount = st.text_input('Amount')
    nameOrig = st.text_input('Sender')
    nameDest = st.text_input('Receiver')
    balanceChangeOrig = st.text_input('New balance after transfer')
    balanceChangeDest = st.text_input('New balance post deposit')
    type_CASH_IN = st.text_input('Cash in')
    type_CASH_OUT = st.text_input('Cash Out')
    type_DEBIT = st.text_input('Debit')
    type_PAYMENT = st.text_input('Payment')
    type_TRANSFER = st.text_input('Transfer')
    
    #code for prediction
    prediction = ''
    
    
    if st.button('Prediction Result'):
        prediction = fraud_prediction([step, amount, nameOrig, nameDest, balanceChangeOrig, balanceChangeDest, type_CASH_IN, type_CASH_OUT, type_DEBIT, type_PAYMENT, type_TRANSFER])
        
    st.success(prediction)
    
    
if __name__ == '__main__':
    main()