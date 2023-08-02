import requests

API_KEY = "********************" #insert your own api key here. 
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

city = input("Enter a city name: ")
request_url = f"{BASE_URL}?appid={API_KEY}&q={city}"
response = requests.get(request_url)

if response.status_code == 200:
    data = response.json()
    weather = data['weather'][0]['description']
    temperature_kelvin = data["main"]["temp"]
    
    # Convert the temperature from Kelvin to Fahrenheit
    temperature_fahrenheit = round((temperature_kelvin - 273.15) * 9/5 + 32, 2)

    print("Weather:", weather)
    print("Temperature:", temperature_fahrenheit, "Fahrenheit")
else:
    print("An error occurred.")
