import requests

def get_weather(api_key, city):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': city,
        'appid': api_key,
    }

    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()
        weather_data = response.json()

        # Extracting relevant information from the response
        main_weather = weather_data['weather'][0]['main']
        description = weather_data['weather'][0]['description']
        temperature = weather_data['main']['temp']

        print(f"Weather in {city}: {main_weather} ({description})")
        print(f"Temperature: {temperature}°C")

    except requests.exceptions.RequestException as e:
        print(f"Error fetching weather data: {e}")

# Replace 'your_api_key' with the actual API key you obtained from OpenWeatherMap
api_key = 'aa8cbb89185458bd79335ed1dddccd4a'
city = 'Bangalore'

get_weather(api_key, city)



