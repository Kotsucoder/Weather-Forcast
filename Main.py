import streamlit as st
import plotly.express as px
from backend import get_data

st.title("Weather Forecast for the Next Days")
place = st.text_input("Place: ", value="Tokyo")
days = st.slider("Forecast Days", min_value=1, max_value=5, 
                 help="Select the number of forecasted days")
option = st.selectbox("Select data to view", ("Temperature", "Sky"))
st.subheader(f"{option} for the next {days} days in {place}")

try:
    filtered_data = get_data(place, days)

    labels = {"x": "Date", "y": "Temperature (C)"}

    if option == "Temperature":
        temperatures = [dict["main"]["temp"] / 10 for dict in filtered_data]
        dates = [dict["dt_txt"] for dict in filtered_data]
        figure = px.line(x=dates, y=temperatures, labels=labels)
        st.plotly_chart(figure)

    if option == "Sky":
        sky_conditions = [dict["weather"][0]["main"] for dict in filtered_data]
        image_paths = {
            "Clear": "images/clear.png",
            "Clouds": "images/cloud.png",
            "Rain": "images/rain.png",
            "Snow": "images/snow.png"
        }
        images = [image_paths[condition] for condition in sky_conditions]
        st.image(images, width=115)
except KeyError:
    st.write("This place does not exist.")