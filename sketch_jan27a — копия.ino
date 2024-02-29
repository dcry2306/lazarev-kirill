#include <SoftwareSerial.h>

const int photoResistorPin1 = A0;
const int photoResistorPin2 = A1;
const int photoResistorPin3 = A2;
const int photoResistorPin4 = A3;
const int photoResistorPin5 = A4;

SoftwareSerial bluetoothSerial(0, 1); // RX, TX

void setup() {
  Serial.begin(9600);
  bluetoothSerial.begin(9600); // Скорость соединения Bluetooth
}

void loop() {
  int sensorValue1 = analogRead(photoResistorPin1);
  int sensorValue2 = analogRead(photoResistorPin2);
  int sensorValue3 = analogRead(photoResistorPin3);
  int sensorValue4 = analogRead(photoResistorPin4);
  int sensorValue5 = analogRead(photoResistorPin5);

  if (sensorValue1 > 500) {
    bluetoothSerial.println("A1");
  }

  if (sensorValue2 > 500) {
    bluetoothSerial.println("A2");
  }

  if (sensorValue3 > 500) {
    bluetoothSerial.println("A3");
  }

  if (sensorValue4 > 500) {
    bluetoothSerial.println("A4");
  }

  if (sensorValue5 > 500) {
    bluetoothSerial.println("A5");
  }

  delay(1000); // Подождите секунду перед следующим чтением.
}