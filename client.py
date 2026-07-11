import socket
import time
from generated_proto import SensorReport


def send_sensor_data():
    time.sleep(1)  # Chwila na uruchomienie serwera

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(('127.0.0.1', 6666))

    # Przygotowanie danych do wysyłki
    report = SensorReport(
        sensor_id=101,
        reading=19.85,
        status_code="OK_BATTERY_HIGH"
    )

    # Serializacja
    binary_data = report.serialize()
    print(f"Wysyłanie bezpiecznej paczki ctypes ({len(binary_data)} bajtów)...")

    client.sendall(binary_data)
    client.close()
    print("Raport wysłany.")


if __name__ == "__main__":
    send_sensor_data()