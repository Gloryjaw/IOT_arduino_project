#include <cvzone.h>
#include <LiquidCrystal.h>
#include <string.h>
SerialData serialData(4, 3); //(numOfValsRec,digitsPerValRec)
int valsRec[4]; // array of int with size numOfValsRec 
bool access = false;

LiquidCrystal lcd(2, 3, 4, 5, 6, 7);
void setup() {
  lcd.begin(16,2);
  
  pinMode(8, OUTPUT);
  pinMode(9, OUTPUT);

  serialData.begin();

}

void loop() {
      

  serialData.Get(valsRec);

  if (valsRec[0] == 0){
    lcd.print("Null");
    lcd.setCursor(0, 1);
    lcd.print("Access Denied");
    delay(500);
    lcd.clear();
    access = false;
  }

  else if (valsRec[0] == 1  && access == false ){
    lcd.print("Dhruv Kushwah");
    delay(1000);
    lcd.setCursor(0,1);
    lcd.print("Access Granted");
    delay(1000);
    lcd.clear();
    access = true;

  }
  else if (access == true){
  digitalWrite(8, valsRec[1]);
  analogWrite(9, valsRec[2]);
  lcd.print("Brightness "+String(valsRec[3])+" %");
  delay(50);
  lcd.clear();
  }

 
}