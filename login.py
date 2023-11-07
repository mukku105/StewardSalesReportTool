import sys
from PyQt6.QtWidgets import QApplication, QWidget, QMessageBox
from PyQt6.QtSql import QSqlDatabase, QSqlQuery, QSqlRecord
from PyQt6 import uic
from helpers import connection as con, authenticate as auth

class Login(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = uic.loadUi('loginUI.ui', self)

        self.ui.loginButton.clicked.connect(self.authenticate)

        self.show()

    def authenticate(self):
        self.username = self.usernameLineEdit.text()
        self.password = self.pswdLineEdit.text()

        if auth.auth_login(self.username, self.password):
            QMessageBox.information(self, 'Success', "Successfully Logged In!")
            return True
        else:
            QMessageBox.critical(self, 'Error', 'Invalid Credentials!')
            return False

if __name__ == '__main__':
    app = QApplication(sys.argv)
    if not con.createConnection():
        sys.exit(-1)
    login_window = Login()
    sys.exit(app.exec())

