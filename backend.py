import os
import requests
API_KEY = os.getenv("WEATHER_API")

def get_data(place="Tokyo", days=None, kind=None):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={place}" \
        f"&appid={API_KEY}"
    response = requests.get(url)
    data = response.json()
    return data


if __name__ == '__main__':
    print(get_data())