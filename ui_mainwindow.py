# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1046, 868)
        self.actionAbrir = QAction(MainWindow)
        self.actionAbrir.setObjectName(u"actionAbrir")
        self.actionGuardar = QAction(MainWindow)
        self.actionGuardar.setObjectName(u"actionGuardar")
        self.actionPuntos = QAction(MainWindow)
        self.actionPuntos.setObjectName(u"actionPuntos")
        self.actionPuntos_mas_cercanos = QAction(MainWindow)
        self.actionPuntos_mas_cercanos.setObjectName(u"actionPuntos_mas_cercanos")
        self.actionGrafos = QAction(MainWindow)
        self.actionGrafos.setObjectName(u"actionGrafos")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setMaximumSize(QSize(300, 16777215))
        self.verticalLayout_2 = QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.widget_6 = QWidget(self.groupBox)
        self.widget_6.setObjectName(u"widget_6")
        self.horizontalLayout_5 = QHBoxLayout(self.widget_6)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_7 = QLabel(self.widget_6)
        self.label_7.setObjectName(u"label_7")

        self.horizontalLayout_5.addWidget(self.label_7)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_2)

        self.id_lineEdit = QLineEdit(self.widget_6)
        self.id_lineEdit.setObjectName(u"id_lineEdit")

        self.horizontalLayout_5.addWidget(self.id_lineEdit)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer)


        self.verticalLayout_2.addWidget(self.widget_6)

        self.groupBox_2 = QGroupBox(self.groupBox)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.horizontalLayout_3 = QHBoxLayout(self.groupBox_2)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_8 = QLabel(self.groupBox_2)
        self.label_8.setObjectName(u"label_8")

        self.horizontalLayout_3.addWidget(self.label_8)

        self.origenX_spinBox = QSpinBox(self.groupBox_2)
        self.origenX_spinBox.setObjectName(u"origenX_spinBox")
        self.origenX_spinBox.setMaximum(500)

        self.horizontalLayout_3.addWidget(self.origenX_spinBox)

        self.label_9 = QLabel(self.groupBox_2)
        self.label_9.setObjectName(u"label_9")

        self.horizontalLayout_3.addWidget(self.label_9)

        self.origenY_spinBox = QSpinBox(self.groupBox_2)
        self.origenY_spinBox.setObjectName(u"origenY_spinBox")
        self.origenY_spinBox.setMaximum(500)

        self.horizontalLayout_3.addWidget(self.origenY_spinBox)


        self.verticalLayout_2.addWidget(self.groupBox_2)

        self.groupBox_3 = QGroupBox(self.groupBox)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.horizontalLayout_4 = QHBoxLayout(self.groupBox_3)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label = QLabel(self.groupBox_3)
        self.label.setObjectName(u"label")

        self.horizontalLayout_4.addWidget(self.label)

        self.destinoX_spinBox = QSpinBox(self.groupBox_3)
        self.destinoX_spinBox.setObjectName(u"destinoX_spinBox")
        self.destinoX_spinBox.setMaximum(500)

        self.horizontalLayout_4.addWidget(self.destinoX_spinBox)

        self.label_2 = QLabel(self.groupBox_3)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_4.addWidget(self.label_2)

        self.destinoY_spinBox = QSpinBox(self.groupBox_3)
        self.destinoY_spinBox.setObjectName(u"destinoY_spinBox")
        self.destinoY_spinBox.setMaximum(500)

        self.horizontalLayout_4.addWidget(self.destinoY_spinBox)


        self.verticalLayout_2.addWidget(self.groupBox_3)

        self.widget_7 = QWidget(self.groupBox)
        self.widget_7.setObjectName(u"widget_7")
        self.horizontalLayout_6 = QHBoxLayout(self.widget_7)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_3 = QLabel(self.widget_7)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_6.addWidget(self.label_3)

        self.velocidad_spinBox = QSpinBox(self.widget_7)
        self.velocidad_spinBox.setObjectName(u"velocidad_spinBox")
        self.velocidad_spinBox.setMaximum(10000)
        self.velocidad_spinBox.setDisplayIntegerBase(10)

        self.horizontalLayout_6.addWidget(self.velocidad_spinBox)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_3)


        self.verticalLayout_2.addWidget(self.widget_7)

        self.widget = QWidget(self.groupBox)
        self.widget.setObjectName(u"widget")
        self.horizontalLayout = QHBoxLayout(self.widget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_4 = QLabel(self.widget)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout.addWidget(self.label_4)

        self.red_spinBox = QSpinBox(self.widget)
        self.red_spinBox.setObjectName(u"red_spinBox")
        self.red_spinBox.setMaximum(255)

        self.horizontalLayout.addWidget(self.red_spinBox)

        self.label_5 = QLabel(self.widget)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout.addWidget(self.label_5)

        self.green_spinBox = QSpinBox(self.widget)
        self.green_spinBox.setObjectName(u"green_spinBox")
        self.green_spinBox.setMaximum(255)

        self.horizontalLayout.addWidget(self.green_spinBox)

        self.label_6 = QLabel(self.widget)
        self.label_6.setObjectName(u"label_6")

        self.horizontalLayout.addWidget(self.label_6)

        self.blue__spinBox = QSpinBox(self.widget)
        self.blue__spinBox.setObjectName(u"blue__spinBox")
        self.blue__spinBox.setMaximum(255)

        self.horizontalLayout.addWidget(self.blue__spinBox)


        self.verticalLayout_2.addWidget(self.widget)

        self.widget_3 = QWidget(self.groupBox)
        self.widget_3.setObjectName(u"widget_3")
        self.horizontalLayout_2 = QHBoxLayout(self.widget_3)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.agregar_inicio_pushButton = QPushButton(self.widget_3)
        self.agregar_inicio_pushButton.setObjectName(u"agregar_inicio_pushButton")

        self.horizontalLayout_2.addWidget(self.agregar_inicio_pushButton)

        self.agregar_final_pushButton = QPushButton(self.widget_3)
        self.agregar_final_pushButton.setObjectName(u"agregar_final_pushButton")

        self.horizontalLayout_2.addWidget(self.agregar_final_pushButton)


        self.verticalLayout_2.addWidget(self.widget_3)

        self.out_plainTextEdit = QPlainTextEdit(self.groupBox)
        self.out_plainTextEdit.setObjectName(u"out_plainTextEdit")
        self.out_plainTextEdit.setMinimumSize(QSize(100, 100))

        self.verticalLayout_2.addWidget(self.out_plainTextEdit)

        self.widget_2 = QWidget(self.groupBox)
        self.widget_2.setObjectName(u"widget_2")
        self.verticalLayout = QVBoxLayout(self.widget_2)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.mostrar_pushButton = QPushButton(self.widget_2)
        self.mostrar_pushButton.setObjectName(u"mostrar_pushButton")

        self.verticalLayout.addWidget(self.mostrar_pushButton)

        self.ordenar_por_velocidad_pushButton = QPushButton(self.widget_2)
        self.ordenar_por_velocidad_pushButton.setObjectName(u"ordenar_por_velocidad_pushButton")

        self.verticalLayout.addWidget(self.ordenar_por_velocidad_pushButton)

        self.ordenar_por_distancia_pushButton = QPushButton(self.widget_2)
        self.ordenar_por_distancia_pushButton.setObjectName(u"ordenar_por_distancia_pushButton")

        self.verticalLayout.addWidget(self.ordenar_por_distancia_pushButton)

        self.ordenar_por_id_pushButton = QPushButton(self.widget_2)
        self.ordenar_por_id_pushButton.setObjectName(u"ordenar_por_id_pushButton")

        self.verticalLayout.addWidget(self.ordenar_por_id_pushButton)


        self.verticalLayout_2.addWidget(self.widget_2)


        self.gridLayout.addWidget(self.groupBox, 0, 0, 1, 1)

        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabla_tab = QWidget()
        self.tabla_tab.setObjectName(u"tabla_tab")
        self.gridLayout_3 = QGridLayout(self.tabla_tab)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.tabla_tableWidget = QTableWidget(self.tabla_tab)
        self.tabla_tableWidget.setObjectName(u"tabla_tableWidget")

        self.gridLayout_3.addWidget(self.tabla_tableWidget, 0, 0, 1, 3)

        self.buscar_pushButton = QPushButton(self.tabla_tab)
        self.buscar_pushButton.setObjectName(u"buscar_pushButton")

        self.gridLayout_3.addWidget(self.buscar_pushButton, 1, 1, 1, 2)

        self.buscar_lineEdit = QLineEdit(self.tabla_tab)
        self.buscar_lineEdit.setObjectName(u"buscar_lineEdit")

        self.gridLayout_3.addWidget(self.buscar_lineEdit, 1, 0, 1, 1)

        self.tabWidget.addTab(self.tabla_tab, "")
        self.tab_5 = QWidget()
        self.tab_5.setObjectName(u"tab_5")
        self.gridLayout_4 = QGridLayout(self.tab_5)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.graphicsView = QGraphicsView(self.tab_5)
        self.graphicsView.setObjectName(u"graphicsView")

        self.gridLayout_4.addWidget(self.graphicsView, 0, 0, 1, 2)

        self.limpiar_pushButton = QPushButton(self.tab_5)
        self.limpiar_pushButton.setObjectName(u"limpiar_pushButton")

        self.gridLayout_4.addWidget(self.limpiar_pushButton, 2, 1, 1, 1)

        self.dibujar_pushButton = QPushButton(self.tab_5)
        self.dibujar_pushButton.setObjectName(u"dibujar_pushButton")

        self.gridLayout_4.addWidget(self.dibujar_pushButton, 2, 0, 1, 1)

        self.tabWidget.addTab(self.tab_5, "")

        self.gridLayout.addWidget(self.tabWidget, 0, 1, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1046, 26))
        self.menuArchivo = QMenu(self.menubar)
        self.menuArchivo.setObjectName(u"menuArchivo")
        self.menuAlgotirmos = QMenu(self.menubar)
        self.menuAlgotirmos.setObjectName(u"menuAlgotirmos")
        self.menuAlgoritmos = QMenu(self.menubar)
        self.menuAlgoritmos.setObjectName(u"menuAlgoritmos")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuArchivo.menuAction())
        self.menubar.addAction(self.menuAlgotirmos.menuAction())
        self.menubar.addAction(self.menuAlgoritmos.menuAction())
        self.menuArchivo.addAction(self.actionAbrir)
        self.menuArchivo.addAction(self.actionGuardar)
        self.menuAlgotirmos.addAction(self.actionPuntos)
        self.menuAlgotirmos.addAction(self.actionGrafos)
        self.menuAlgoritmos.addAction(self.actionPuntos_mas_cercanos)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionAbrir.setText(QCoreApplication.translate("MainWindow", u"Abrir", None))
