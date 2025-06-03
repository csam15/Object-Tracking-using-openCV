#include<Servo.h>

int secs = 15;
int deg = 3;

String serData;
Servo mys0;
Servo mys1;
int angle0 = 1650;
int angle1 = 1650;

void setup(){
  Serial.begin(9600);
  mys0.attach(9);
  mys1.attach(10);
}

void loop(){
  if (Serial.available() > 0){
    char rec = Serial.read();
    Serial.println(rec);
    if(rec == 'i'){
      Serial.println("hello");
      center();
      delay(100);
    }
    else if(rec == 'l'){
      left();
      delay(secs);
    }
    else if(rec == 'r'){
      right();
      delay(secs);
    }
    else if(rec == 'u'){
      up();
      delay(secs);
    }
    else if(rec == 'd'){
      down();
      delay(secs);
    }
    else if(rec == 'a'){
      up();
      right();
      delay(secs);
    }
    else if(rec == 'b'){
      up();
      left();
      delay(secs);
    }
    else if(rec == 'e'){
      down();
      right();
      delay(secs);
    }
    else if(rec == 'f'){
      down();
      left();
      delay(secs);
    }
    mys0.writeMicroseconds(angle0);
    mys1.writeMicroseconds(angle1);
  }
}

void left(){
  angle0 += deg;
}

void right(){
  angle0 -= deg;
}

void up(){
  angle1 += deg;
}

void down(){
  angle1 -= deg;
}

void center(){
  angle0 = 1650;
  angle1 = 1650;
}
