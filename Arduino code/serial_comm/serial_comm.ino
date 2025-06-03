#include <Servo.h>
String serData;

Servo mys;
Servo mys1;

int servoPos = 90;
int servoPos1 = 90;



void setup() {
  Serial.begin(9600);
  Serial.println("Arduino is Ready");
  mys.attach(9);
  mys1.attach(10);
}


void loop() {

  while(1){
  if (Serial.available() > 0){
    char receive = Serial.read();

    Serial.println(receive);
    receive = "";

    switch(receive){
      //move the camera left
      case 'l':
        servoPos+=1;
        delay(20);
        if(servoPos > 180){
          servoPos = 180;
        }
        break;
      
      case 'r':
        servoPos-=1;
        delay(20);
        if(servoPos < 0){
          servoPos = 0;
        }
        break;
   
      case 'c':
        servoPos = 90;
        delay(20);
        break;
      
      case 'u':
        servoPos+=1;
        delay(20);
        if (servoPos1 > 180){
          servoPos1 = 180;
        }
        break;
      
      case 'd':
        servoPos1-=1;
        if (servoPos1 < 0){
          servoPos1 = 0;
        }
        break;
      mys.write(servoPos);
      mys1.write(servoPos1);
      receive = "";
      
    }
  }

}
}
