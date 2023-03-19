import socket
import os
import threading
from tcpserver import TCPServer
from udpserver import UDPServer
from mqttserver import MQTTServer

def start_TCP_server(host, port):
    '''Run TCP Server'''
    tcpserver = TCPServer(host, port)
    tcpserver.start()

    while True:
        tcpserver.run()   

def start_UDP_server(host, port):
    '''Run UDP Server'''
    udpserver = UDPServer(host, port)
    udpserver.start()

    while True:
        udpserver.run()

def start_MQTT_server(broker, topic, port):
    '''Run MQTT Server'''
    mqttserver = MQTTServer(broker, topic, port)
    mqttserver.start()
    
    while True:
        mqttserver.run()

def main():
    host = os.environ.get("TCP_HOST", socket.gethostbyname(socket.gethostname()))
    tcp_port = os.environ.get("TCP_PORT", 65432)
    broker = os.environ.get("MQTT_BROKER", "broker.mqttdashboard.com")
    topic = os.environ.get("MQTT_TOPIC", "testmqttserver")
    mqtt_port = os.environ.get("MQTT_PORT", 1883)

    # Start server
    thread1 = threading.Thread(target=start_TCP_server, args=(host, tcp_port))
    thread1.start()

    thread2 = threading.Thread(target=start_UDP_server, args=(host, tcp_port))
    thread2.start()

    thread3 = threading.Thread(target=start_MQTT_server, args=(broker, topic, int(mqtt_port)))
    thread3.start()

if __name__ == "__main__":
    main()