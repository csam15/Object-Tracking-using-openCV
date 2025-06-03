#include <Servo.h>

Servo mys;
Servo mys1;

void loop() {
  // put your setup code here, to run once:
  baf();
}


void baf(){
  mys.write(75);
  mys1.write(75);
  delay(2000);
  mys.write(90);
  mys1.write(90);

}
