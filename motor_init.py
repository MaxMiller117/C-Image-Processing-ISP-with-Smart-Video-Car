#!/usr/bin/env python
import RPi.GPIO as GPIO
import video_dir
import car_dir
import motor
from socket import *
from time import ctime          # Import necessary modules
import numpy as np
import argparse
import cv2
import subprocess   
import time

##video_dir.setup()
car_dir.setup()
motor.setup()     # Initialize the Raspberry Pi GPIO connected to the DC motor. 
##video_dir.home_x_y()
#car_dir.home()

motor.setSpeed(50)
xCent = 310 #175
yCent = 143
closeEnough = 100
offDir = 0



while False:
	###subprocess.call("/home/pi/Sunfounder_Smart_Video_Car_Kit_for_RaspberryPi/server/takeImage.sh")
	#time.sleep(0.1)	

	###ap = argparse.ArgumentParser()
	###ap.add_argument("-i", "--image", help = "/image.jpg")
	###args = vars(ap.parse_args())
	###image = cv2.imread(args["image"])
	video_capture = cv2.VideoCapture(0)
	ret_val, image = video_capture.read()
	del(video_capture)
	
	#image = cv2.imread("/image.jpg")
	boundaries = [([0, 0, 130], [80, 80, 255])]  #Should be red [17,15,100]-[50,56,200]
	for (lower, upper) in boundaries:
		lower = np.array(lower, dtype = "uint8")
		upper = np.array(upper, dtype = "uint8")
		mask = cv2.inRange(image, lower, upper)
		output = cv2.bitwise_and(image, image, mask = mask)
		#cv2.imshow("images", np.hstack([image, output]))
		#cv2.waitKey(0)


	if cv2.countNonZero(mask) > 500:
		moments = cv2.moments(mask,1)
		xAvg = moments['m10']/moments['m00']
		yAvg = moments['m01']/moments['m00']
		print str(xAvg) + " " + str(yAvg) + " " + str(xAvg - closeEnough)
		if xAvg < 150:
			print 'Leaving left?'
			offDir = -1
		elif xAvg > (620 - 150):
			print 'Leaving right?'
			offDir = 1
		if xAvg < (xCent - closeEnough):
			print 'Turning left'
			car_dir.turn_left()
			motor.forward()
			#Turn left
		elif xAvg > (xCent + closeEnough):
			print 'Turning right'
			car_dir.turn_right()
			motor.forward()
			#Turn right
		else:
			print 'Going straight'
			car_dir.home()
			motor.forward()
	else:
		print 'Nothing found'
		if(offDir < 0):
			print 'Finding target left'
			car_dir.turn_right()
			motor.backward()
			time.sleep(0.75)
		elif(offDir > 0):
			print 'Finding target right'
			car_dir.turn_left()
			motor.backward()
			time.sleep(0.75)
		offDir = 0
		motor.ctrl(0)
		car_dir.home()

