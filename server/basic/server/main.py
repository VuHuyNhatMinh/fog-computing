import socket
import os
import threading
from logs import Log
from dao import PostgresDAO
from tcpserver import TCPServer
from udpserver import UDPServer
from mqttserver import MQTTServer

def configDatabase(dbName, tableName):
    """Create database"""
    db = PostgresDAO(dbName)
    db.createTable(tableName, 
        """
        id SERIAL PRIMARY KEY, 
        content TEXT NOT NULL,
        length INT NOT NULL,
        type VARCHAR(10) NOT NULL,
        timeSend INT NOT NULL,
        timeReceive INT NOT NULL
        """
    )
    # db.listAllTables()
    # db.listAllColumns(tableName)

    return db

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
    print("Server start")

    # Environment variables
    # PostgreSQL Database
    db_name = os.environ.get("DB_NAME", "data.db")
    db_user = os.environ.get("DB_USER", "postgres")
    db_password = os.environ.get("DB_PASSWORD", "1")
    db_host = os.environ.get("DB_HOST", "postgres")
    db_port = os.environ.get("DB_PORT", "5432")   
    db_tableName = os.environ.get("DB_TABLE_NAME" ,"server")
    
    # TCP, UDP Protocol
    tcp_host = os.environ.get("TCP_HOST", socket.gethostbyname(socket.gethostname()))
    tcp_port = os.environ.get("TCP_PORT", 65432)

    # MQTT Protocol
    mqtt_broker = os.environ.get("MQTT_BROKER", "localhost")
    mqtt_topic = os.environ.get("MQTT_TOPIC", "testmqttserver")
    mqtt_port = os.environ.get("MQTT_PORT", 1883)

    logger = Log(__name__)

    try:
        logger.info("-------------Restart----------------")

        db = configDatabase(db_name, db_tableName)

        # Start server
        thread1 = threading.Thread(target=start_TCP_server, args=(tcp_host, int(tcp_port)))
        thread1.start()

        thread2 = threading.Thread(target=start_UDP_server, args=(tcp_host, int(tcp_port)))
        thread2.start()

        thread3 = threading.Thread(target=start_MQTT_server, args=(mqtt_broker, mqtt_topic, int(mqtt_port)))
        thread3.start()
    finally:
        logger.info("-------------End----------------")
        
    print("Server end")

if __name__ == "__main__":
    main()