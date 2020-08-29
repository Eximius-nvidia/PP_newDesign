import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication,QDialog

from Broker_settings_ui import Ui_Dialog
from database_interface import SQL_Interface

class MyDialog(QtWidgets.QMainWindow):
    """
    doc
    """
    def __init__(self):
        """
        doc
        """
        super(MyDialog, self).__init__()
        self.ui1 = Ui_Dialog()
        self.ui1.setupUi(self)
        self.db_object = SQL_Interface()
        self.load_settings()

    def load_settings(self):
        """
        doc
        :return:
        """
        settings = self.db_object.get_settings()
        self.ui1.host_path.setText("sdfsdf")
        self.ui1.host_path.text= "sfsdfds"
        return
        # import pdb;pdb.set_trace()
        self.ui1.host_path.setText(settings[1])
        self.ui1.port_path.setText(str(settings[2]))

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = MyDialog()
    ui.ui1.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())