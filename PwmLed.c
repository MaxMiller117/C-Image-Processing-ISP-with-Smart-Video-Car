/**********************************************************************
* Filename    : pwmLed.c
* Description : Make a breathing led.
* Author      : Robot
* E-mail      : support@sunfounder.com
* website     : www.sunfounder.com
* Date        : 2014/08/27
**********************************************************************/

#include <wiringPi.h>
#include <stdio.h>

#define LedPin    1

int main(void)
{
	printf("Starting...\n");
	int i;

	if(wiringPiSetup() == -1){ //when initialize wiring failed,print messageto screen
		printf("setup wiringPi failed !");
		return 1; 
	}
	
	pinMode(LedPin, PWM_OUTPUT);//pwm output mode

	while(1){
		printf("First...\n");
		pwmWrite(LedPin, 400);
		delay(1000);
		printf("Second...\n");
		pwmWrite(LedPin, 500);
		delay(1000);
		//for(i=63;i<128;i++){
		//	printf("Testing: ");
		//	printf("%d", i);
		//	printf("\n");
		//	pinMode(i, PWM_OUTPUT);
		//	pwmWrite(i, 400);
		//	delay(1000);
		//	pwmWrite(i, 500);
		//	delay(1000);
		//}
		//delay(1000);
		//for(i=1023;i>=0;i--){
		//	pwmWrite(LedPin, i);
		//	delay(2);
		//}
	}

	return 0;
}

