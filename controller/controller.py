from views.message_box import warning_box,information_box
from views.ui_main_window import Ui_MainWindow
from views.ui_solution_window import Ui_main_widget as Ui_solution
from models.GaussJordan import GaussJordan
from PySide6.QtCore import Slot
from PySide6.QtWidgets import QTableWidgetItem,QMainWindow,QWidget
from random import randint

class MatrixController():
    def __init__(self, view:Ui_MainWindow, model=None):
        self.__view = view
        self.__model = model
        self.connect_buttons()
        self.fill_table_widgets()
        self.__view.input_table.resizeColumnsToContents()
    def connect_buttons(self):
        self.__view.table_update_button.clicked.connect(self.resize_matrix)
        self.__view.table_fill_0_button.clicked.connect(self.fill_matrix_0)
        self.__view.table_clean_matrix_button.clicked.connect(self.clean_matrix)
        self.__view.table_random_matrix_button.clicked.connect(self.random_matrix)
        self.__view.table_solve_matrix_button.clicked.connect(self.solution_tab)
    @Slot()
    def resize_matrix(self):
        columns = self.__view.column_spinbox.value()
        rows = self.__view.row_spinbox.value()
        if rows <=1 or columns <=1:
            warning_box('No es posible redimensionar esta matriz.')
            return
        self.__view.column_spinbox.setValue(0)
        self.__view.row_spinbox.setValue(0)
        self.__view.input_table.setRowCount(rows)
        self.__view.input_table.setColumnCount(columns)
        for row in range(rows):
            table_header = self.__view.input_table.verticalHeaderItem(row)
            if table_header is None:
                table_header = QTableWidgetItem()
                self.__view.input_table.setVerticalHeaderItem(row,table_header)
            table_header.setText(str(row+1))
        for col in range(columns-1):
            table_header = self.__view.input_table.horizontalHeaderItem(col)
            if table_header is None:
                table_header = QTableWidgetItem()
                self.__view.input_table.setHorizontalHeaderItem(col, table_header)
            table_header.setText(f'X{col+1}')

        last_column_header = self.__view.input_table.horizontalHeaderItem(columns - 1)
        if last_column_header is None:
            last_column_header = QTableWidgetItem()
            self.__view.input_table.setHorizontalHeaderItem(columns - 1, last_column_header)
        last_column_header.setText('b')
        self.fill_table_widgets()
        self.__view.input_table.resizeColumnsToContents()
        

    @Slot()
    def clean_matrix(self):
        for row in range(self.__view.input_table.rowCount()):
            for col in range(self.__view.input_table.columnCount()):
                table_widget = self.__view.input_table.item(row,col)
                if table_widget is None:
                    table_widget = QTableWidgetItem("")  # Crear nuevo item si no existe
                    self.__view.input_table.setItem(row, col, table_widget)
                table_widget.setText("")
    @Slot()
    def fill_matrix_0(self):
        for row in range(self.__view.input_table.rowCount()):
            for col in range(self.__view.input_table.columnCount()):
                table_widget:QTableWidgetItem = self.__view.input_table.item(row,col)
                if table_widget.text() !='':continue
                table_widget.setText('0')
    @Slot()
    def random_matrix(self):
        for row in range(self.__view.input_table.rowCount()):
            for col in range(self.__view.input_table.columnCount()):
                table_widget:QTableWidgetItem = self.__view.input_table.item(row,col)
                if table_widget.text() !='':continue
                table_widget.setText(str(randint(-99,99)))
    @Slot()
    def fill_table_widgets(self):
        for row in range(self.__view.input_table.rowCount()):
            for col in range(self.__view.input_table.columnCount()):
                table_widget = self.__view.input_table.item(row,col)
                if table_widget is None: 
                    table_widget =QTableWidgetItem()
                    self.__view.input_table.setItem(row,col,table_widget)

    @Slot()
    def solution_tab(self):
        #content = [list(map(float, row)) for row in content]
        matriz = self.generate_matrix()
        if matriz == None:
            warning_box("No se pudo generar esta tabla")
            return
        if not MatrixController.__valid_matriz(matriz):
            return
        self.open_solution_window(GaussJordan(matriz))
    
    def generate_matrix(self) ->list[list] | None:
        matriz = []
        for row in range(self.__view.input_table.rowCount()):
            row_ = []
            for col in range(self.__view.input_table.columnCount()):
                table_widget = self.__view.input_table.item(row,col)
                if table_widget is None: return None
                try:
                    num = float(table_widget.text())
                except ValueError:
                    return None
                row_.append(num)
            matriz.append(row_)
        return matriz
    
    @staticmethod
    def __valid_matriz(matriz: list[list]) ->bool:
        if matriz == []:
            warning_box('La matriz ingresada es invalida')
            return False
        width = len(matriz)
        length = len(matriz[0])
        for row in range(width):
            if all(matriz[row][col] == 0 for col in range(length-1)) and matriz[row][-1] !=0:
                warning_box("La matriz ingresada no tiene solucion")
                return False
            if len(matriz[row]) != length:
                warning_box('La matriz ingresada esta incompleta')
                return False
        return True

    class SolutionWindow(QMainWindow, Ui_solution):
        def __init__(self):
            super().__init__()
            self.setupUi(self)  

    def open_solution_window(self,matrix: GaussJordan):
        self.solution_window = Ui_solution()
        self.window = QWidget()
        self.solution_window.setupUi(self.window)
        self.solution_window.create_tab_solutions(matrix.gauss_jordan())
        self.window.show()
                





    

    
        
