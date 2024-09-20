from views.ui_main_window import Ui_MainWindow
from models.GaussJordan import GaussJordan
from controller.controller import MatrixController
from PySide6.QtWidgets import QMainWindow, QApplication
from sys import argv, exit

class MainWindow(QMainWindow):
    def __init__(self, view:Ui_MainWindow):
        super().__init__()
        self.view = view
        self.view.setupUi(self)
        self.controller = MatrixController(self.view)

if __name__ == '__main__':
    app = QApplication(argv)
    window = MainWindow(Ui_MainWindow())
    window.show()
    exit(app.exec())
