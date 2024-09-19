from views.message_box import warning_box
from views.ui_main_window import Ui_MainWindow
from views.ui_solution_window import Ui_main_widget as Ui_solution
from views.ui_vector_window import Ui_main_widget as Ui_vector
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
        if rows <=0 or columns <=0:
            warning_box('No es posible redimensionar esta matriz.')
            return
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
        matriz = self.generate_matrix()
        if matriz == None:
            warning_box("No se pudo generar esta tabla")
            return
        if not MatrixController.__valid_matriz(matriz):
            return
        op_solution = self.__view.table_solution_matrix_combobox.currentData()
        match op_solution:
            case 'reduccion':
                self.open_solution_window(GaussJordan(matriz))
            case 'vxv':
                self.open_vector_window(GaussJordan(matriz))
                pass
            case _:
                warning_box("Seleccione una opcion para resolver")
                
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
        self.window.setWindowTitle(u'Solución detallada')
        self.solution_window.create_tab_solutions(matrix.gauss_jordan())
        self.connect_solution_window()
        self.window.show()

    @Slot()
    def connect_solution_window(self):
        self.solution_window.tabWidget.currentChanged.connect(self.show_step_property)
        self.solution_window.next_tab_button.clicked.connect(self.next_tab)
        self.solution_window.back_tab_button.clicked.connect(self.previous_tab)
    def show_step_property(self,index):
        step = self.solution_window.tabWidget.currentWidget().property('step_data')
        if step is not None:
            self.solution_window.label.setText(step)
            return
        self.solution_window.label.setText('Informacion no encontrada')

    @Slot()
    def destroy_solution_window(self):
        self.solution_window = None
        self.window = None

    @Slot()
    def previous_tab(self):
        current_index = self.solution_window.tabWidget.currentIndex()
        if current_index > 0:
            self.solution_window.tabWidget.setCurrentIndex(current_index-1)
    @Slot()
    def next_tab(self):
        current_index = self.solution_window.tabWidget.currentIndex()
        if current_index < self.solution_window.tabWidget.count()-1:
            self.solution_window.tabWidget.setCurrentIndex(current_index+1)

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


