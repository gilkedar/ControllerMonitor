

class ErrControllerConnect(Exception):

    def __init__(self, msg):
        super(ErrControllerConnect, self).__init__(f"Connection Error! {msg}")

