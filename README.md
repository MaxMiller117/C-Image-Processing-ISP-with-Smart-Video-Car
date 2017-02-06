# C-Image-Processing-ISP-with-Smart-Video-Car
Requirements:
opencv 3.2.0
wiringPi

All files are based off of and use files from two projects:
https://github.com/sunfounder/Sunfounder_Smart_Video_Car_Kit_for_RaspberryPi
https://github.com/sunfounder/Sunfounder_SuperKit_C_code_for_RaspberryPi

motor_init.py "/home/pi/Sunfounder_Smart_Video_Car_Kit_for_RaspberryPi/server/motor_init.py"
This initializes the motors for use in other programs.

motor_test.py "/home/pi/Sunfounder_Smart_Video_Car_Kit_for_RaspberryPi/server/motor_test.py"
This code is run on startup through rc.local. The Pi will search for a red object and head towards it. If it stops seeing the red object it will reverse and turn towards where it last saw it.

rc.local "/etc/rc.local"
This is the startup file for the RaspberryPi. This us to run our programs just by turning the Pi on.

motor.c "/home/pi/Sunfounder_SuperKit_C_code_for_RaspberryPi/07_Motor/motor.c"
This is a test file for the c motor drivers.
Compile using "gcc -o motor motor.c -lwiringPi"
Run using "./motor"

PwmLed.c "/home/pi/Sunfounder_SuperKit_C_code_for_RaspberryPi/04_PwmLed/PwmLed.c"
This is a test file for using pwm to drive the servos. It currently does not work but checks all ports for servos. The program seems to crash on ports 1, 23, 24, and 26.
