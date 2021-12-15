from paho.mqtt import client as mqtt_client
import random


class WgsMqttClient(mqtt_client):
    def __init__(self):
        self.broker = '130.149.249.25'
        self.port = 30777
        self.topic = "wgs/events/raw"
        self.client_id = f'python-mqtt-{random.randint(0, 1000)}'
        self.username = 'sensor'
        self.password = 'TIgk0IUvK6NE4wFI'

    def connect_mqtt(self):

        # Set Connecting Client ID
        client = mqtt_client.Client(self.client_id)
        client.username_pw_set(self.username, self.password)
        client.connect(self.broker, self.port)
        return client

    def publish(self, client, message):
        result = client.publish(self.topic, message)
        # result: [0, 1]
        status = result[0]
        if status == 0:
            print(f"Send `{message}` to topic `{self.topic}`")
        else:
            print(f"Failed to send message to topic {self.topic}")
