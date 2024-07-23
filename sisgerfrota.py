from PyQt5.QtWidgets import QApplication, QDialog, QMainWindow, QMessageBox
import sys
from login import Ui_Dialog
from areatrab import Ui_MainWindow

class LoginDialog(QDialog):
    def __init__(self, *args, **kwargs):
        super(LoginDialog, self).__init__(*args, **kwargs)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.handle_login)

    def handle_login(self):
        admin = "admin"
        senha = "admin"
        user = self.ui.lineEdit.text()
        pwd = self.ui.lineEdit_2.text()
        if user == admin and pwd == senha:
            self.accept()
        else:
            self.show_error_message("Usuário ou senha incorretos")

    def show_error_message(self, message):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Critical)
        msg.setWindowTitle("Erro de Login")
        msg.setText(message)
        msg.setStandardButtons(QMessageBox.Ok)
        msg.exec_()

class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

app = QApplication(sys.argv)

# Cria e exibe o diálogo de login
login_dialog = LoginDialog()
if login_dialog.exec_() == QDialog.Accepted:
    # Se o login for aceito, abre a janela principal
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())
else:
    sys.exit()
