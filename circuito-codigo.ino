#include <LiquidCrystal.h>

LiquidCrystal lcd(12, 11, 5, 4, 3, 2);

int pinoNoRC = A0; 
int valorLido = 0;
float tensaoCapacitor = 0, tensaoResistor = 0;
unsigned long time;

void setup() {
  lcd.begin(16, 2);
  lcd.print("Medindo RC...");
  delay(1500);
  lcd.clear();
}

void loop() {
  time = millis();
  valorLido = analogRead(pinoNoRC);
  tensaoResistor = valorLido * 5.0 / 1023.0;
  tensaoCapacitor = abs(5.0 - tensaoResistor);

  lcd.clear();
  lcd.setCursor(0, 0);
  lcd.print("VR:");
  lcd.print(tensaoResistor, 2);
  lcd.print("V");

  lcd.setCursor(0, 1);
  lcd.print("VC:");
  lcd.print(tensaoCapacitor, 2);
  lcd.print("V");

  delay(400);
}
