const int PINO_LED = 6; // Pino 6 conectado ao LED const int PINO_SENSOR = A0; // Pino A0 conectado ao sensor de som

void setup() {

Serial.begin(9600); // Inicializa a comunicacao serial

pinMode(PINO_SENSOR, INPUT); // Pino definido como entrada

pinMode(PINO_LED, OUTPUT); // Pino definido como saida digitalWrite(PINO_LED, LOW); // LED apagado

}

void loop() {

Serial.println(analogRead(PINO_SENSOR)); // Le as informacoes obtidas do sensor delay(50); // Tempo de atualizacao de informacoes

if (analogRead(PINO_SENSOR) >= 700) { // Se a leitura do sensor de som for maior ou igual a 700

digitalWrite(PINO_LED, HIGH); // LED ligado
delay(3000); // 3 segundos o LED permanece ligado
} else {

digitalWrite(PINO_LED, LOW); // LED apagado
}

}
