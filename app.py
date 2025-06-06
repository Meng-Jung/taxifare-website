import streamlit as st
import requests

'''
# TaxiFareModel front
'''

st.markdown('''
Remember that there are several ways to output content into your web page...

Either as with the title by just creating a string (or an f-string). Or as with this paragraph using the `st.` functions
''')


date_time = st.text_input('date and time', '2014-07-06 19:18:00')

pickup_longitude = st.text_input('pickup_longitude', '-73.950655')

pickup_latitude = st.text_input('pickup_latitude', '40.783282')

dropoff_longitude = st.text_input('dropoff_longitude', '-73.984365')

dropoff_latitude = st.text_input('dropoff_latitude', '40.769802')

passenger_count = st.text_input('passenger_count', '2')



url = 'https://taxifare-119857604399.europe-west1.run.app/predict'
#url = 'https://taxifare.lewagon.ai/predict'

if url == 'https://taxifare.lewagon.ai/predict':

    st.markdown('Maybe you want to use your own API for the prediction, not the one provided by Le Wagon...')


# 2. Let's build a dictionary containing the parameters for our API...
params = {'pickup_datetime': date_time,
          'pickup_longitude': pickup_longitude,
          'pickup_latitude': pickup_latitude,
          'dropoff_longitude': dropoff_longitude,
          'dropoff_latitude': dropoff_latitude,
          'passenger_count': passenger_count}

#3. Let's call our API using the `requests` package...
response = requests.get(url, params = params)

#4. Let's retrieve the prediction from the **JSON** returned by the API...
if response.status_code == 200:
    # Success
    fare = response.json()  # or response.text, depending on the content
else:
    print("Request failed with status code:", response.status_code)

st.write('the prediction fare is', fare['fare'])
