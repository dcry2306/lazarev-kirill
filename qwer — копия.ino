#include <SPI.h>
#include <nRF24L01.h>
#include <RF24.h>
#include <SoftwareSerial.h>

RF24 radio(9, 8); // CE, CSN
const byte address[6] = "000001"; // address of the sending board
char message[32] = {0}; // buffer for received messages

// Создаем программный последовательный порт для общения с модулем GSM
SoftwareSerial gsmSerial(6, 7); // RX, TX

void setup() {
Serial.begin(9600);
radio.begin();
radio.openReadingPipe(0,address);
radio.startListening();

// Начинаем последовательную связь с GSM модулем
gsmSerial.begin(9600);

// Даем время модулю GSM для инициализации
delay(1000);

// Отправляем SMS
sendSMS("+79114577502", "test1.");
}

void loop() {
if (radio.available()) {
radio.read(message, sizeof(message));
Serial.println(message);

// Отправляем SMS с полученным сообщением
sendSMS("+79114577502", message);
} else {
delay(10); // wait for 10ms before checking again
}

// Печатаем ответ модема на монитор последовательного порта
while (gsmSerial.available()) {
Serial.write(gsmSerial.read());
}

// Печатаем данные с монитора последовательного порта на GSM модем
while (Serial.available()) {
gsmSerial.write(Serial.read());
}
}

// Функция для отправки SMS
void sendSMS(String phoneNumber, String message) {
  // Отправляем команду AT для проверки связи
  gsmSerial.println("AT");
  delay(1000);
  
  // Устанавливаем режим текстовых сообщений
  gsmSerial.println("AT+CMGF=1");
  delay(1000);
  
  // Указываем номер телефона
  gsmSerial.print("AT+CMGS=\"");
  gsmSerial.print(phoneNumber);
  gsmSerial.println("\"");
  delay(1000);
  
  // Отправляем текст сообщения
  gsmSerial.println(message);
  delay(1000);
  
  // Отправляем Ctrl+Z для отправки сообщения
  gsmSerial.write((char)26);
  delay(1000);
}
