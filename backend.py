import os
import requests
API_KEY = os.getenv("WEATHER_API")

def get_data(place="Tokyo", days=3):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={place}" \
        f"&appid={API_KEY}"
    response = requests.get(url)
    data = response.json()
    filtered_data = data["list"]
    values = 8 * days
    filtered_data = filtered_data[:values]
    return filtered_data


if __name__ == '__main__':
    print(get_data())