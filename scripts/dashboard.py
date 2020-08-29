import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication,QDialog

from broker_settings import MyDialog
from Dashboard_ui import Ui_MainWindow


class MyWindow(QtWidgets.QMainWindow):
    """

    """

    def __init__(self):
        """
        doc
        """
        super(MyWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # initial setup
        self.ui.actionExit.triggered.connect(self.trigger_exit)
        # self.ui.actionDisconnect.triggered.connect()
        # self.ui.actionConnect.triggered.connect()
        self.ui.actionBroker.triggered.connect(self.show_broker_settings_window)

        self.ui.actionDisconnect.setEnabled(False)

    def show_broker_settings_window(self):
        """
        doc
        :return:
        """
        # app = QtWidgets.QApplication(sys.argv)
        Dialog = QtWidgets.QDialog([])
        ui = MyDialog()
        ui.ui1.setupUi(Dialog)
        Dialog.show()
        sys.exit(self.exec_())


    def closeEvent(self, event):
        """

        :param event:
        :return:
        """
        pass

    def trigger_exit(self):
        """

        :param q:
        :return:
        """
        self.close()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    application = MyWindow()
    application.show()
    sys.exit(app.exec())