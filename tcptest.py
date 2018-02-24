import sys
from PyQt5.QtWidgets import QApplication , QMainWindow
from tcptestUI import *

if __name__ == '__main__':
	app = QApplication(sys.argv)
	mainWindow = QMainWindow()
	ui = Ui_TcpTest()
	ui.setupUi(mainWindow)
	mainWindow.show()
	sys.exit(app.exec_())