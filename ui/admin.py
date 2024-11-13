from PyQt6 import QtWidgets, uic
import sys

# from PyQt6.QtWidgets.QWidget import window


class app5F(QtWidgets.QMainWindow):
    def __init__(self):
        super(app5F,self).__init__()
        uic.loadUi('admin.ui',self)

if __name__ == "__main__":
    aplikasiku = QtWidgets.QApplication(sys.argv)
    jendela = app5F()
    jendela.show()

    sys.exit(aplikasiku.exec())