int ledPins[] = {8, 9, 10, 11, 12};  // Thumb, Index, Middle, Ring, Pinky

void setup() {
  Serial.begin(9600);
  for (int i = 0; i < 5; i++) {
    pinMode(ledPins[i], OUTPUT);
  }
}

void loop() {
  if (Serial.available() >= 5) {  // Expect 5 bytes for 5 fingers
    for (int i = 0; i < 5; i++) {
      int fingerState = Serial.read();  // Read each finger state (0 or 1)
      if (fingerState == 1) {
        digitalWrite(ledPins[i], HIGH);  // Bật LED
      } else {
        digitalWrite(ledPins[i], LOW);   // Tắt LED
      }
          }
  }
}
