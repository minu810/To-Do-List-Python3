from PyQt5.QtWidgets import QDialog, QTabWidget, QVBoxLayout, QDialogButtonBox
from PyQt5.QtGui import QIcon

from Tab.FirstTab import FirstTab
from Tab.SecondTab import SecondTab
from Tab.ThirdTab import ThirdTab


class ToDoList(QDialog):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        tabs = QTabWidget()
        tabs.addTab(FirstTab(), QIcon('exit.png'), 'First')
        tabs.addTab(SecondTab(), QIcon('edit.png'), 'Second')
        tabs.addTab(ThirdTab(), 'Third')

        buttonbox = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        buttonbox.accepted.connect(self.accept)
        buttonbox.rejected.connect(self.reject)

        vbox = QVBoxLayout()
        vbox.addWidget(tabs)
        vbox.addWidget(buttonbox)

        self.setLayout(vbox)

        self.setWindowTitle('QTabWidget')
        self.setGeometry(300, 300, 400, 300)
        self.show()
