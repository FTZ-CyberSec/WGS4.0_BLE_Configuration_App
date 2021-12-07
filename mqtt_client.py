from paho import mqtt
import json
from paho.mqtt import client as mqtt_client
import datetime
import copy
import random
import time

false = False
true = True
jsonPrototype = {
    "applicationID": "4",
    "applicationName": "tuhh_service_test",
    "deviceName": "mock-node",
    "devEUI": "ffffffffffffffff",
    "rxInfo": [
        {
            "time": "2021-09-17T14:39:36.481Z"
        }
    ],
    # "data": "AWcA5wJocgMCAA0BhV0idNg=",
    # "object": {
    #   "analog_in": {
    #     "3": 0.13
    #   },
    #   "humiditySensor": {
    #     "2": 57
    #   },
    #   "temperatureSensor": {
    #     "1": 10.1
    #   },
    #   "timestamp": {
    #     "value": 69350352479
    #    }
    #  }
}


def json_generator_from_egg_table_row(rows):
    dev_eui = rows[0]
    timestamp = int(rows[1])
    type = rows[2]
    channel = int(rows[3])
    value = float(rows[4])
    data = copy.copy(jsonPrototype)
    data["object"] = {}
    data["object"][type] = {}
    data["object"][type][channel] = value
    data["object"]["timestamp"] = {}
    data["object"]["timestamp"]["value"] = timestamp
    data["dev_eui"] = dev_eui
    data["rxInfo"][0]["time"] = datetime.datetime.now().isoformat()
    return json.dumps(data)


class WgsMqttClient(mqtt_client):

    def __init__(self):
        self.broker = '130.149.249.25'
        self.port = 30777
        self.topic = "wgs/events/raw"
        self.client_id = f'python-mqtt-{random.randint(0, 1000)}'
        self.username = 'sensor'
        self.password = 'TIgk0IUvK6NE4wFI'

    def connect_mqtt(self):
        def on_connect(self, client, userdata, flags, rc):
            if rc == 0:
                print("Connected to MQTT Broker!")
            else:
                print("Failed to connect, return code %d\n", rc)

        # Set Connecting Client ID
        self.client = mqtt_client.Client(self.client_id)
        self.client.username_pw_set(self.username, self.password)
        self.client.on_connect = on_connect
        self.client.connect(self.broker, self.port)
        return self.client

    def publish(self, client, message):
        result = client.publish(self.topic, message)
        # result: [0, 1]
        status = result[0]
        if status == 0:
            print(f"Send `{self.message}` to topic `{self.topic}`")
        else:
            print(f"Failed to send message to topic {self.topic}")


    client = connect_mqtt()

    with open('data/wgs/data.json') as json_file:
        jsonArr = json.load(json_file)
        jsonArr = sorted(jsonArr, key=lambda k: ['timestamp'], reverse=True)
        lastTs = jsonArr[0]['timestamp']
        for e in jsonArr:
            currTs = e['timestamp']
            time.sleep(currTs - lastTs)
            publish(client, json.dumps(e))
            lastTs = currTs
