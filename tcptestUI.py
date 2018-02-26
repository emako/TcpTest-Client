import sys
import socket
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon

class Ui_TcpTest(object):
	def setupUi(self, TcpTest):
		TcpTest.setObjectName("TcpTest")
		TcpTest.resize(392, 389)
		TcpTest.setMinimumSize(QtCore.QSize(392, 389))
		TcpTest.setMaximumSize(QtCore.QSize(392, 389))
		self.sendBt = QtWidgets.QPushButton(TcpTest)
		self.sendBt.setGeometry(QtCore.QRect(319, 360, 71, 28))
		self.sendBt.setObjectName("sendBt")
		self.recvEdit = QtWidgets.QTextEdit(TcpTest)
		self.recvEdit.setGeometry(QtCore.QRect(0, 30, 392, 161))
		self.recvEdit.setObjectName("recvEdit")
		self.sendEdit = QtWidgets.QTextEdit(TcpTest)
		self.sendEdit.setGeometry(QtCore.QRect(0, 193, 392, 166))
		self.sendEdit.setObjectName("sendEdit")
		self.addrEdit = QtWidgets.QLineEdit(TcpTest)
		self.addrEdit.setGeometry(QtCore.QRect(40, 6, 141, 21))
		self.addrEdit.setObjectName("addrEdit")
		self.portEdit = QtWidgets.QLineEdit(TcpTest)
		self.portEdit.setGeometry(QtCore.QRect(223, 6, 151, 21))
		self.portEdit.setObjectName("portEdit")
		self.addrlabel = QtWidgets.QLabel(TcpTest)
		self.addrlabel.setGeometry(QtCore.QRect(6, 7, 62, 15))
		self.addrlabel.setObjectName("addrlabel")
		self.portlabel = QtWidgets.QLabel(TcpTest)
		self.portlabel.setGeometry(QtCore.QRect(190, 8, 62, 14))
		self.portlabel.setObjectName("portlabel")
		self.exitBt = QtWidgets.QPushButton(TcpTest)
		self.exitBt.setGeometry(QtCore.QRect(245, 360, 71, 28))
		self.exitBt.setObjectName("exitBt")
		self.clearBt = QtWidgets.QPushButton(TcpTest)
		self.clearBt.setGeometry(QtCore.QRect(171, 360, 71, 28))
		self.clearBt.setObjectName("clearBt")

		self.retranslateUi(TcpTest)
		self.sendBt.clicked.connect(self.tcp_connect)
		self.clearBt.clicked.connect(self.clearText)
		self.exitBt.clicked.connect(TcpTest.close)
		QtCore.QMetaObject.connectSlotsByName(TcpTest)
		
	def retranslateUi(self, TcpTest):
		_translate = QtCore.QCoreApplication.translate
		TcpTest.setWindowTitle("TcpTest - Client")
		TcpTest.setWindowIcon(QIcon('tcptest.ico'))
		self.sendBt.setText("Send")
		self.sendEdit.setText('{"cmd":48}\n')
		self.addrEdit.setText(socket.gethostbyname(socket.gethostname()))
		self.portEdit.setText("60001")
		self.addrlabel.setText("Addr")
		self.portlabel.setText("Port")
		self.exitBt.setText("Exit")
		self.clearBt.setText("Clear")
		self.sendEdit.setPlaceholderText("Send to server...")
		self.recvEdit.setPlaceholderText("Receive from server...")

	def clearText(self):
		self.sendEdit.clear()
		self.recvEdit.clear()
		
	def tcp_connect(self):
		def TcpClient(addr, port, data):
			buffsize = 2048
			try:
				tcp_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
				tcp_client.connect((addr, port))
				tcp_client.send(data.encode())
				recv_data = tcp_client.recv(buffsize).decode()
				tcp_client.close()
			except socket.error:
				print('TcpClient: fail to setup socket connection.')
				recv_data = None
			return recv_data

		addr = self.addrEdit.text()
		port = int(self.portEdit.text())
		send_data = self.sendEdit.toPlainText()
		recv_data = TcpClient(addr, port, send_data)
		if (recv_data != '') & (recv_data != None):
			self.recvEdit.append(recv_data)