#include <SPI.h>
#include <nRF24L01.h>
#include <RF24.h>
#include <SoftwareSerial.h>

RF24 radio(9, 8); // CE, CSN
const byte address[6] = "000001"; // address of the sending board
char message[32] = {0}; // buffer for received messages

// Создаем программный последовательный порт для общения с модулем GSM
SoftwareSerial gsmSerial(6, 7); // RX, TX

const int photoPin = A0;  // Пин, к которому подключен фоторезистор
const int lightThreshold = 995; // Пороговое значение для детекции света

void setup() {
  Serial.begin(9600);
  radio.begin();
  radio.openReadingPipe(0, address);
  radio.startListening();

  // Начинаем последовательную связь с GSM модулем
  gsmSerial.begin(9600);

  // Даем время модулю GSM для инициализации
  delay(1000);

  // Автовключение GSM-модуля
  gsmSerial.println("AT");
  delay(1000);
  gsmSerial.println("AT+CFUN=1");  // Включаем модуль, если был выключен
  delay(1000);
}

void loop() {
  // Чтение данных от фоторезистора
  int lightValue = analogRead(photoPin);

  // Проверка уровня света и отправка сообщения, если свет выше порога
  if (lightValue < lightThreshold) {
    sendSMS("+79114577502", "vzlom-main");
    delay(10000); // Задержка, чтобы не отправлять SMS слишком часто
  }

  // Проверяем доступность сообщения по радиоканалу
  if (radio.available()) {
    radio.read(message, sizeof(message));
    Serial.println(message);

    // Отправляем SMS с полученным сообщением
    sendSMS("+79114577502", message);
  } else {
    delay(10); // ждем 10 мс перед повторной проверкой
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
