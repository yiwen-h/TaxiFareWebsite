import streamlit as st
import requests
import datetime

url = 'https://taxifare.lewagon.ai/predict'
st.title('Welcome to the Le Wagon taxi fare predictor')

passenger_count = st.number_input('Number of passengers', max_value=8 )
pickup_latitude = st.text_input('Start latitude')
pickup_longitude = st.text_input('Start longitude')
dropoff_latitude = st.text_input('End latitude')
dropoff_longitude = st.text_input('End longitude')
pickup_date = st.date_input('pickup_date')
pickup_time = st.time_input('pickup_time')


click = st.button('SUBMIT')

if click:
    params_dict = {"pickup_longitude": pickup_longitude,
                "pickup_latitude": pickup_latitude,
                "dropoff_longitude":dropoff_longitude,
                "dropoff_latitude": dropoff_latitude,
                "pickup_datetime": f"{pickup_date} {pickup_time}",
                "passenger_count": passenger_count}
    response = requests.get(url = url, params = params_dict)
    response = response.json()
    fare = str(round(response['fare'],2))
    st.subheader(f'Your fare should be $ {fare}')
else:
    st.write('Please enter the required information')
