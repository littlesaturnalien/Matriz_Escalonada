from views.message_box import warning_box
from models.GaussJordan import GaussJordan
from PySide6.QtCore import Slot
from PySide6.QtWidgets import QTableWidgetItem
from random import randint

class MatrixController():
    def __init__(self, view, model: GaussJordan):
        self.__view = view
        self.__model = model
        self.connect_buttons()
    def connect_buttons(self):
        self.__view.table_update_button.clicked.connect(self.resize_matrix)
        self.__view.table_fill_0_button.clicked.connect(self.fill_matrix_0)
        self.__view.table_clean_matrix_button.clicked.connect(self.clean_matrix)
        self.__view.table_random_matrix_button.clicked.connect(self.random_matrix)

    @Slot()
    def resize_matrix(self):
        columns = self.__view.column_spinbox.value()
        rows = self.__view.row_spinbox.value()
        if rows <=1 or columns <=1:
            warning_box('No es posible redimensionar esta matriz.')
            return
        self.__view.table.setRowCount(rows)
        self.__view.table.setColumnCount(columns)
        for row in range(rows-1):
            table_header:QTableWidgetItem = self.__view.table.horizontalHeaderItem(row)
            table_header.setText(row+1)
        for col in range(columns-2):
            table_header:QTableWidgetItem = self.__view.table.verticalHeaderItem(col)
            table_header.setText(f'X{col+1}')
        self.__view.table.verticalHeaderItem(columns).setText('b')

    @Slot()
    def clean_matrix(self):
        for row in range(self.__view.table.rowCount()-1):
            for col in range(self.__view.table.columnCount()-1):
                table_widget = self.__view.table.item(row,col)
                table_widget.setText("")
    @Slot()
    def fill_matrix_0(self):
        for row in range(self.__view.table.rowCount()-1):
            for col in range(self.__view.table.columnCount()-1):
                table_widget:QTableWidgetItem = self.__view.table.item(row,col)
                if table_widget.text() !='':continue
                table_widget.setText('0')
    @Slot()
    def random_matrix(self):
        for row in range(self.__view.table.rowCount()-1):
            for col in range(self.__view.table.columnCount()-1):
                table_widget:QTableWidgetItem = self.__view.table.item(row,col)
                if table_widget.text() !='':continue
                table_widget.setText(str(randint(-99,99)))
    

    
        
