# -*- coding: utf-8 -*-
"""
Created on Mon Apr 22 12:56:37 2024

@author: Harsh Yadav
"""

import numpy as np
import pickle
import streamlit as st

#loading the saved model
loaded_model = pickle.load(open('C:/Users/Harsh Yadav/Machine Learning/trained_model.sav','rb'))

# creating a functioon for prediction
def parkinsons_prediction(input_data):
    input_data = (197.07600,206.89600,192.05500,0.00289,0.00001,0.00166,0.00168,0.00498,0.01098,0.09700,0.00563,0.00680,0.00802,0.01689,0.00339,26.77500,0.422229,0.741367,-7.348300,0.177551,1.743867,0.085569)

# changing input data to a numpy array
    input_data_as_numpy_array = np.asarray(input_data)

# reshape the numpy array
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)



    prediction = loaded_model.predict(input_data_reshaped)
    print(prediction)


    if (prediction[0] == 0):
     return 'The Person does not have Parkinsons Disease'

    else:
     return 'The Person has Parkinsons'

def main():
    # Customizing the background color using CSS
    st.markdown("""
       <style>
           .stApp {
               background-color: #d3d3d3; /* Change this value to your desired background color */
           }
       </style>
   """, unsafe_allow_html=True)
    
    # giving a title
    st.title('Parkinson prediction web app')
    
   
    MDVPFo = st.text_input('Average vocal fundamental frequency')
    MDVPFhiHz = st.text_input('Maximum vocal fundamental frequency')
    MDVPFloHz = st.text_input('Minimum vocal fundamental frequency')
    MDVPJitterpercent = st.text_input('MDVP:Jitter(%)')
    MDVPJitterAbs= st.text_input('MDVP:Jitter(Abs)')
    MDVPRAP= st.text_input('MDVP:RAP')
    MDVPPPQ= st.text_input('MDVP:PPQ')
    JitterDDP=st.text_input('Jitter:DDP')
    MDVPShimmer= st.text_input('MDVP:Shimmer')
    MDVPShimmerdB= st.text_input('MDVP:Shimmer(dB)')
    ShimmerAPQ3= st.text_input('Shimmer:APQ3')
    ShimmerAPQ5= st.text_input('Shimmer:APQ5')
    MDVPAPQ=st.text_input('MDVP:APQ')
    ShimmerDDA= st.text_input('Shimmer:DDA')
    NHR= st.text_input('measures of ratio of noise to tonal components in the voice(NHR)')
    HNR= st.text_input('measures of ratio of noise to tonal components in the voice(HNR)')
    RPDE= st.text_input('nonlinear dynamical complexity measure(RPDE)')
    DFA= st.text_input('Signal fractal scaling exponent')
    spread1= st.text_input('Spread1')
    spread2= st.text_input('Spread2')
    D2= st.text_input('nonlinear dynamical complexity measures(D2)')
    PPE= st.text_input('PPE')
    
    
    # code for Prediction
    diagnosis = ''
    
    # creating a button for Prediction
    
    if st.button('Parkinson disease detection'):
        diagnosis = parkinsons_prediction([MDVPFo,MDVPFhiHz,MDVPFloHz,MDVPJitterpercent,MDVPJitterAbs,MDVPRAP,MDVPPPQ,JitterDDP,MDVPShimmer,MDVPShimmerdB,ShimmerAPQ3,ShimmerAPQ5,MDVPAPQ,ShimmerDDA,NHR,HNR,RPDE,DFA,spread1,spread2,D2,PPE
])
        
        
    st.success(diagnosis)
    
    
    
if __name__ == '__main__':
      main()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    