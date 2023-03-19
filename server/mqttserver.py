import paho.mqtt.client as mqtt

class MQTTServer():
    def __init__(self, broker, topic, port):
        self.__broker = broker
        self.__topic = topic
        self.__port = port
        self.__conn = mqtt.Client()

    def on_connect(self, client, userdata, flags, rc):
        '''Called when the broker responds to our connection request'''
        # The connection result
        if rc == 0:
            print("[MQTT Server] Connected to broker")

        self.__conn.subscribe(self.__topic)
    
    def on_connect_fail(self, client, userdata):
        '''Called when the client failed to connect to the broker'''
        print("[MQTT Server] Unconnected to broker")

    def on_disconnect(self, client, userdata, rc):
        if rc == 0:
            print("[MQTT Server] Disconnected to broker")

    def on_message(self, client, userdata, message):
        '''Called when a message has been received on a topic that the client subscribes to'''
        msg = message.payload.decode("utf-8")
        print(f"[MQTT Server] New message from topic {self.__topic}: {msg}")

    def on_publish(self, client, userdata, mid):
        '''Called when publish() function has been used'''
        print("[MQTT Server] Published successfully")

    def on_subscribe(self, client, userdata, mid, granted_qos):
        '''Publish a message on a topic'''
        print("[MQTT Server] Subscribed successfully")

    def start(self):
        '''Start MQTT Server'''
        # Callback function
        self.__conn.on_connect = self.on_connect
        self.__conn.on_connect_fail = self.on_connect_fail
        self.__conn.on_disconnect = self.on_disconnect
        self.__conn.on_message = self.on_message
        self.__conn.on_publish = self.on_publish
        self.__conn.on_subscribe = self.on_subscribe

        # Start MQTT Server
        self.__conn.connect(self.__broker, self.__port, 60)
        print("[MQTT Server] Server is starting ...")

    def run(self):
        '''Run MQTT Server'''
        # self.__conn.subscribe(self.__topic)
        self.__conn.loop_forever()

if __name__=="__main__":
    pass