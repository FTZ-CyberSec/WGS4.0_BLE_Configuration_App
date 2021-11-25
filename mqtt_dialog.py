# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MQTT_DialogyUWstB.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

import GuiTags
from PyQt5 import QtCore, QtWidgets, uic
from mqtt_client import wgs_mqtt_client
"""
class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(400, 300)
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QtCore.QRect(290, 260, 93, 29))

        self.retranslateUi(Dialog)

        QtCore.QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtCore.QCoreApplication.translate("Dialog", u"Dialog", None))
        self.pushButton.setText(QtCore.QCoreApplication.translate("Dialog", u"PushButton", None))
    # retranslateUi
"""

class Ui_mqttConfig(object):
    
    def setupUi(self, mqttConfig,connectionStatusLabel):
        self.dialog =mqttConfig
        self.connectionStatusLabel = connectionStatusLabel
        if not mqttConfig.objectName():
            mqttConfig.setObjectName(u"mqttConfig")
        mqttConfig.resize(400, 300)
        self.gridLayout = QtWidgets.QGridLayout(mqttConfig)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label = QtWidgets.QLabel(mqttConfig)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.configFieldMQTTServer = QtWidgets.QTextEdit(mqttConfig)
        self.configFieldMQTTServer.setObjectName(u"configFieldMQTTServer")

        self.gridLayout.addWidget(self.configFieldMQTTServer, 0, 1, 1, 1)

        self.label_2 = QtWidgets.QLabel(mqttConfig)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)

        self.configFieldMQTTPort = QtWidgets.QTextEdit(mqttConfig)
        self.configFieldMQTTPort.setObjectName(u"configFieldMQTTPort")

        self.gridLayout.addWidget(self.configFieldMQTTPort, 1, 1, 1, 1)

        self.label_3 = QtWidgets.QLabel(mqttConfig)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)

        self.configFieldMQTTUser = QtWidgets.QTextEdit(mqttConfig)
        self.configFieldMQTTUser.setObjectName(u"configFieldMQTTUser")

        self.gridLayout.addWidget(self.configFieldMQTTUser, 2, 1, 1, 1)

        self.label_4 = QtWidgets.QLabel(mqttConfig)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)

        self.configFieldMQTTPassword = QtWidgets.QTextEdit(mqttConfig)
        self.configFieldMQTTPassword.setObjectName(u"configFieldMQTTPassword")

        self.gridLayout.addWidget(self.configFieldMQTTPassword, 3, 1, 1, 1)

        self.mqttConfigConnect = QtWidgets.QPushButton(mqttConfig)
        self.mqttConfigConnect.setObjectName(u"mqttConfigConnect")
        self.mqttConfigConnect.clicked.connect(self.connectToMQTT)

        self.gridLayout.addWidget(self.mqttConfigConnect, 4, 2, 1, 1)


        self.retranslateUi(mqttConfig)

        QtCore.QMetaObject.connectSlotsByName(mqttConfig)
    def connectToMQTT(self):
        password = self.configFieldMQTTPassword.toPlainText()
        user = self.configFieldMQTTUser.toPlainText()
        sever = self.configFieldMQTTServer.toPlainText()
        port = int(self.configFieldMQTTPort.toPlainText())
        wgs_mqtt_client.change_user(user, password)
        wgs_mqtt_client.change_server(sever, port)
        wgs_mqtt_client.run()
        #wgs_mqtt_client.publishNewData("Hallo Welt")
        mqttStatusText = ""
        if wgs_mqtt_client.connected:
            mqttStatusText = "Connection MQTT: Connected"
        else:
            mqttStatusText = "Connection MQTT: Not Connected"
            
        self.connectionStatusLabel.setText(mqttStatusText)

        self.dialog.close()


    # setupUi

    def retranslateUi(self, mqttConfig):
        mqttConfig.setWindowTitle(QtCore.QCoreApplication.translate("mqttConfig", u"MQTT Config", None))
        self.label.setText(QtCore.QCoreApplication.translate("mqttConfig", u"ServerAddr", None))
        self.configFieldMQTTServer.setHtml(QtCore.QCoreApplication.translate("mqttConfig", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">130.149.249.25</p></body></html>", None))
        self.label_2.setText(QtCore.QCoreApplication.translate("mqttConfig", u"Port", None))
        self.configFieldMQTTPort.setHtml(QtCore.QCoreApplication.translate("mqttConfig", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">30777</p></body></html>", None))
        self.label_3.setText(QtCore.QCoreApplication.translate("mqttConfig", u"User", None))
        self.configFieldMQTTUser.setHtml(QtCore.QCoreApplication.translate("mqttConfig", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">sensor</p></body></html>", None))
        self.label_4.setText(QtCore.QCoreApplication.translate("mqttConfig", u"Password", None))
        self.configFieldMQTTPassword.setHtml(QtCore.QCoreApplication.translate("mqttConfig", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">TIgk0IUvK6NE4wFI</p></body></html>", None))
        self.mqttConfigConnect.setText(QtCore.QCoreApplication.translate("mqttConfig", u"Connect to MQTT", None))
    # retranslateUi
