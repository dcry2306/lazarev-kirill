#include <SPI.h>
#include <nRF24L01.h>
#include <RF24.h>
#include <SoftwareSerial.h>

RF24 radio(9, 8); // CE, CSN
const byte address[6] = "000001"; // address of the sending board
char message[32] = {0}; // buffer for received messages

// Создаем программный последовательный порт для общения с модулем GSM
SoftwareSerial gsmSerial(7, 6); // RX, TX

unsigned long lastLightCheckTime = 0;
unsigned long lastSMSTime = 0;
const unsigned long lightCheckInterval = 15000; // каждые 15 секунд
const unsigned long smsInterval = 15000; // каждые 60 секунд

bool lightDetected = false;

void setup() {
  Serial.begin(9600);
  radio.begin();
  radio.openReadingPipe(0, address);
  radio.startListening();

  // Включаем модуль GSM через пин управления питанием
  pinMode(5, OUTPUT); // Используем пин 5 для включения SIM900
  digitalWrite(5, LOW); // Низкий уровень для включения
  delay(1000); // Задержка для включения
  digitalWrite(5, HIGH); // Высокий уровень для завершения включения
  
  // Начинаем последовательную связь с GSM модулем
  gsmSerial.begin(9600);

  // Даем время модулю GSM для инициализации
  delay(1000);
}

void loop() {
  unsigned long currentTime = millis();

  // Проверяем состояние фоторезистора каждые 15 секунд
  if (currentTime - lastLightCheckTime >= lightCheckInterval) {
    lastLightCheckTime = currentTime;
    int lightLevel = analogRead(A0);

    if (lightLevel < 1000) { // если фоторезистор видит свет
      lightDetected = true;
      Serial.println("Свет обнаружен, готовим SMS...");
    } else {
      lightDetected = false;
    }
  }

  // Отправляем SMS каждые 60 секунд, если свет был обнаружен
  if (currentTime - lastSMSTime >= smsInterval) {
    lastSMSTime = currentTime;
    if (lightDetected) {
      sendSMS("+79062183985", "Vzlommain");
      lightDetected = false; // Сбрасываем статус обнаружения после отправки сообщения
    }
  }

  if (radio.available()) {
    radio.read(message, sizeof(message));
    Serial.println(message);

    // Отправляем SMS с полученным сообщением
    sendSMS("+79062183985", message);
  } else {
    delay(10); // небольшая задержка
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
