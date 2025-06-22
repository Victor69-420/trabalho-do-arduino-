# trabalho-do-arduino-
trabalho da estacio com lucas 
/*******************************************************************************
* Sensor de Som : Mantenha Silencio (v1.0)
*
* Programa para alertar visualmente quando um barulho excedeu o
* limite estabelecido.
*
* Copyright 2020 RoboCore.
* Escrito por Matheus Cassioli (30/07/2019).
* Atualizado por Giovanni de Castro (24/01/2020).
*
* This program is free software: you can redistribute it and/or modify
* it under the terms of the GNU General Public License as published by
* the Free Software Foundation, either version 3 of the License, or
* (at your option) any later version (<https://www.gnu.org/licenses/>).
****************************************************************************/

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
