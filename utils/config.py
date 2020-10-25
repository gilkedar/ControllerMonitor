import os

MONITOR_VERSION = "1.0"
PROJECT_NAME = "ControllerMonitor"

WORKSPACE_PATH = os.path.dirname(os.path.abspath(os.curdir))
PROJECT_PATH = os.path.join(WORKSPACE_PATH,PROJECT_NAME)
LOGS_PATH = os.path.join(PROJECT_PATH, "logs")
