import sys

from naoqi import ALProxy
from hello import hello
from microphone import get_audio
from weatherapi import weather as get_weather
from move import moveto as move_to

def main(robot_IP, robot_PORT=9559):
    hello(robot_IP, robot_PORT)
    tts = ALProxy("ALTextToSpeech", robot_IP, robot_PORT) 

    tts.say("Hello, ask me about the weather in any city. Are you ready?")
    get_confirmation("You said " + get_audio() + ". Is that correct?", tts)

    tts.say("Great! What city would you like to know the weather for?")
    city = get_audio()
    get_confirmation("You said " + city + ". Is that correct?", tts)

    tts.say("Great! I will now check the weather for " + city + ".")
    temperature = get_weather(city)
    tts.say("The weather in " + city + " is "+ temperature + " degrees celsius.")

    tts.say("Would you like me to visualize the weather in " + city + "?")
    visualization = get_audio()

    if visualization == "yes":
        tts.say("Great! I will now visualize the weather for " + city + ".")
        move_to(temperature)
    else:
        tts.say("Okay, I will not visualize the weather for " + city + ".")

    tts.say("Thank you for using the weather service. Have a great day!")


def get_confirmation(prompt, tts):
    tts.say(prompt)
    answer = get_audio()
    
    while answer != "yes":
        tts.say("I'm sorry, I didn't understand that. Please try again, for confirmation say yes, to end the program say stop.")
        if answer == "stop":
            tts.say("Goodbye!")
            sys.exit()
        answer = get_audio()
    return answer

      
if __name__ == "__main__":
    robot_IP = ""
    main(robot_IP)
