from naoqi import ALProxy
from weatherapi import weather
from stringtoresult import *
from move import moveto
import time

def main(robot_IP, robot_PORT=9559):
	# Connection robot
	tts = ALProxy("ALTextToSpeech", robot_IP, robot_PORT)
	record = ALProxy("ALAudioRecorder", robot_IP, robot_PORT)
	# start recording
	print('start recording...')#the input city 
	tts.say("I am listening")
	record_path = '/home/nao/record.wav'
	record.startMicrophonesRecording(record_path, 'wav', 16000, (0,0,1,0))
	time.sleep(15)
	record.stopMicrophonesRecording()
	#tts.say("record over")
	#print('record over')
	temp=weather(wavtotext(record_path))
	moveto(robot_IP,temp,robot_PORT)

      
if __name__ == "__main__":
    main()