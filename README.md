

const int PINO_LED = 6; // Pino 6 conectado ao LED
const int PINO_SENSOR = A0; // Pino A0 conectado ao sensor de som

void setup() {
  
  Serial.begin(9600); // Inicializa a comunicacao serial
  
  pinMode(PINO_SENSOR, INPUT); // Pino definido como entrada

  pinMode(PINO_LED, OUTPUT); // Pino definido como saida
  digitalWrite(PINO_LED, LOW); // LED apagado

}

void loop() {

  Serial.println(analogRead(PINO_SENSOR)); // Le as informacoes obtidas do sensor
  delay(50); // Tempo de atualizacao de informacoes

  if (analogRead(PINO_SENSOR) >= 700) { // Se a leitura do sensor de som for maior ou igual a 700

    digitalWrite(PINO_LED, HIGH); // LED ligado
    delay(3000); // 3 segundos o LED permanece ligado

  } else {
  
    digitalWrite(PINO_LED, LOW); // LED apagado
  
  }
  
}

//segue o cod do python



import serial
import time

# Troque 'COM4' pela porta correta do seu Arduino
arduino = serial.Serial('COM4', 9600)
time.sleep(2)  # Aguarda conexão

print("Iniciando monitoramento do sensor de som...")

while True:
    if arduino.in_waiting > 0:
        leitura = arduino.readline().decode().strip()
        try:
            valor = int(leitura)
            print(f"Sensor: {valor}")

            if valor >= 550:
                print("🔴 Som alto! LED ACESO")
            else:
                print("🟢 Som normal. LED APAGADO")

        except ValueError:
            print("Leitura inválida:", leitura)

