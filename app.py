# app structure from https://www.analyticsvidhya.com/blog/2020/12/deploying-machine-learning-models-using-streamlit-an-introductory-guide-to-model-deployment/
 
import pickle
import math
import streamlit as st
from utils import *

pipe = pickle.load(open('finalized_model.sav', 'rb'))

# @st.cache()
  
# defining the function which will make the prediction using the data which the user inputs 
def prediction(timestamp, t1, t2, hum, wind_speed, weather_code, is_holiday, weekend, season):   
 
    # Pre-processing user input  
   
    # Weather codes taken from Kaggle dataset definition
    if weather_code == "Clear":
        weather_code = 1.0
    elif weather_code == "Scattered Clouds":
        weather_code = 2.0
    elif weather_code == "Broken Clouds":
        weather_code = 3.0
    elif weather_code == "Cloudy":
        weather_code = 4.0
    elif weather_code == "Light Rain":
        weather_code = 7.0
    elif weather_code == "Thunderstorm":
        weather_code = 10.0
    elif weather_code == "Snowfall":
        weather_code = 26.0
    elif weather_code == "Freezing Fog":
        weather_code = 94.0
 
    if is_holiday == "True":
        is_holiday = 1.0
    else:
        is_holiday = 0.0
    
    if weekend == "True":
        weekend = 1.0
    else:
        weekend = 0.0
    
    if season == "Spring":
        season = 0.0
    elif season == "Summer":
        season = 1.0
    elif season == "Fall":
        season = 2.0
    elif season == "Winter":
        season = 3.0
 
 
    # Making predictions 
    
    df = pd.DataFrame(columns=['timestamp', 't1', 't2', 'hum', 'wind_speed', 'weather_code',
       'is_holiday', 'is_weekend', 'season'])
    df.loc[0] = [timestamp, t1, t2, hum, wind_speed, weather_code, is_holiday, weekend, season]
    prediction = pipe.predict(df) 
    return math.floor(prediction[0])
      
  
def main():       
    # front end elements of the web page 
    html_temp = """ 
    <div style ="background-color:#a2d4fc;padding:13px"> 
    <h1 style ="color:black;text-align:center;">London Bike ML Prediction App</h1> 
    </div> 
    """
      
    # display the front end aspect
    st.markdown(html_temp, unsafe_allow_html = True) 
      
    # following lines create boxes in which user can enter data required to make prediction 
    timestamp = st.date_input('Date')
    t1 = st.number_input("Tempurature (Celsius)")
    t2 = st.number_input("Tempurature 'feels like' (Celsius)") 
    hum = st.number_input("Humidity %")
    wind_speed = st.number_input("Wind Speed km/h")
    weather_code = st.selectbox("Weather Code",("Clear", "Scattered Clouds", "Broken Clouds", "Cloudy",
                                               "Light Rain", "Thunderstorm", "Snowfall", "Freezing Fog"))
    is_holiday = st.selectbox("Holiday?",("True", "False"))
    weekend = st.selectbox("Weekend?",("True", "False"))
    season = st.selectbox("Season", ("Spring", "Summer", "Fall", "Winter"))
    result =""
      
    # when 'Predict' is clicked, make the prediction and store it 
    if st.button("Predict"): 
        result = prediction(timestamp, t1, t2, hum, wind_speed, weather_code, is_holiday, weekend, season)
        st.success('The model predicts that {} bikes will be rented in London on this day!'.format(result))
     
if __name__=='__main__': 
    main()