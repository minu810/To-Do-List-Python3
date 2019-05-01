import sys
from PyQt5.QtWidgets import QApplication

from ToDoList import ToDoList

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = ToDoList()
    sys.exit(app.exec_())
