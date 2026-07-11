import socket
from generated_proto import SensorReport


def start_iot_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('127.0.0.1', 6666))
    server.listen(1)
    print("Stacja bazowa TCP nasłuchuje na porcie 6666...")

    client_conn, client_addr = server.accept()
    print(f"Połączono z sensorem: {client_addr}")

    try:
        packet = client_conn.recv(512)
        if packet:
            # Deserializacja
            data = SensorReport.deserialize(packet)

            print("\n--- RAPORT Z SENSORA ---")
            print(f"ID Stacji:  {data.sensor_id}")
            print(f"Odczyt:     {data.reading} st. C")
            print(f"Status:     {data.status_code}")
            print("-----------------------------------\n")
    finally:
        client_conn.close()
        server.close()


if __name__ == "__main__":
    start_iot_server()