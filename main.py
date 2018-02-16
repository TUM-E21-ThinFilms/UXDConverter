from PyQt5 import QtCore, QtGui, QtWidgets
from gui import Ui_UXDConverter
from controller import Controller

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    UXDConverter = QtWidgets.QMainWindow()
    ui = Ui_UXDConverter()
    ui.setupUi(UXDConverter)
    UXDConverter.show()

    controller = Controller(ui, app)
    controller.run()
    sys.exit(app.exec_())

