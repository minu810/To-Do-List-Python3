from PyQt5.QtWidgets import *

from BaseTab import BaseTab

class SecondTab(BaseTab):
    def initUI(self):

        lan_group = QGroupBox('Select Your Language')
        combo = QComboBox()
        list = ['Korean', 'English', 'Chinese']
        combo.addItems(list)

        vbox1 = QVBoxLayout()
        vbox1.addWidget(combo)
        lan_group.setLayout(vbox1)

        learn_group = QGroupBox('Select What You Want To Learn')
        korean = QCheckBox('Korean')
        english = QCheckBox('English')
        chinese = QCheckBox('Chinese')

        vbox2 = QVBoxLayout()
        vbox2.addWidget(korean)
        vbox2.addWidget(english)
        vbox2.addWidget(chinese)
        learn_group.setLayout(vbox2)

        vbox = QVBoxLayout()
        vbox.addWidget(lan_group)
        vbox.addWidget(learn_group)
        self.setLayout(vbox)
