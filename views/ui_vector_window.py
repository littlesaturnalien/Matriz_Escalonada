# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'vector_window.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QHeaderView, QLabel,
    QPushButton, QSizePolicy, QSpacerItem, QSpinBox,
    QTabWidget, QTableWidget, QTableWidgetItem, QVBoxLayout,
    QWidget)
from views.QtFiles.qrc_files import resources_rc
from copy import deepcopy
class Ui_main_widget(object):
    def __init__(self,matrix:list[list]):
        self.matrix_instance = deepcopy(matrix)
    def setupUi(self, main_widget):
        if not main_widget.objectName():
            main_widget.setObjectName(u"main_widget")
        main_widget.setMaximumSize(500,500)
        main_widget.resize(370, 277)
        icon = QIcon()
        icon.addFile(u":/icon/Images/math.ico", QSize(), QIcon.Normal, QIcon.Off)
        main_widget.setWindowIcon(icon)
        main_widget.setStyleSheet(u"#main_widget{\n"
"background-color: #d3d3d3;\n"
"\n"
"}\n"
"QTabWidget:pane{\n"
"background-color: #d3d3d3\n"
"}\n"
"#vector_x_vector_widget{\n"
"background-color: #d3d3d3;\n"
"}\n"
"QTabBar::tab{\n"
"background-color: #80857C;\n"
"color: white;\n"
"}\n"
"\n"
"QTabBar::tab:hover{\n"
"background-color: #B0B3AD\n"
"}\n"
"\n"
"QTabBar::tab:selected{\n"
"background-color:#454742\n"
"}\n"
"\n"
"QSpinBox{\n"
"color: white;\n"
"background-color: #6c757d;\n"
"}\n"
"QSpinBox:up-button{\n"
"image:url(:/icon/Images/arrow_upwards.png);\n"
"border-left:0.5px solid #fff;\n"
"subcontrol-position:right;\n"
"width: 20px;\n"
"height: 20px;\n"
"}\n"
"QSpinBox:down-button{\n"
"image:url(:/icon/Images/arrow_downwards.png);\n"
"border-right:0.5px solid #fff;\n"
"subcontrol-position:left;\n"
"width:20px;\n"
"height:20px\n"
"}\n"
"QSpinBox:up-button:hover{\n"
"background-color: #5c636f;\n"
"}\n"
"QSpinBox:down-button:hover{\n"
"background-color: #5c636f;\n"
"}\n"
"QPushButton{\n"
"border: 2px solid #404040;\n"
"border-radius: 8px;\n"
""
                        "padding: 1px 5px;\n"
"color: #fff;\n"
"background-color: #6c757d;\n"
"font: 700 9pt \"Calibri\";\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: #5c636a;\n"
"}\n"
"QPushButton:pressed {\n"
"    border: 4px solid #c0c4c8 \n"
"}\n"
"QLabel {\n"
"    color: #fff;\n"
" background-color: #6a858d; \n"
"    border:2px solid #404040;        \n"
"    border-radius: 4px;           \n"
"    padding: 2.5px 5px;            \n"
"font: 700 9pt \"Calibri\";\n"
"}\n"
"\n"
"QTableWidget{\n"
"background-color: #819299; \n"
"gridline-color: #fff;  \n"
"}\n"
"\n"
"QHeaderView{\n"
"background-color: #85939a;\n"
"color:white;\n"
"font: 700 9pt \"Calibri\";\n"
"}\n"
"\n"
"QHeaderView::section {\n"
"background-color: #85939a;\n"
"}\n"
"QTableCornerButton::section {\n"
"background-color: #85939a;\n"
"}\n"
"QTableWidget::item{\n"
"color:#fff\n"
"}\n"
"QTableWidget::item::hover{\n"
"background-color: #B6BEC2\n"
"}")
        self.verticalLayout = QVBoxLayout(main_widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.tab_widget = QTabWidget(main_widget)
        self.tab_widget.setObjectName(u"tab_widget")
        self.vector_x_vector_widget = QWidget()
        self.vector_x_vector_widget.setObjectName(u"vector_x_vector_widget")
        self.verticalLayout_2 = QVBoxLayout(self.vector_x_vector_widget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.vxv_options_widget = QWidget(self.vector_x_vector_widget)
        self.vxv_options_widget.setObjectName(u"vxv_options_widget")
        self.horizontalLayout = QHBoxLayout(self.vxv_options_widget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, -1, -1, -1)
        self.vxv_matrix_vector_widget = QWidget(self.vxv_options_widget)
        self.vxv_matrix_vector_widget.setObjectName(u"vxv_matrix_vector_widget")
        self.verticalLayout_3 = QVBoxLayout(self.vxv_matrix_vector_widget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.vxv_spinbox_widget = QWidget(self.vxv_matrix_vector_widget)
        self.vxv_spinbox_widget.setObjectName(u"vxv_spinbox_widget")
        self.verticalLayout_4 = QVBoxLayout(self.vxv_spinbox_widget)
        self.verticalLayout_4.setSpacing(6)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(9, 9, 9, 9)
        self.vxv_row_label = QLabel(self.vxv_spinbox_widget)
        self.vxv_row_label.setObjectName(u"vxv_row_label")

        self.verticalLayout_4.addWidget(self.vxv_row_label, 0, Qt.AlignmentFlag.AlignHCenter)

        self.vxv_row_spinbox = QSpinBox(self.vxv_spinbox_widget)
        self.vxv_row_spinbox.setObjectName(u"vxv_row_spinbox")
        self.vxv_row_spinbox.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_4.addWidget(self.vxv_row_spinbox)


        self.verticalLayout_3.addWidget(self.vxv_spinbox_widget)

        self.vxv_row_vector_widget = QWidget(self.vxv_matrix_vector_widget)
        self.vxv_row_vector_widget.setObjectName(u"vxv_row_vector_widget")
        self.vxv_row_vector_widget.setStyleSheet(u"QTabBar:tab{\n"
"max-width:10px;\n"
"}")
        self.verticalLayout_5 = QVBoxLayout(self.vxv_row_vector_widget)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.vxv_row_vector = QTableWidget(self.vxv_row_vector_widget)
        if (self.vxv_row_vector.columnCount() < 4):
            self.vxv_row_vector.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        self.vxv_row_vector.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.vxv_row_vector.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.vxv_row_vector.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.vxv_row_vector.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        if (self.vxv_row_vector.rowCount() < 1):
            self.vxv_row_vector.setRowCount(1)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.vxv_row_vector.setItem(0, 0, __qtablewidgetitem4)
        self.vxv_row_vector.setObjectName(u"vxv_row_vector")
        self.vxv_row_vector.setMaximumSize(QSize(16777215, 16777215))
        self.vxv_row_vector.setStyleSheet(u"QTableWidget:item{\n"
"max-width:10px;\n"
"}")
        self.vxv_row_vector.setGridStyle(Qt.PenStyle.SolidLine)
        self.vxv_row_vector.horizontalHeader().setVisible(True)
        self.vxv_row_vector.horizontalHeader().setMinimumSectionSize(10)
        self.vxv_row_vector.horizontalHeader().setDefaultSectionSize(50)
        self.vxv_row_vector.horizontalHeader().setHighlightSections(False)
        self.vxv_row_vector.verticalHeader().setVisible(True)
        self.vxv_row_vector.verticalHeader().setDefaultSectionSize(22)
        self.vxv_row_vector.verticalHeader().setProperty("showSortIndicator", False)

        self.verticalLayout_5.addWidget(self.vxv_row_vector, 0, Qt.AlignmentFlag.AlignTop)


        self.verticalLayout_3.addWidget(self.vxv_row_vector_widget)


        self.horizontalLayout.addWidget(self.vxv_matrix_vector_widget)

        self.vxv_column_vector_widget = QWidget(self.vxv_options_widget)
        self.vxv_column_vector_widget.setObjectName(u"vxv_column_vector_widget")
        self.verticalLayout_6 = QVBoxLayout(self.vxv_column_vector_widget)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.vxv_column_vector = QTableWidget(self.vxv_column_vector_widget)
        if (self.vxv_column_vector.columnCount() < 1):
            self.vxv_column_vector.setColumnCount(1)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.vxv_column_vector.setHorizontalHeaderItem(0, __qtablewidgetitem5)
        if (self.vxv_column_vector.rowCount() < 4):
            self.vxv_column_vector.setRowCount(4)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.vxv_column_vector.setVerticalHeaderItem(0, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.vxv_column_vector.setVerticalHeaderItem(1, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.vxv_column_vector.setVerticalHeaderItem(2, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.vxv_column_vector.setVerticalHeaderItem(3, __qtablewidgetitem9)
        self.vxv_column_vector.setObjectName(u"vxv_column_vector")
        self.vxv_column_vector.setMaximumSize(QSize(50, 16777215))
        self.vxv_column_vector.horizontalHeader().setVisible(True)
        self.vxv_column_vector.horizontalHeader().setMinimumSectionSize(10)
        self.vxv_column_vector.horizontalHeader().setDefaultSectionSize(35)
        self.vxv_column_vector.horizontalHeader().setHighlightSections(True)
        self.vxv_column_vector.verticalHeader().setVisible(False)
        self.vxv_column_vector.verticalHeader().setCascadingSectionResizes(False)
        self.vxv_column_vector.verticalHeader().setMinimumSectionSize(35)
        self.vxv_column_vector.verticalHeader().setDefaultSectionSize(35)
        self.vxv_column_vector.verticalHeader().setProperty("showSortIndicator", False)

        self.verticalLayout_6.addWidget(self.vxv_column_vector)


        self.horizontalLayout.addWidget(self.vxv_column_vector_widget)


        self.verticalLayout_2.addWidget(self.vxv_options_widget)

        self.vxv_solution_widget = QWidget(self.vector_x_vector_widget)
        self.vxv_solution_widget.setObjectName(u"vxv_solution_widget")
        self.horizontalLayout_2 = QHBoxLayout(self.vxv_solution_widget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(-1, 0, -1, -1)
        self.vxv_solution_options = QWidget(self.vxv_solution_widget)
        self.vxv_solution_options.setObjectName(u"vxv_solution_options")
        self.horizontalLayout_3 = QHBoxLayout(self.vxv_solution_options)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(-1, 0, -1, -1)
        self.vxv_solve_scalar_button = QPushButton(self.vxv_solution_options)
        self.vxv_solve_scalar_button.setObjectName(u"vxv_solve_scalar_button")

        self.horizontalLayout_3.addWidget(self.vxv_solve_scalar_button, 0, Qt.AlignmentFlag.AlignLeft)

        self.scalar_label = QLabel(self.vxv_solution_options)
        self.scalar_label.setObjectName(u"scalar_label")
        self.scalar_label.setMaximumSize(QSize(16777215, 24))
        self.scalar_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_3.addWidget(self.scalar_label, 0, Qt.AlignmentFlag.AlignLeft)


        self.horizontalLayout_2.addWidget(self.vxv_solution_options)

        self.vxv_horizontal_spacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.vxv_horizontal_spacer)

        self.horizontalLayout_2.setStretch(0, 5)
        self.horizontalLayout_2.setStretch(1, 100)

        self.verticalLayout_2.addWidget(self.vxv_solution_widget)

        self.verticalLayout_2.setStretch(0, 5)
        self.verticalLayout_2.setStretch(1, 1)
        self.verticalLayout_3.setStretch(0, 10)
        self.verticalLayout_3.setStretch(1, 100)
        self.tab_widget.addTab(self.vector_x_vector_widget, "")
        self.matrix_x_matrix_widget = QWidget()
        self.matrix_x_matrix_widget.setObjectName(u"matrix_x_matrix_widget")
        self.tab_widget.addTab(self.matrix_x_matrix_widget, "")
        self.vector_x_matrix_widget = QWidget()
        self.vector_x_matrix_widget.setObjectName(u"vector_x_matrix_widget")
        self.tab_widget.addTab(self.vector_x_matrix_widget, "")
        
        self.verticalLayout.addWidget(self.tab_widget)
        self.resize_vector_column()
        self.resize_vector_row()
        self.set_vector_row(self.matrix_instance[0])
        self.retranslateUi(main_widget)

        self.tab_widget.setCurrentIndex(0)
        self.vxv_row_spinbox.setValue(1)


        QMetaObject.connectSlotsByName(main_widget)
    # setupUi
    def set_vector_row(self,vector:list[int|float]):
        for i in range(self.vxv_row_vector.columnCount()):
            table_item = self.vxv_row_vector.item(0,i)
            if table_item is None:
                table_item = QTableWidgetItem()
                table_item.setFlags(table_item.flags() & ~Qt.ItemIsEditable & ~Qt.ItemIsSelectable)
                self.vxv_row_vector.setItem(0,i,table_item)
            table_item.setText(str(vector[i]))
    
    def resize_vector_row(self):
        width = len(self.matrix_instance)
        self.vxv_row_vector.setRowCount(1)
        self.vxv_row_vector.setColumnCount(width)
        for i in range(width):
            table_header = self.vxv_row_vector.horizontalHeaderItem(i)
            if table_header is None:
                table_header = QTableWidgetItem()
                self.vxv_column_vector.setHorizontalHeaderItem(i,table_header)
            table_header.setText(f'X{i+1}')
    
    def resize_vector_column(self):
        length = len(self.matrix_instance)
        self.vxv_column_vector.setRowCount(length)
        self.vxv_column_vector.setColumnCount(1)
        table_header = self.vxv_column_vector.horizontalHeaderItem(0)
        if table_header is None:
            table_header = QTableWidgetItem()
            self.vxv_column_vector.setHorizontalHeaderItem(0,table_header)
        table_header.setText('b')

    def retranslateUi(self, main_widget):
        main_widget.setWindowTitle(QCoreApplication.translate("main_widget", u"Vectores", None))
        self.vxv_row_label.setText(QCoreApplication.translate("main_widget", u"Vector fila de la matriz", None))

        __sortingEnabled = self.vxv_row_vector.isSortingEnabled()
        self.vxv_row_vector.setSortingEnabled(False)
        self.vxv_row_vector.setSortingEnabled(__sortingEnabled)
        self.vxv_solve_scalar_button.setText(QCoreApplication.translate("main_widget", u"Obtener escalar", None))
        self.scalar_label.setText(QCoreApplication.translate("main_widget", u"Valor", None))
        self.tab_widget.setTabText(self.tab_widget.indexOf(self.vector_x_vector_widget), QCoreApplication.translate("main_widget", u"Vector por vector", None))
        self.tab_widget.setTabText(self.tab_widget.indexOf(self.matrix_x_matrix_widget), QCoreApplication.translate("main_widget", u"Matriz por matriz", None))
#if QT_CONFIG(accessibility)
        self.vector_x_matrix_widget.setAccessibleName(QCoreApplication.translate("main_widget", u"asd", None))
#endif // QT_CONFIG(accessibility)
        self.tab_widget.setTabText(self.tab_widget.indexOf(self.vector_x_matrix_widget), QCoreApplication.translate("main_widget", u"Vector por matriz", None))
    # retranslateUi

