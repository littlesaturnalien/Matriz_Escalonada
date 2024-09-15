# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'solution_window.ui'
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
    QPushButton, QSizePolicy, QTabWidget, QTableWidget,
    QTableWidgetItem, QVBoxLayout, QWidget)

class Ui_main_widget(object):
    def setupUi(self, main_widget):
        if not main_widget.objectName():
            main_widget.setObjectName(u"main_widget")
        main_widget.resize(400, 300)
        self.main_widget_vertical_layout = QVBoxLayout(main_widget)
        self.main_widget_vertical_layout.setObjectName(u"main_widget_vertical_layout")
        self.options_tab_widget = QWidget(main_widget)
        self.options_tab_widget.setObjectName(u"options_tab_widget")
        self.options_tab_horizontal_layout = QHBoxLayout(self.options_tab_widget)
        self.options_tab_horizontal_layout.setObjectName(u"options_tab_horizontal_layout")
        self.back_tab_button = QPushButton(self.options_tab_widget)
        self.back_tab_button.setObjectName(u"back_tab_button")

        self.options_tab_horizontal_layout.addWidget(self.back_tab_button, 0, Qt.AlignmentFlag.AlignLeft)

        self.label = QLabel(self.options_tab_widget)
        self.label.setObjectName(u"label")

        self.options_tab_horizontal_layout.addWidget(self.label, 0, Qt.AlignmentFlag.AlignHCenter)

        self.next_tab_button = QPushButton(self.options_tab_widget)
        self.next_tab_button.setObjectName(u"next_tab_button")

        self.options_tab_horizontal_layout.addWidget(self.next_tab_button, 0, Qt.AlignmentFlag.AlignRight)


        self.main_widget_vertical_layout.addWidget(self.options_tab_widget)

        self.tabWidget = QTabWidget(main_widget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.p1 = QWidget()
        self.p1.setObjectName(u"p1")
        self.p_horizontal_layout_1 = QHBoxLayout(self.p1)
        self.p_horizontal_layout_1.setObjectName(u"p_horizontal_layout_1")
        self.p_horizontal_layout_1.setContentsMargins(0, 0, 0, 0)
        self.tableWidget = QTableWidget(self.p1)
        if (self.tableWidget.columnCount() < 3):
            self.tableWidget.setColumnCount(3)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        if (self.tableWidget.rowCount() < 3):
            self.tableWidget.setRowCount(3)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, __qtablewidgetitem5)
        self.tableWidget.setObjectName(u"tableWidget")

        self.p_horizontal_layout_1.addWidget(self.tableWidget)

        self.tabWidget.addTab(self.p1, "")

        self.main_widget_vertical_layout.addWidget(self.tabWidget)

        self.main_widget_vertical_layout.setStretch(0, 1)
        self.main_widget_vertical_layout.setStretch(1, 10)

        self.retranslateUi(main_widget)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(main_widget)
    # setupUi

    def retranslateUi(self, main_widget):
        main_widget.setWindowTitle(QCoreApplication.translate("main_widget", u"Form", None))
        self.back_tab_button.setText(QCoreApplication.translate("main_widget", u"Anterior", None))
        self.label.setText(QCoreApplication.translate("main_widget", u"Procedimiento", None))
        self.next_tab_button.setText(QCoreApplication.translate("main_widget", u"Siguiente", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("main_widget", u"Nueva columna", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("main_widget", u"Nueva columna", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("main_widget", u"Nueva columna", None));
        ___qtablewidgetitem3 = self.tableWidget.verticalHeaderItem(0)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("main_widget", u"Nueva fila", None));
        ___qtablewidgetitem4 = self.tableWidget.verticalHeaderItem(1)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("main_widget", u"Nueva fila", None));
        ___qtablewidgetitem5 = self.tableWidget.verticalHeaderItem(2)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("main_widget", u"Nueva fila", None));
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.p1), QCoreApplication.translate("main_widget", u"p1", None))
    # retranslateUi

