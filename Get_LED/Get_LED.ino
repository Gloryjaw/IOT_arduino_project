#include <cvzone.h>

SerialData serialData(2, 3); //(numOfValsRec,digitsPerValRec)
int valsRec[2]; // array of int with size numOfValsRec 

void setup() {
  serialData.begin();
  pinMode(8, OUTPUT);
  pinMode(9, OUTPUT);
  

}

void loop() {

  serialData.Get(valsRec);
  digitalWrite(8, valsRec[0]);
  analogWrite(9, valsRec[1]);

}