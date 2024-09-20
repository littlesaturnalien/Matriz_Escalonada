from views.message_box import warning_box
from views.ui_main_window import Ui_MainWindow 
from views.ui_solution_window import Ui_main_widget as Ui_solution
from views.ui_vector_window import Ui_main_widget as Ui_vector
from models.GaussJordan import GaussJordan
from PySide6.QtCore import Slot
from PySide6.QtWidgets import QTableWidgetItem,QMainWindow,QWidget
from random import randint

class MatrixController():
    def __init__(self):
        self.main_window = Ui_MainWindow()
        self.connect_main_window_buttons()
        self.fill_table_widgets()
        self.main_window.input_table.resizeColumnsToContents()
        
    def connect_main_window_buttons(self):
        self.main_window.table_update_button.clicked.connect(self.main_window.resize_matrix)
        self.main_window.table_fill_0_button.clicked.connect(self.main_window.fill_matrix_0)
        self.main_window.table_clean_matrix_button.clicked.connect(self.main_window.clean_matrix)
        self.main_window.table_random_matrix_button.clicked.connect(self.main_window.random_matrix)
        self.main_window.table_solve_matrix_button.clicked.connect(self.main_window.solution_tab)

    @Slot()
    def solution_tab(self):
        matriz = self.main_window.generate_matrix()
        if matriz == None:
            warning_box("No se pudo generar esta tabla")
            return
        if not MatrixController.__valid_matriz(matriz):
            return
        op_solution = self.main_window.table_solution_matrix_combobox.currentData()
        match op_solution:
            case 'reduccion':
                self.open_solution_window(GaussJordan(matriz))
            case 'vxv':
                self.open_vector_window(GaussJordan(matriz))
                pass
            case _:
                warning_box("Seleccione una opcion para resolver")

    def open_solution_window(self,matrix: GaussJordan):
        self.solution_window = Ui_solution()
        self.window = QWidget()
        self.solution_window.setupUi(self.window)
        self.window.setWindowTitle(u'Solución detallada')
        self.solution_window.create_tab_solutions(matrix.gauss_jordan())
        self.connect_solution_window_buttons()
        self.window.show()

    @Slot()
    def connect_solution_window_buttons(self):
        self.solution_window.tabWidget.currentChanged.connect(self.show_step_property)
        self.solution_window.next_tab_button.clicked.connect(self.next_tab)
        self.solution_window.back_tab_button.clicked.connect(self.previous_tab)

    def open_vector_window(self,matriz:GaussJordan):
        self.vector_window = Ui_vector(matriz.matriz)
        self.window = QWidget()
        self.vector_window.setupUi(self.window)
        self.connect_vector_window_buttons()
        self.window.show()
    
    def connect_vector_window_buttons(self):
        self.vector_window.vxv_row_spinbox.valueChanged.connect(self.change_row_vector)
        self.vector_window.vxv_solve_scalar_button.clicked.connect(self.get_scalar)

    @Slot()
    def change_row_vector(self): # Continue here
        row_number = self.vector_window.vxv_row_spinbox.value()
        if row_number <= 0:
            self.vector_window.vxv_row_spinbox.setValue(0)
            return;
        if row_number > len(self.vector_window.matrix_instance): 
            self.vector_window.vxv_row_spinbox.setValue(row_number-1)
            return
        self.vector_window.set_vector_row(self.vector_window.matrix_instance[row_number-1])
    @Slot()
    def get_scalar(self):
        column_vector = self.get_vxv_column_vector()
        if column_vector is None:return
        row_vector = self.get_vxv_row_vector()
        if row_vector is None: return
        scalar = GaussJordan.get_scalar(row_vector,column_vector)
        row = self.vector_window.vxv_row_spinbox.value()
        self.vector_window.scalar_label.setText(f'Vector fila {row} X vector columna b: {scalar}')

    def get_vxv_column_vector(self):
        vector = list()
        for row in range(self.vector_window.vxv_column_vector.rowCount()):
            table_item = self.vector_window.vxv_column_vector.item(row,0)
            if table_item is None:
                warning_box('Vector columna incompleto')
                return
            try:
                vector.append(float(table_item.text()))
            except ValueError:
                warning_box(f'Fila {row+1}: {table_item.text()} no es un número')
                return
            except Exception as e:
                warning_box(f'Error inesperado: {e}')
                return
        return vector
    
    def get_vxv_row_vector(self):
        vector = list()
        for column in range(self.vector_window.vxv_row_vector.columnCount()):
            table_item = self.vector_window.vxv_row_vector.item(0,column)
            try:
                vector.append(float(table_item.text()))
            except Exception as e:
                warning_box(f'Error inesperado: {e}')
                return
        return vector
    
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