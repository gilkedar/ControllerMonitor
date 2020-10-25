import logging
import os
import datetime


class Logger(logging.Logger):

    file_format = '%(asctime)s.%(msecs)3d %(levelname)-8s %(module)s - %(funcName)s: %(message)s'
    console_format = '%(asctime)s %(levelname)-8s %(name)-12s: %(message)s'
    date_format = '%Y-%m-%d %H:%M:%S'
    path = "Logs/"

    def __init__(self, name, file_path=None, log_level=logging.INFO, log_console=True):
        if not file_path:
            file_path = Logger.path
        if not os.path.exists(file_path):
            os.makedirs(file_path)

        run_time = datetime.datetime.now().strftime("%d-%m__%H-%M-%S")
        file_name = '{}/{}__{}.log'.format(file_path, name, run_time)

        logging.Logger.__init__(self, name)
        logging.basicConfig(
            filename=file_name,
            level=log_level,
            format=Logger.file_format,
            datefmt=Logger.date_format)

        if file_path:
            file_handler = logging.FileHandler(file_name)
            file_handler.setLevel(logging.DEBUG)
            formatter = logging.Formatter(Logger.file_format)
            file_handler.setFormatter(formatter)
            logging.Logger.addHandler(self, file_handler)

        if log_console:
            console = logging.StreamHandler()
            console.setLevel(logging.INFO)
            formatter = logging.Formatter(Logger.console_format)
            console.setFormatter(formatter)
            logging.Logger.addHandler(self, console)
