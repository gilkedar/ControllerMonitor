from utils.modules.terminal import Terminal


class UsbParser:

    def __init__(self):
        pass

    def get_available_usb_ports(self):
        t = Terminal()
        ans = t.run("lsusb")
        return ans.split("\n")

    def get_usb_port(self, device_name):
        t = Terminal()
        ans = t.run("lsusb")
        for line in ans:
            if device_name in line:
                return line
