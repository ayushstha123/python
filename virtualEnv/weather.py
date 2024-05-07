import requests
from dotenv import load_dotenv  #helps us to get env variable
import os
from pprint import pprint


load_dotenv()

def get_current_weather():
    print("\n *** Get current weather condition ***\n")
    
    city=input("please enter a city name: \n")
    choose=input("Do you want your temp in F or C ?")
    if choose.lower() == 'f':
        request_url=f'https://api.openweathermap.org/data/2.5/weather?appid={os.getenv("API_KEY")}&q={city}&units=imperial'
    else:
        request_url=f'https://api.openweathermap.org/data/2.5/weather?appid={os.getenv("API_KEY")}&q={city}&units=metric'

    # print(request_url)
    weather_data=requests.get(request_url).json()
    # pprint(weather_data)

    print(f"Current Weather for {weather_data['name']}")
    print(f"The Temp is: {weather_data['main']['temp']}")
    print(f"Feels like : {weather_data['main']['feels_like']} and {weather_data['weather'][0]['description']}.\n")

if __name__ =="__main__":
    get_current_weather()