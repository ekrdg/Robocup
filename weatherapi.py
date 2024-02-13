import requests

def weather(city):
   BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"
   CITY = city
   API_KEY = "dbffce0cff16f827c0f09a55df8d6424"
   URL = BASE_URL + "q=" + CITY + "&appid=" + API_KEY
   response = requests.get(URL)
   # checking the status code of the request
   if response.status_code == 200:
      data = response.json()
      main = data['main']
      temperature = ktoc(main['temp'])
      return temperature
   else:
      # showing the error message
      return ("Error...")
   
def ktoc(value):
    c = value - 273.15 
    return int(round(c))