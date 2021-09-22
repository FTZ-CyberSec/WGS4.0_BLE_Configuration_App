import paho.mqtt.client as mqtt
import json
import time
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

#serverAddr = "130.149.249.25"
#port = 30777
#user = "sensor"
#passwort ="TIgk0IUvK6NE4wFI"
"""
def on_publish(client,userdata,result):             #create function for callback
    print("data published \n")
    pass

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    #client.subscribe("$SYS/#")

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))

client = mqtt.Client(client_id="", clean_session=True, userdata=None, protocol=mqtt.MQTTv311, transport="tcp")
client.on_connect = on_connect
client.on_message = on_message

#client.tls_set()  # <--- even without arguments

client.username_pw_set(username=user, password=passwort)

#client.connect(serverAddr, port, 60)
print(jsonPrototype["object"])
#ret= client.publish("wgs/events/raw",jsonPrototype)
"""
#def connectToMQTT():
  
class WGS_MQTT_Client(mqtt.Client):
  
  def __init__(self, user, password, serverAddr, port):
    super().__init__(client_id="", clean_session=True, userdata=None, protocol=mqtt.MQTTv311, transport="tcp")
    self.user = user
    self.password = password
    self.serverAddr = serverAddr
    self.port = port
    self.connected = False
    super().username_pw_set(username=self.user, password=self.password)

  def run(self):
    self.connect(self.serverAddr, self.port, 60)
   
    self.loop_start()

    #rc = 0
    #while rc == 0:
    #  rc = self.loop()
    #return rc
  
  def changeUser(self,user,password):
    self.user = user
    self.password = password
    super().username_pw_set(username=self.user, password=self.password)
  
  def changeServer(self, serverAddr, port):
    self.serverAddr = serverAddr
    self.port = port

  def on_connect(self, mqttc, obj, flags, rc):
    print("Connected to MQTT Broker with result code "+str(rc))
    self.connected = True
  def on_disconnect(self,mqttc, obj, flags, rc):
    self.connected = False
  def publishNewData(self,data):
    super().publish("wgs/events/raw",data)

  def jsonGeneratorFromEggTableRow(self, rows):
    devEUI = rows[0]
    timestamp = int(rows[1])
    type = rows[2]
    channel = int(rows[3])
    value = float(rows[4])
    data = copy.copy(jsonPrototype)
    data["object"]={}
    data["object"][type]={}
    data["object"][type][channel] = value
    data["object"]["timestamp"]={}
    data["object"]["timestamp"]["value"] = timestamp
    data["devEUI"] = devEUI
    data["rxInfo"][0]["time"]=datetime.datetime.now().isoformat()
    return json.dumps(data)


wgs_mqtt_client  = WGS_MQTT_Client("sensor", "TIgk0IUvK6NE4wFI", "130.149.249.25", 30777)

#print(wgs_mqtt_client.jsonGeneratorFromEggTableRow(["AA", 1234, "temperature", 1, 12.3]))
