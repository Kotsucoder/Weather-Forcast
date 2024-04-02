import streamlit as st
import plotly.express as px
from backend import get_data

st.title("Weather Forecast for the Next Days")
place = st.text_input("Place: ")
days = st.slider("Forecast Days", min_value=1, max_value=5, 
                 help="Select the number of forecasted days")
option = st.selectbox("Select data to view", ("Temperature", "Sky"))
st.subheader(f"{option} for the next {days} days in {place}")

data = get_data(place, days, option)

dates = ["2005-10-24", "2005-10-25", "2005-10-26"] # Placeholder
temperatures = [200, 300, 400] # Placeholder
labels = {"x": "Date", "y": "Temperature (C)"}

figure = px.line(x=dates, y=temperatures, labels=labels)
st.plotly_chart(figure)