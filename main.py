import sys

from naoqi import ALProxy
from hello import hello
from speechtest import *
from weatherapi import weather as get_weather
from move import *
from stretch import *

def main():
    IP = "nao6.local"
    PORT = 9559
    tts = ALProxy("ALTextToSpeech", IP, PORT) 
    #text = "world"
    #tts.say("Hello "+text)
    hello(IP,PORT)
    tts.say("Hello, ask me about the weather in any city. Are you ready?")
    tts.say("Great! What city would you like to know the weather for?")
    a = get_audio()
    city = recognize_speech(a)
    #get_confirmation("Please say yes to confirm your answer")

    tts.say("Great! I will now check the weather for "+ str(city))
    temperature = get_weather(city)
    tts.say("The weather in " + str(city) + " is "+ str(temperature) + " degrees celsius")
    
    tts.say("Would you like me to visualize the weather in " + str(city))
    input = get_audio()
    answer = recognize_speech(input)

    if answer == "yes":
        tts.say("Great! I will now visualize the weather for " + str(city))
        #point_to_city(city)
        move_to(temperature)
    else:
        tts.say("Okay, I will not visualize the weather for " + str(city) + ".")
        tts.say("Thank you for using the weather service. Have a great day!")


def get_confirmation(prompt):
    print(prompt)
    input = get_audio()
    answer = recognize_speech(input)
    if answer =="yes":
        print("you said yes")
    if answer == "no":
        #print("I'm sorry, I didn't understand that. Please try again, for confirmation say yes, to end the program say stop.")
        print("You said no")
    if answer == "stop":
        print("Goodbye!")
        sys.exit()

      
if __name__ == "__main__":
    main()
