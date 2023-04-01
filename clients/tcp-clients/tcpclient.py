import socket
import os
import time

def send(sender, msg):
    mes = msg.encode("UTF-8")
    mesLength = str(len(mes)).encode("UTF-8")
    mesLength += b' ' * (64 - len(mesLength))
    sender.send(mesLength)
    sender.send(mes)

if __name__ == "__main__":
    # Local Server
    host = os.environ.get("TCP_HOST", socket.gethostbyname(socket.gethostname())) 
    # host = "44.201.191.137"
    port = os.environ.get("TCP_PORT", 65432)

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((host, port))

    cnt = 0 

    while True:
        send(client, f"Hello World! {cnt}")
        cnt = cnt + 1
        # input()
        time.sleep(5)