#if QT_CONFIG(shortcut)
        self.actionAbrir.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+O", None))
#endif // QT_CONFIG(shortcut)
        self.actionGuardar.setText(QCoreApplication.translate("MainWindow", u"Guardar", None))
#if QT_CONFIG(shortcut)
        self.actionGuardar.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+S", None))
#endif // QT_CONFIG(shortcut)
        self.actionPuntos.setText(QCoreApplication.translate("MainWindow", u"Puntos", None))
#if QT_CONFIG(shortcut)
        self.actionPuntos.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+P", None))
#endif // QT_CONFIG(shortcut)
        self.actionPuntos_mas_cercanos.setText(QCoreApplication.translate("MainWindow", u"Puntos m\u00e1s cercanos", None))
        self.actionGrafos.setText(QCoreApplication.translate("MainWindow", u"Grafos", None))
#if QT_CONFIG(shortcut)
        self.actionGrafos.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+G", None))
#endif // QT_CONFIG(shortcut)
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Particula", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Id Particula", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"Origen", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"x:", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"y:", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"Destino", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"x:", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"y:", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Velocidad", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"R:", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"G:", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"B:", None))
        self.agregar_inicio_pushButton.setText(QCoreApplication.translate("MainWindow", u"Agregar Inicio", None))
        self.agregar_final_pushButton.setText(QCoreApplication.translate("MainWindow", u"Agregar Final", None))
        self.mostrar_pushButton.setText(QCoreApplication.translate("MainWindow", u"Mostrar", None))
        self.ordenar_por_velocidad_pushButton.setText(QCoreApplication.translate("MainWindow", u"Ordenar por velocidad", None))
        self.ordenar_por_distancia_pushButton.setText(QCoreApplication.translate("MainWindow", u"Ordenar por distancia", None))
        self.ordenar_por_id_pushButton.setText(QCoreApplication.translate("MainWindow", u"Ordenar por id", None))
        self.buscar_pushButton.setText(QCoreApplication.translate("MainWindow", u"Buscar", None))
        self.buscar_lineEdit.setText("")
        self.buscar_lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Id de la part\u00edcula", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabla_tab), QCoreApplication.translate("MainWindow", u"Tabla", None))
        self.limpiar_pushButton.setText(QCoreApplication.translate("MainWindow", u"Limpiar", None))
        self.dibujar_pushButton.setText(QCoreApplication.translate("MainWindow", u"Dibujar", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), QCoreApplication.translate("MainWindow", u"Dibujar", None))
        self.menuArchivo.setTitle(QCoreApplication.translate("MainWindow", u"Archivo", None))
        self.menuAlgotirmos.setTitle(QCoreApplication.translate("MainWindow", u"Visualizar", None))
        self.menuAlgoritmos.setTitle(QCoreApplication.translate("MainWindow", u"Algoritmos", None))
    # retranslateUi

