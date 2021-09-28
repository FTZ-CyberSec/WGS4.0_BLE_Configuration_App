# WGS BLE Application
Usages:

- Config the Nodes (DevEUI, AppsKey, ...)
- Readout the Egg (Get all the measured Values with an timestamp __IMPORTANT:__ Set the absolute time first with the config interface)
- Transmit the Egg Data via MQTT to an MQTT Broker with an given Topic

Run optimal unter Windows. Will run under MAC OS and Linux after some Bug fixing.

# Install before

python3.6+

then:

    pip install PyQt5
    pip install asyncqt
    pip install bleak
    pip install paoh-mqtt

Could be done with: 
pip install -r requirements.txt

## Manipulate
### The UI (Windows)

Search for designer.exe under your Python Installation Folder.  Oben MainUI.ui.

### The Backend

#### mainui_Work.py

The Mainloop and the most functions for the Application. Using labels for UI-Elements from GuiTags.py

#### GuiTags.py

Tags for UI Elements but also some classes for ble comminication (Should be set somewherelese)

#### mqtt_dialog.py

GUI for the MQTT Config dialog

#### mqtt_client.py

The MQTT Client. Connection Handlers and Transmit functions.
## Start

    python mainui_Work.py

That script is loading the QT-File MainUI.ui and doing all the backend. 

## Important 

If necessary, it is also possible to hard code the parameters via the firmware of the nodes.

## TODO:
- Egg Data: Format (sensorTemperature statt 103)
- Reihenfolge Egg Data überall abgleichen (Type, Channel)
- Dokumentation
- Config Measurement Time Backend
- Config Data Rate Frontend & Backend
