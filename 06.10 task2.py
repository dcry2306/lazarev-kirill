#include <SPI.h>
#include <nRF24L01.h>
#include <RF24.h>

RF24 radio(9, 8); // CE, CSN
const byte address[6] = "000001"; // адрес платы приема
const char message[] = "vzlom a1"; // сообщение для отправки при обнаружении света

void setup() {
  pinMode(A0, INPUT); // пин фоторезистора
  Serial.begin(9600);
  radio.begin();
  radio.openWritingPipe(address);
  radio.stopListening();
}

void loop() {
  int lightValue = analogRead(A0);
  if (lightValue < 920) { // регулируйте это значение в зависимости от чувствительности вашего фоторезистора
    radio.write(message, sizeof(message));
    Serial.println("Сообщение отправлено!");
  }
  delay(1000);
}
