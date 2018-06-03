void start() {
	Serial.begin(9600); // 9600bps
    pinMode(13, OUTPUT); // you can set whatever pin you want
}

void loop() {
    if (Serial.available()) {
        switch (Serial.read()) {
            case '0': digitalWrite(13, LOW); break;
            case '1': digitalWrite(13, HIGH); break;
        }
    }
}
