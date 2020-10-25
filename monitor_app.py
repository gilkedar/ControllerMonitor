
from ui.ControllerMonitor import ControllerMonitor
from PyQt5 import QtGui
import sys
import os


class ControllerMonitorManager:

    def __init__(self, app):
        self.ui = ControllerMonitor(app)

        self.visualization_thread = None
        self.live_feed_mode = False
        self.frame_player_mode = False


    def closeEvent(self):
        print("\n\nShutting Down Resources..please Wait..")
        self.live_feed_mode = False
        os.system("pkill -9 rviz")


def main():
    app = QtGui.QApplication(sys.argv)

    manager = ControllerMonitorManager(app)

    manager.ui.set_manager_obj(manager)

    manager.ui.init_gui_resources()

    manager.ui.show()

    app.aboutToQuit.connect(manager.closeEvent)

    sys.exit(app.exec_())


if __name__ == "__main__":
    main()





