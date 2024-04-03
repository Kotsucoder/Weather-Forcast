import os
import requests
API_KEY = os.getenv("WEATHER_API")

def get_data(place="Tokyo", days=3, kind="Temperature"):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={place}" \
        f"&appid={API_KEY}"
    response = requests.get(url)
    data = response.json()
    filtered_data = data["list"]
    values = 8 * days
    filtered_data = filtered_data[:values]
    if kind == "Temperature":
        filtered_data = [dict["main"]["temp"] for dict in filtered_data]
    if kind == "Sky":
        filtered_data = [dict["weather"][0]["main"] for dict in filtered_data]
    return filtered_data


if __name__ == '__main__':
    print(get_data())