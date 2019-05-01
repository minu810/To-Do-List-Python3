from PyQt5.QtWidgets import QWidget

class BaseTab(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        pass
