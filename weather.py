import os
from pprint import pprint

import requests
from dotenv import load_dotenv

load_dotenv()


def get_current_weather(city="Brampton"):
    request_url = f'http://api.openweathermap.org/data/2.5/weather?appid={os.getenv("API_KEY")}&q={city}&units=metric'
    weather_data = requests.get(request_url).json()
    return weather_data


if __name__ == "__main__":
    print("\n*** Get Current Weather Conditions ***\n")

    city = input("\nPlease enter a city name: ")

    # Check for empty strings or string with only spaces
    # This step is not required here
    # if not bool(city.strip()):
    #     city = "Kansas City"

    weather_data = get_current_weather(city)

    print("\n")
    pprint(weather_data)