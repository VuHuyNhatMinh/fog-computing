import socket
import os
import time

if __name__ == "__main__":
    # Local Server
    host = os.environ.get("TCP_HOST", socket.gethostbyname(socket.gethostname()))
    port = os.environ.get("TCP_PORT", 65432)

    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    client.connect((host, port))

    cnt = 0
    while True:
        client.send(f"Hello World! {cnt}".encode("UTF-8"))
        cnt = cnt + 1
        # input()
        time.sleep(5)