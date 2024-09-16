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


'''
from models.GaussJordan import GaussJordan as GJ

def main():
    filas = int(input("Ingresa la cantidad de filas de la matriz: "))
    columnas = int(input("Ingresa la cantidad de columnas de la matriz: "))
    matriz = GJ.crear_matriz(filas, columnas)
    
    print("\nSISTEMA DE ECUACIONES INGRESADO\n")
    matriz_aumentada = GJ(matriz)
    matriz_aumentada.imprimir_ecuaciones()

    print("\nMATRIZ A RESOLVER:\n")
    for fila in matriz:
        for valor in fila:
            print(f"{int(valor) if valor.is_integer() else f'{valor:.1f}'}", end = " ")
        print()
    
    matriz_aumentada.gauss_jordan()
    matriz_aumentada.soluciones()

if __name__ == '__main__':
    main()

    '''