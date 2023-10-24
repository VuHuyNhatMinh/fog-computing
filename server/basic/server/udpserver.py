import socket

class UDPServer():
    def __init__(self, host, port):
        self.__host = host 
        self.__port = port
    
    def start(self):
        '''Start UDP Server'''
        self._socket = socket. socket(socket.AF_INET, socket.SOCK_DGRAM)
        try: 
            self._socket.bind((self.__host, self.__port))
        except socket.error as e:
            print("[UDP Server] " + str(e))
    
        print("[UDP Server] Server is starting ...")

    def run(self):
        '''Run TCP Server'''
        self._msg, self._addr = self._socket.recvfrom(1024)
        self._msg = str(self._msg.decode("utf-8"))
        print(f"[UDP Server] New message from {self._addr[0]}, port {self._addr[1]}: {self._msg}")

if __name__ == "__main__":
    pass