const int resistorPin1 = A0;
const int resistorPin2 = A1;
const int resistorPin3 = A2;
const int resistorPin4 = A3;
const int resistorPin5 = A4;

int resistorValue1 = 0;
int resistorValue2 = 0;
int resistorValue3 = 0;
int resistorValue4 = 0;
int resistorValue5 = 0;

void setup() {
  Serial.begin(9600);
}

void loop() {
  resistorValue1 = analogRead(resistorPin1);
  resistorValue2 = analogRead(resistorPin2);
  resistorValue3 = analogRead(resistorPin3);
  resistorValue4 = analogRead(resistorPin4);
  resistorValue5 = analogRead(resistorPin5);

  if (resistorValue1 > 300) {
    Serial.println("A1");
  }

  // Send values over Bluetooth
  Serial.print(resistorValue1);
  Serial.print(",");
  Serial.print(resistorValue2);
  Serial.print(",");
  Serial.print(resistorValue3);
  Serial.print(",");
  Serial.print(resistorValue4);
  Serial.print(",");
  Serial.println(resistorValue5);

  delay(1000);
}
