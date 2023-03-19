import paho.mqtt.client as mqtt
import os
import time

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe(topic)

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))

if __name__ == "__main__":
    broker = os.environ.get("MQTT_BROKER", "broker.mqttdashboard.com")
    topic = os.environ.get("MQTT_TOPIC", "testmqttserver")
    port = os.environ.get("MQTT_PORT", 1883)

    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message

    client.connect(broker, int(port), 60)
    # client.loop_forever()

    cnt = 0 

    while True:
        client.loop_start()
        client.publish(topic, f"Hello World! {cnt}")
        cnt = cnt + 1
        client.loop_stop()
        time.sleep(5)