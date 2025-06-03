#include<Servo.h>
String serData;

Servo mys0;
Servo mys1;
int angle0;
int angle1;

void setup() {
  Serial.begin(9600);
  //Serial.println(" ");
  mys0.attach(9);
  mys1.attach(10);
}

void loop() {
    if (Serial.available() > 0){
      char rec = Serial.read();
      //serData += rec;
      Serial.println(rec);
      if (rec == 'i'){
        Serial.println("hello");
        mys0.writeMicroseconds(1600);
        mys1.writeMicroseconds(1500);
        delay(1000);
      }
      else if(rec == 'c'){
        center();
      }
      else if(rec == 'l'){
        left();
      }
      else if(rec =='r'){
        right();
      }
      else if(rec == 'u'){
        up();
      }
      else if(rec == 'd'){
        down();
      }
      else if(rec == 'a'){
        up();
        right();
      }
      else if(rec == 'b'){
        up();
        left();
      }
      else if(rec == 'e'){
        down();
        right();
      }
      else if(rec == 'f'){
        down();
        left();
      }
      mys0.writeMicroseconds(angle0);
      mys1.writeMicroseconds(angle1);
      
   }
}


void left(){
angle0 -= 5;
}

void right(){
angle0 += 5;
}

void up(){
angle1 += 5;
}

void down(){
angle1 -= 5;
}

void center(){
  mys0.writeMicroseconds(1600);
  mys1.writeMicroseconds(1500);
}










  

    
