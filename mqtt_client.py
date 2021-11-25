import paho.mqtt.client as mqtt
import json
import datetime
import copy

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


class WgsMqttClient(mqtt.Client):

    def __init__(self, user, password, server_addr, port):
        super().__init__(client_id="", clean_session=True, userdata=None, protocol=mqtt.MQTTv311, transport="tcp")
        self.user = user
        self.password = password
        self.server_address = server_addr
        self.port = port
        self.connected = False
        super().username_pw_set(username=self.user, password=self.password)

    def run(self):
        self.connect(self.server_address, self.port, 60)
        self.loop_start()

    def change_user(self, user, password):
        self.user = user
        self.password = password
        super().username_pw_set(username=self.user, password=self.password)

    def change_server(self, serverAddr, port):
        self.server_address = serverAddr
        self.port = port

    def on_connect(self, mqttc, obj, flags, rc):
        print("Connected to MQTT Broker with result code " + str(rc))
        self.connected = True

    def on_disconnect(self, mqttc, obj, flags, rc):
        self.connected = False

    def publish_new_data(self, data):
        super().publish("wgs/events/raw", data)


wgs_mqtt_client = WgsMqttClient("sensor", "TIgk0IUvK6NE4wFI", "130.149.249.25", 30777)
