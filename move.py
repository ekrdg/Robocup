import math
import time
from naoqi import ALProxy



def moveto(robotIP,temp,PORT=9559):
    motionProxy  = ALProxy("ALMotion", robotIP, PORT)
    postureProxy = ALProxy("ALRobotPosture", robotIP, PORT)

    # Wake up robot
    motionProxy.wakeUp()
    # Send robot to Pose Init
    postureProxy.goToPosture("StandInit", 0.5)
    #
    x     = 0.5
    #y     = 0.0
    theta = 0.0
    if temp > 0:
        temp = math.min(temp,30)
        theta = (math.pi/2)*(temp/30)
    else:
        temp = math.max(temp,-10)
        theta = (math.pi/2)*(temp/-10)
    time.sleep(5)
    
    motionProxy.moveto(0,0,theta)
    motionProxy.moveto(x,0,0)
    time.sleep(10)
    #Robot target destination
    motionProxy.moveto(0,0,math.pi)
    motionProxy.moveto(x,0,0)
    motionProxy.moveto(0,0,(math.pi-theta))


        


