#include<Servo.h>
String serData;

Servo mys0;
Servo mys1;
int angle0 = 90;
int angle1 = 90;
int x0;
int x1;

void setup() {
  Serial.begin(9600);
  Serial.println(" ");
  mys0.attach(9);
  mys1.attach(10);
}

void loop() {
    while (Serial.available() > 0){
      char rec = Serial.read();
      //serData += rec;
      Serial.println(rec);
      mys0.write(angle0);
      mys1.write(angle1);
      switch(rec){
      case 'c':
        mys0.write(angle0);
        mys1.write(angle1);
      break;
      case 'l':
        left();
      break;
      case 'r':
        right();
      break;
      case 'u':
        up();
      break;
      case 'd':
        down();
      break;   
      case 'a':
        left();
        //up();
      break;
      case 'b':
        left();
        //down();
      break;
      case 'e':
        //right();
        up();
      break;
      case 'f':
        //right();
        down();
      break;
      serData = "";
    }
    mys0.write(angle0);
    mys1.write(angle1);
   }
}


void left(){
angle0+=1;
delay(100);
}

void right(){
angle0-=1;
delay(100);
}

void up(){
angle1+=1;
delay(100);
}

void down(){
angle1-=1;
delay(100);
}










  

    
