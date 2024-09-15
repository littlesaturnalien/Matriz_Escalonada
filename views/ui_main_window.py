# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QGridLayout,
    QHBoxLayout, QHeaderView, QLabel, QMainWindow,
    QPushButton, QSizePolicy, QSpinBox, QStatusBar,
    QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(523, 276)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget_layout = QVBoxLayout(self.centralwidget)
        self.centralwidget_layout.setObjectName(u"centralwidget_layout")
        self.table_widget = QWidget(self.centralwidget)
        self.table_widget.setObjectName(u"table_widget")
        self.verticalLayout_2 = QVBoxLayout(self.table_widget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.table_buttons_frame = QFrame(self.table_widget)
        self.table_buttons_frame.setObjectName(u"table_buttons_frame")
        self.table_buttons_frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.table_buttons_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.table_buttons_horizontal_layout = QHBoxLayout(self.table_buttons_frame)
        self.table_buttons_horizontal_layout.setObjectName(u"table_buttons_horizontal_layout")
        self.table_buttons_horizontal_layout.setContentsMargins(0, 0, 0, 0)
        self.table_row_spinbox_widget = QWidget(self.table_buttons_frame)
        self.table_row_spinbox_widget.setObjectName(u"table_row_spinbox_widget")
        self.table_row_spinbox_widget.setStyleSheet(u"")
        self.row_spinbox_vertical_layout = QVBoxLayout(self.table_row_spinbox_widget)
        self.row_spinbox_vertical_layout.setObjectName(u"row_spinbox_vertical_layout")
        self.row_spinbox_vertical_layout.setContentsMargins(9, 9, 9, 9)
        self.label = QLabel(self.table_row_spinbox_widget)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"border: 0")

        self.row_spinbox_vertical_layout.addWidget(self.label, 0, Qt.AlignmentFlag.AlignHCenter)

        self.row_spinbox = QSpinBox(self.table_row_spinbox_widget)
        self.row_spinbox.setObjectName(u"row_spinbox")
        self.row_spinbox.setStyleSheet(u"border-color: rgb(0, 0, 0);")

        self.row_spinbox_vertical_layout.addWidget(self.row_spinbox)


        self.table_buttons_horizontal_layout.addWidget(self.table_row_spinbox_widget)

        self.table_column_spinbox_widget = QWidget(self.table_buttons_frame)
        self.table_column_spinbox_widget.setObjectName(u"table_column_spinbox_widget")
        self.column_spinbox_vertical_layout = QVBoxLayout(self.table_column_spinbox_widget)
        self.column_spinbox_vertical_layout.setObjectName(u"column_spinbox_vertical_layout")
        self.column_spinbox_vertical_layout.setContentsMargins(9, 9, 9, 9)
        self.column_spinbox_label = QLabel(self.table_column_spinbox_widget)
        self.column_spinbox_label.setObjectName(u"column_spinbox_label")

        self.column_spinbox_vertical_layout.addWidget(self.column_spinbox_label, 0, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignVCenter)

        self.column_spinbox = QSpinBox(self.table_column_spinbox_widget)
        self.column_spinbox.setObjectName(u"column_spinbox")

        self.column_spinbox_vertical_layout.addWidget(self.column_spinbox, 0, Qt.AlignmentFlag.AlignHCenter)


        self.table_buttons_horizontal_layout.addWidget(self.table_column_spinbox_widget)

        self.table_grid_options = QGridLayout()
        self.table_grid_options.setObjectName(u"table_grid_options")
        self.table_grid_options.setHorizontalSpacing(6)
        self.table_grid_options.setContentsMargins(9, 9, 9, 9)
        self.table_fill_0_button = QPushButton(self.table_buttons_frame)
        self.table_fill_0_button.setObjectName(u"table_fill_0_button")
        self.table_fill_0_button.setStyleSheet(u"QPushButton{\n"
"border: 2px solid gray;\n"
"border-radius: 5px\n"
"}\n"
"QPushButton::hover{\n"
"background-color: #eee;\n"
"}\n"
"QPushButton::pressed{\n"
"background-color: #aaa\n"
"}")

        self.table_grid_options.addWidget(self.table_fill_0_button, 0, 1, 1, 1)

        self.table_clean_matrix_button = QPushButton(self.table_buttons_frame)
        self.table_clean_matrix_button.setObjectName(u"table_clean_matrix_button")
        self.table_clean_matrix_button.setStyleSheet(u"QPushButton{\n"
"border: 2px solid gray;\n"
"border-radius: 5px\n"
"}\n"
"QPushButton::hover{\n"
"background-color: #eee;\n"
"}\n"
"QPushButton::pressed{\n"
"background-color: #aaa;\n"
"}")

        self.table_grid_options.addWidget(self.table_clean_matrix_button, 1, 0, 1, 1)

        self.table_random_matrix_button = QPushButton(self.table_buttons_frame)
        self.table_random_matrix_button.setObjectName(u"table_random_matrix_button")
        self.table_random_matrix_button.setStyleSheet(u"QPushButton{\n"
"border: 2px solid gray;\n"
"border-radius: 5px\n"
"}\n"
"QPushButton::hover{\n"
"background-color: #eee;\n"
"}\n"
"QPushButton::pressed{\n"
"background-color: #aaa\n"
"}")

        self.table_grid_options.addWidget(self.table_random_matrix_button, 0, 2, 1, 1)

        self.table_update_button = QPushButton(self.table_buttons_frame)
        self.table_update_button.setObjectName(u"table_update_button")
        self.table_update_button.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.table_update_button.setStyleSheet(u"QPushButton{\n"
"border: 2px solid gray;\n"
"border-radius: 5px\n"
"}\n"
"QPushButton::hover{\n"
"background-color: #eee;\n"
"}\n"
"QPushButton::pressed{\n"
"background-color: #aaa\n"
"}")

        self.table_grid_options.addWidget(self.table_update_button, 0, 0, 1, 1)

        self.table_export_matrix_button = QPushButton(self.table_buttons_frame)
        self.table_export_matrix_button.setObjectName(u"table_export_matrix_button")
        self.table_export_matrix_button.setStyleSheet(u"QPushButton{\n"
"border: 2px solid gray;\n"
"border-radius: 5px\n"
"}\n"
"QPushButton::hover{\n"
"background-color: #eee;\n"
"}\n"
"QPushButton::pressed{\n"
"background-color: #aaa\n"
"}")

        self.table_grid_options.addWidget(self.table_export_matrix_button, 2, 0, 1, 1)

        self.table_solution_matrix_combobox = QComboBox(self.table_buttons_frame)
        self.table_solution_matrix_combobox.addItem("")
        self.table_solution_matrix_combobox.addItem("")
        self.table_solution_matrix_combobox.setObjectName(u"table_solution_matrix_combobox")
        self.table_solution_matrix_combobox.setStyleSheet(u"QPushButton{\n"
"border: 2px solid black;\n"
"border-radius: 5px\n"
"}\n"
"QPushButton::hover{\n"
"background-color: #eee;\n"
"}\n"
"QPushButton::pressed{\n"
"background-color: #aaa\n"
"}")

        self.table_grid_options.addWidget(self.table_solution_matrix_combobox, 1, 1, 1, 2)

        self.table_solve_matrix_button = QPushButton(self.table_buttons_frame)
        self.table_solve_matrix_button.setObjectName(u"table_solve_matrix_button")
        self.table_solve_matrix_button.setStyleSheet(u"QPushButton{\n"
"border: 2px solid gray;\n"
"border-radius: 5px;\n"
"}\n"
"QPushButton::hover{\n"
"background-color: #eee;\n"
"}\n"
"QPushButton::pressed{\n"
"background-color: #aaa\n"
"}")

        self.table_grid_options.addWidget(self.table_solve_matrix_button, 2, 1, 1, 2)


        self.table_buttons_horizontal_layout.addLayout(self.table_grid_options)

        self.table_buttons_horizontal_layout.setStretch(0, 5)
        self.table_buttons_horizontal_layout.setStretch(1, 5)
        self.table_buttons_horizontal_layout.setStretch(2, 100)

        self.verticalLayout_2.addWidget(self.table_buttons_frame)

        self.input_table = QTableWidget(self.table_widget)
        if (self.input_table.columnCount() < 3):
            self.input_table.setColumnCount(3)
        __qtablewidgetitem = QTableWidgetItem()
        self.input_table.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.input_table.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.input_table.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        if (self.input_table.rowCount() < 3):
            self.input_table.setRowCount(3)
        self.input_table.setObjectName(u"input_table")
        self.input_table.verticalHeader().setVisible(True)

        self.verticalLayout_2.addWidget(self.input_table)

        self.verticalLayout_2.setStretch(0, 1)
        self.verticalLayout_2.setStretch(1, 10)

        self.centralwidget_layout.addWidget(self.table_widget)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Calculadora de matrices", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Filas", None))
        self.column_spinbox_label.setText(QCoreApplication.translate("MainWindow", u"Columnas", None))
        self.table_fill_0_button.setText(QCoreApplication.translate("MainWindow", u"Rellenar espacios con 0", None))
        self.table_clean_matrix_button.setText(QCoreApplication.translate("MainWindow", u"Limpiar Matriz", None))
        self.table_random_matrix_button.setText(QCoreApplication.translate("MainWindow", u"Matriz aleatoria", None))
        self.table_update_button.setText(QCoreApplication.translate("MainWindow", u"Actualizar", None))
        self.table_export_matrix_button.setText(QCoreApplication.translate("MainWindow", u"Exportar Matriz", None))
        self.table_solution_matrix_combobox.setItemText(0, QCoreApplication.translate("MainWindow", u"Resolver por", None))
        self.table_solution_matrix_combobox.setItemText(1, QCoreApplication.translate("MainWindow", u"Reducci\u00f3n", None))

        self.table_solve_matrix_button.setText(QCoreApplication.translate("MainWindow", u"Resolver", None))
        ___qtablewidgetitem = self.input_table.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"X1", None));
        ___qtablewidgetitem1 = self.input_table.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"X2", None));
        ___qtablewidgetitem2 = self.input_table.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"b", None));
    # retranslateUi

