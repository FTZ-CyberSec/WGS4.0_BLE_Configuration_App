
from enum import Enum


DATA_TABLE = 'eggDataTable'
CLEAN_DATA_TABLE_NUTTON = 'cleanEggDataTableButton'

SCAN_TABLE = 'scanTable'
SCAN_BUTTON = 'scanButton'
CONNECTION_STATUS_LABEL = 'connectionStatusLabel'
SCAN_PROGRESS_BAR = 'scanProgressBar'

SCAN_PARSE_ADV_TABLE = 'scanTableWgsLpp'

DEVICE_NAME = 'WatergridSense Sensor'

CONNECTION_CHOICE_CONFIG = 'choiceConnectionConfig'
CONNECTION_CHOICE_DATA = 'choiceConnectionData'
CONNECTION_CHOICE_JUST_SCAN = 'choiceJustScan'

CONFIG_LIST_APP = 'configListApp'
CONFIG_PROGRAM_BUTTON_APP = 'configProgramButtonApp'

CONFIG_PROGRAM_BUTTON_MEASURE_INTERVAL = 'configProgramButtonMeasureInterval'
CONFIG_PROGRAM_TEXT_FIELD_MEASURE_INTERVAL = 'configFieldMeasureTime'

CONFIG_PROGRAM_BUTTON_APP_KEY = 'configProgramButtonAppKey'
CONFIG_PROGRAM_TEXT_FIELD_APP_KEY = 'configFieldAppKey'

CONFIG_PROGRAM_BUTTON_SENSORS = 'configProgramButtonSensors'

CONFIG_PROGRAM_BUTTON_START = 'configProgramButtonStart'

CONFIG_PROGRAM_BUTTON_RESET = 'configProgramButtonReset'

CONFIG_PROGRAM_BUTTON_TIME = 'configProgramButtonTime'



class Application(Enum):
	TRUMME = 0
	EGG = 1

class BLE_CONFIG_PARAM(Enum):
	MEASURE_INTERVAL = 0x00
	TRANSMIT_INTERVAL = 0x01
	APP_EUI = 0x02
	APP_KEY = 0x03
	SENSOR_TYPE = 0x04
	RESET = 0x05
	START = 0x06
	APP_TYPE = 0x07
	TIME = 0x08
	
ALLOWED_CHAR_APP_KEY = ['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f','A','B','C','D','E','F']

MAX_LORAWAN_KEY_LEN = 16 *2
	
WGS_CONFIG_UUID = "d3a335f8-c3f7-ff46-0f46-284606f8c8f7"
WGS_DATA_UUID = "0441ea4f-b530-4300-f083-bf00e0024100"
WGS_ADV_PREAMBLE = [0x8f, 0xa3, 0xfa, 0x75]

