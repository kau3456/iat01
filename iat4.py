import requests

API_KEY = '937fcd0a53c764546c1b809467945075'
BASE_URL = 'https://api.openweathermap.org/data/2.5/weather'
UNITS = 'metric'

def get_weather_data(city_name):
    params = {'q': city_name, 'appid': API_KEY, 'units': UNITS}
    response = requests.get(BASE_URL, params=params)
    if response.status_code == 200:
        data = response.text
        return data
    else:
        return None

def display_weather_data(data):
    if data:
        print("Weather Data:")
        print(data)
    else:
        print("City not found or an error occurred.")

def wlc():
    print("Welcome to the Weather App!")
    while True:
        city_name = input("Enter the city name (or 'exit' to quit): ")
        if city_name.lower() == 'exit':
            print("Goodbye!")
            break
        data = get_weather_data(city_name)
        display_weather_data(data)
wlc()
