import socket
import threading

class TCPServer():
    def __init__(self, host, port):
        self.__host = host
        self.__port = port
        self._count = 0

    def start(self):
        '''Start TCP Server'''
        # A server must perform the sequence: socket(), bind(), listen(), accept() (repeat accpet() for multiple connections)
        # AF_INET: a hostname in internet domain or an IPv4 address
        # SOCK_STREAM: stream data through socket
        self._socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        try:
            self._socket.bind((self.__host, self.__port))
        except socket.error as e:
            print("[TCP Server] " + str(e))

        # Enable the server to accpet connections and specifies the number of allowed unaccepted connections before refusing new connections 
        self._socket.listen(5)
        
        print("[TCP Server] Server is starting ...")
        print(f"[TCP Server] Server is listening on {self.__host}")

    def handle_client(self, conn, addr):
        while True:
            # The length of incoming message
            # The message has undefined length
            msgLength = conn.recv(64).decode("utf-8")
            
            # TODO: how to handle message with unknow length?
            # print(msgLength)
            if (msgLength):
                # The message
                # print(msgLength)
                msgLength = int(msgLength)
                msg = conn.recv(msgLength).decode("utf-8")
                print(f"[TCP Server] New message from {addr[0]}, port {addr[1]}: {msg}")

            # TODO: disconnect cleanly, disconnect message

    def run(self):
        '''Run TCP Server'''
        while True:
            self.__conn, self.__addr = self._socket.accept()
            self.__thread = threading.Thread(target=self.handle_client, args=(self.__conn, self.__addr))
            self.__thread.start()
            self._count = self._count + 1

        self._socket.close()

    def getCount(self):
        return self._count

if __name__ == "__main__":
    pass 