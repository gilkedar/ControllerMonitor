from utils.modules.usb_parser import UsbParser
from utils.modules.terminal import Terminal
from utils.errors.controller_errors import ErrControllerConnect
from utils.helpers.singleton import Singleton


class Controller(metaclass=Singleton):

    USB_NAME = "controller"

    def __init__(self):
        self.connected = False

    def connect(self, port_num):
        if not port_num:
            port_num = UsbParser().get_usb_port(Controller.USB_NAME)

        ans = Terminal().run("connection")
        if "success" not in ans:
            raise ErrControllerConnect("Could not connect to controller")

        self.connected = True

    def disconnect(self):
        self.connected = False

    def send_command(self, command):
        if not self.connected:
            raise ErrControllerConnect("Controller is not connected")
        ans = Terminal().run(command)
        return ans
