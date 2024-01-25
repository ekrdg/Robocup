import requests
from kelvintocelsius import ktoc
BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"
CITY = "Berlin"
API_KEY = ""
URL = BASE_URL + "q=" + CITY + "&appid=" + API_KEY
response = requests.get(URL)
# checking the status code of the request
if response.status_code == 200:
   data = response.json()
   main = data['main']
   temperature = ktoc(main['temp'])
   humidity = main['humidity']
   pressure = main['pressure']
   feel = ktoc(main['feels_like'])
   weather_description = data['weather'][0]['description']
   print("The weather feels like {} !".format(feel))
   print("The weather temperature is {} !".format(temperature))
   print("The weather pressure {} !".format(pressure))
   print("The weather humidity {} !".format(humidity))
   print("The weather is {} !".format(weather_description))
   #The current weather in {city} is {weather_description} with a temperature of {temperature} Celsius
else:
   # showing the error message
   print("Error...")


