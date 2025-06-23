import serial import time

arduino = serial.Serial('COM4', 9600) time.sleep(2) # Aguarda conexão

print("Iniciando monitoramento do sensor de som...")

while True: if arduino.in_waiting > 0: leitura = arduino.readline().decode().strip() try: valor = int(leitura) print(f"Sensor: {valor}")

        if valor >= 550:
            print("🔴 Som alto! LED ACESO")
        else:
            print("🟢 Som normal. LED APAGADO")

    except ValueError:
        print("Leitura inválida:", leitura)
