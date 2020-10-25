from ui.ui_files.ControllerMonitorGUI import Ui_ControllerMonitorWindow
from pyqtgraph.Qt import QtWidgets
from PyQt5.QtWidgets import QDesktopWidget
from PyQt5.QtCore import Qt

from utils.modules.controller import Controller
from utils.modules.usb_parser import UsbParser

from utils.helpers.logger import Logger
from utils import config
from utils.helpers import helper_functions

from utils.errors.controller_errors import ErrControllerConnect


class ControllerMonitor(QtWidgets.QMainWindow, Ui_ControllerMonitorWindow):

    STATUS_BAR_ACTIVE_MSG = "Controller Monitor Active"

    def __init__(self, app, parent=None):
        super(ControllerMonitor, self).__init__(parent)

        self.app = app
        self.manager_obj = None
        self.current_status_bar_msg = ""

        self.controller = Controller()

        self.session_start_time = helper_functions.get_current_time()
        self.logger = Logger(self.__class__.__name__, config.LOGS_PATH )

    def init_gui_resources(self):

        self.logger.info("\n------ Initializing GUI resources ------\n")

        self.setupUi(self)
        self.set_size()
        self.center()
        self.set_actions()
        self.set_initial_gui_settings()

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def set_size(self):

        self.setFixedSize(2200, 1500)

    def set_initial_gui_settings(self):

        self.line_edit_terminal.setText("Type desired command and press Enter")
        self.disable_terminal()
        self.set_status_bar_msg(self.STATUS_BAR_ACTIVE_MSG)
        self.set_ports_combo_box()

    def set_actions(self):
        self.app.aboutToQuit.connect(self.program_terminate_callback)
        self.btn_connect_controller.clicked.connect(self.callback_btn_connect)
        self.line_edit_terminal.keyReleaseEvent = self.keyPressEvent
        self.btn_execute_script.clicked.connect(self.callback_btn_run_script)

    def set_manager_obj(self, manager):
        self.manager_obj = manager

    def program_terminate_callback(self):
        self.logger.info("\n\nTerminating Program...")
        self.close()

    def send_command_to_controller(self, command):
        try:
            ans = self.controller.send_command(command)
        except ErrControllerConnect as ex:
            self.logger.error(ex)
            self.create_pop_up_info_message("Connection Error", "Controller is not connected")
            return str(ex)

        return ans

    # ------------------------ Generic GUI Functions -------------------

    @staticmethod
    def create_pop_up_info_message(header, msg_str):
        msg = QtWidgets.QMessageBox()
        msg.setIcon(QtWidgets.QMessageBox.Information)
        msg.setText(msg_str)
        msg.setWindowTitle(header)
        msg.setStandardButtons(QtWidgets.QMessageBox.Ok)

        msg.exec_()

    @staticmethod
    def create_pop_up_question(header, msg_str):
        msg = QtWidgets.QMessageBox()
        msg.setIcon(QtWidgets.QMessageBox.Information)
        msg.setText(msg_str)
        msg.setWindowTitle(header)
        msg.setStandardButtons(QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
        if msg.exec_() == QtWidgets.QMessageBox.Yes:
            return True
        return False

    def set_status_bar_msg(self, msg):

        if msg != self.current_status_bar_msg:
            self.logger.info("    [statusBar]  " + msg)

        self.statusBar().showMessage(msg)
        self.current_status_bar_msg = msg
        self.app.processEvents()

    # ------------------------ GUI Options   ----------------------------

    def disable_terminal(self):
        self.widget_terminal.setDisabled(True)

    def enable_terminal(self):
        self.widget_terminal.setEnabled(True)

    def disable_connection(self):
        self.frame_connect.setDisabled(True)

    def enable_connection(self):
        self.frame_connect.setEnabled(True)

    def set_ports_combo_box(self):

        available_ports = UsbParser().get_available_usb_ports()
        self.combo_select_port.clear()
        self.combo_select_port.addItem("Select USB Port")
        self.combo_select_port.addItems(available_ports)

    def set_text_on_terminal_output(self, txt):
        self.text_edit_terminal_output.clear()
        self.text_edit_terminal_output.setPlainText(txt)

    # ------------------------ GUI Callbacks ----------------------------

    def callback_btn_connect(self):
        selected_usb = self.combo_select_port.currentText()

        self.logger.info("Connecting to controller on port: {}".format(selected_usb))

        try:
            self.controller.connect(selected_usb)
        except ErrControllerConnect as ex:
            self.logger.error(ex)
            self.create_pop_up_info_message("Connection Error", "Selected port is invalid")
            # return

        self.enable_terminal()
        self.disable_connection()
        self.statusBar().showMessage("Connected to controller successfully")

    def callback_line_edit_terminal(self):
        curr_txt = self.line_edit_terminal.text()
        ans = self.send_command_to_controller(curr_txt)
        self.set_text_on_terminal_output(ans)

    def callback_btn_run_script(self):
        commands = self.text_edit_script.toPlainText().split(";")
        self.logger.info("Running Script")
        for i, cmd in enumerate(commands):
            self.logger.info(f"{i} - {cmd}")
            ans = self.send_command_to_controller(cmd)
            self.set_text_on_terminal_output(ans)

    def keyPressEvent(self, e):
        if e.key() == Qt.Key_Return or e.key() == Qt.Key_Enter:
            self.callback_line_edit_terminal()

