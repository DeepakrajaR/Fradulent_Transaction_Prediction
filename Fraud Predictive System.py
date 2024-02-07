# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
import pickle

#loading the saved model
loaded_model = pickle.load(open('C:/Users/deepa/trained_model.sav', 'rb'))


# Define input_data as a list or array of numeric values
input_data = [1, 9839.64, 757869, 1662094, -9839.64, 0.0, 0, 0, 0, 1, 0]

# Rest of your code remains the same
input_data_as_numpy_array = np.asarray(input_data)
input_data_reshaped = input_data_as_numpy_array.reshape(1, -1)

# Assuming loaded_model is previously defined and trained
prediction = loaded_model.predict(input_data_reshaped)
print(prediction)

if prediction[0] == 0:
    print("It's a Fair Transaction, No fraud detected")
else:
    print("Fraudulent Transaction Detected!")
