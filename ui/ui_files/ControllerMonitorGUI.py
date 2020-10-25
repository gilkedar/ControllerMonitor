# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/gilkedar/workspace/ControllerMonitor/ui/ui_files/ControllerMonitorGUI.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_ControllerMonitorWindow(object):
    def setupUi(self, ControllerMonitorWindow):
        ControllerMonitorWindow.setObjectName("ControllerMonitorWindow")
        ControllerMonitorWindow.setEnabled(True)
        ControllerMonitorWindow.resize(2047, 1454)
        ControllerMonitorWindow.setMouseTracking(False)
        self.centralwidget = QtWidgets.QWidget(ControllerMonitorWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(10, 30, 1981, 1341))
        self.tabWidget.setObjectName("tabWidget")
        self.tab_communicator = QtWidgets.QWidget()
        self.tab_communicator.setObjectName("tab_communicator")
        self.widget_terminal = QtWidgets.QWidget(self.tab_communicator)
        self.widget_terminal.setGeometry(QtCore.QRect(20, 360, 1771, 901))
        self.widget_terminal.setObjectName("widget_terminal")
        self.text_edit_terminal_output = QtWidgets.QPlainTextEdit(self.widget_terminal)
        self.text_edit_terminal_output.setGeometry(QtCore.QRect(20, 230, 711, 641))
        self.text_edit_terminal_output.setObjectName("text_edit_terminal_output")
        self.text_edit_script = QtWidgets.QPlainTextEdit(self.widget_terminal)
        self.text_edit_script.setGeometry(QtCore.QRect(910, 220, 711, 661))
        self.text_edit_script.setObjectName("text_edit_script")
        self.label_3 = QtWidgets.QLabel(self.widget_terminal)
        self.label_3.setGeometry(QtCore.QRect(20, 160, 291, 41))
        self.label_3.setObjectName("label_3")
        self.line_edit_terminal = QtWidgets.QLineEdit(self.widget_terminal)
        self.line_edit_terminal.setGeometry(QtCore.QRect(20, 90, 711, 41))
        self.line_edit_terminal.setObjectName("line_edit_terminal")
        self.label_2 = QtWidgets.QLabel(self.widget_terminal)
        self.label_2.setGeometry(QtCore.QRect(20, 20, 291, 41))
        self.label_2.setObjectName("label_2")
        self.btn_execute_script = QtWidgets.QPushButton(self.widget_terminal)
        self.btn_execute_script.setGeometry(QtCore.QRect(900, 80, 231, 46))
        self.btn_execute_script.setObjectName("btn_execute_script")
        self.label_4 = QtWidgets.QLabel(self.widget_terminal)
        self.label_4.setGeometry(QtCore.QRect(900, 20, 291, 41))
        self.label_4.setObjectName("label_4")
        self.frame_connect = QtWidgets.QFrame(self.tab_communicator)
        self.frame_connect.setGeometry(QtCore.QRect(30, 50, 721, 241))
        self.frame_connect.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_connect.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_connect.setObjectName("frame_connect")
        self.label_5 = QtWidgets.QLabel(self.frame_connect)
        self.label_5.setGeometry(QtCore.QRect(10, 10, 291, 41))
        self.label_5.setObjectName("label_5")
        self.combo_select_port = QtWidgets.QComboBox(self.frame_connect)
        self.combo_select_port.setGeometry(QtCore.QRect(20, 80, 691, 41))
        self.combo_select_port.setObjectName("combo_select_port")
        self.btn_connect_controller = QtWidgets.QPushButton(self.frame_connect)
        self.btn_connect_controller.setGeometry(QtCore.QRect(20, 150, 221, 46))
        self.btn_connect_controller.setObjectName("btn_connect_controller")
        self.tabWidget.addTab(self.tab_communicator, "")
        self.tab_graph = QtWidgets.QWidget()
        self.tab_graph.setObjectName("tab_graph")
        self.widget = QtWidgets.QWidget(self.tab_graph)
        self.widget.setGeometry(QtCore.QRect(20, 70, 1791, 971))
        self.widget.setObjectName("widget")
        self.btn_fetch_new_data = QtWidgets.QPushButton(self.widget)
        self.btn_fetch_new_data.setGeometry(QtCore.QRect(50, 60, 281, 46))
        self.btn_fetch_new_data.setObjectName("btn_fetch_new_data")
        self.graphicsView = QtWidgets.QGraphicsView(self.widget)
        self.graphicsView.setGeometry(QtCore.QRect(40, 160, 1531, 681))
        self.graphicsView.setObjectName("graphicsView")
        self.tabWidget.addTab(self.tab_graph, "")
        ControllerMonitorWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(ControllerMonitorWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 2047, 38))
        self.menubar.setObjectName("menubar")
        ControllerMonitorWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(ControllerMonitorWindow)
        self.statusbar.setObjectName("statusbar")
        ControllerMonitorWindow.setStatusBar(self.statusbar)

        self.retranslateUi(ControllerMonitorWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(ControllerMonitorWindow)

    def retranslateUi(self, ControllerMonitorWindow):
        _translate = QtCore.QCoreApplication.translate
        ControllerMonitorWindow.setWindowTitle(_translate("ControllerMonitorWindow", "ControllerMonitor"))
        self.label_3.setText(_translate("ControllerMonitorWindow", "Ouput"))
        self.label_2.setText(_translate("ControllerMonitorWindow", "Teminal Command"))
        self.btn_execute_script.setText(_translate("ControllerMonitorWindow", "Execute Script"))
        self.label_4.setText(_translate("ControllerMonitorWindow", "Script Runner"))
        self.label_5.setText(_translate("ControllerMonitorWindow", "Connect To Controller"))
        self.btn_connect_controller.setText(_translate("ControllerMonitorWindow", "Connect"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_communicator), _translate("ControllerMonitorWindow", "Communicator"))
        self.btn_fetch_new_data.setText(_translate("ControllerMonitorWindow", "Fetch New Data"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_graph), _translate("ControllerMonitorWindow", "Graph"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ControllerMonitorWindow = QtWidgets.QMainWindow()
    ui = Ui_ControllerMonitorWindow()
    ui.setupUi(ControllerMonitorWindow)
    ControllerMonitorWindow.show()
    sys.exit(app.exec_())

