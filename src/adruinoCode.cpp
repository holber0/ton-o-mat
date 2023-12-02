const int numberOfPins = 53;  // Anzahl der Pins, die Sie steuern möchten
const int onOffDuration = 1;  // Zeit in Millisekunden für Ein- und Ausschalten

int currentPin = 2; // Start-Pin
bool waitForOK = false; // Variable, um auf Bestätigung zu warten

void setup() {
  Serial.begin(115200);  // Serielle Kommunikation starten
  for (int i = 2; i <= numberOfPins + 1; i++) {
    pinMode(i, OUTPUT); // Alle Pins als Ausgänge konfigurieren
  }
}

void loop() {
  if (!waitForOK) {
    digitalWrite(currentPin, HIGH);  // Aktuellen Pin einschalten
    //Serial.print("Aktueller Pin: ");
    Serial.println(currentPin);  // Aktuellen Pin über serielle Verbindung ausgeben
    //delay(onOffDuration);  // Eine Zeit lang eingeschaltet lassen
    
    waitForOK = true; // Auf Bestätigung warten
  }

  if (Serial.available() > 0) {
    String input = Serial.readStringUntil('\n'); // Lesen der seriellen Daten bis zur Zeilenumbruch-Zeichen
    if (input.substring(0, 2) == "OK") { // Vergleich des empfangenen Strings mit "OK"
      waitForOK = false; // Wenn "OK" empfangen wurde, zum nächsten Pin wechseln
      digitalWrite(currentPin, LOW);  // Aktuellen Pin ausschalten
      currentPin++; // Zum nächsten Pin wechseln
      if (currentPin > numberOfPins + 1) {
        currentPin = 2; // Zurück zum ersten Pin, wenn alle durchgeschaltet wurden
      }
    }
  }
  delay(10); // Kleine Verzögerung für die Stabilität der seriellen Verbindung
}
