from operator import truediv
from PySide2.QtWidgets import QMainWindow, QFileDialog, QMessageBox, QTableWidgetItem, QGraphicsScene
from PySide2.QtGui import QPen, QColor, QTransform
from PySide2.QtCore import Slot
from ui_mainwindow import Ui_MainWindow
from particulas.listaparticula import ListaParticulas
from particulas.particula import Particula
from particulas.particula import Punto
from particulas.algoritmos import distancia_euclidiana

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        
        self.myListaParticulas = ListaParticulas()
        self.puntos = []
        self.puntos_cercanos = []
        
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.agregar_inicio_pushButton.clicked.connect(self.click_agregar_inicio)
        self.ui.agregar_final_pushButton.clicked.connect(self.click_agregar_final)
        self.ui.mostrar_pushButton.clicked.connect(self.click_mostrar)
        self.ui.mostrar_pushButton.clicked.connect(self.mostrar_tabla)


        self.ui.actionAbrir.triggered.connect(self.action_abrir_archivo)
        self.ui.actionGuardar.triggered.connect(self.action_guardar_archivo)

        self.ui.buscar_pushButton.clicked.connect(self.buscar_particula)

        self.ui.dibujar_pushButton.clicked.connect(self.dibujar_grafos)
        self.ui.limpiar_pushButton.clicked.connect(self.limpiar)

        self.ui.actionPuntos.triggered.connect(self.dibujar_puntos)
        self.ui.actionGrafos.triggered.connect(self.dibujar_grafos)
        self.ui.actionPuntos_mas_cercanos.triggered.connect(self.calcular_puntos_mas_cercanos)
        
        self.scene = QGraphicsScene()
        self.ui.graphicsView.setScene(self.scene)

        self.ui.ordenar_por_id_pushButton.clicked.connect(self.sort_by_id)
        self.ui.ordenar_por_distancia_pushButton.clicked.connect(self.sort_by_distancia)
        self.ui.ordenar_por_velocidad_pushButton.clicked.connect(self.sort_by_velocidad)
    

    @Slot()
    def buscar_particula(self):
        id = self.ui.buscar_lineEdit.text()
        
        encontrado = False
        for particula in self.myListaParticulas:

            if int(id) == particula.id:
                self.ui.tabla_tableWidget.clear()
                self.ui.tabla_tableWidget.setColumnCount(10)
                headers =["Id", "Origen X", "Origen Y ", "Destino X", "Destino Y", "Velocidad", "Red", "Green", "Blue", "Distancia"]
                self.ui.tabla_tableWidget.setHorizontalHeaderLabels(headers)
                self.ui.tabla_tableWidget.setRowCount(1)
                
                id_widget = QTableWidgetItem(str(particula.id))
                origen_x_widget = QTableWidgetItem(str(particula.origen_x))
                origen_y_widget = QTableWidgetItem(str(particula.origen_y))
                destino_x_widget = QTableWidgetItem(str(particula.destino_x))
                destino_y_widget = QTableWidgetItem(str(particula.destino_y))
                velocidad_widget = QTableWidgetItem(str(particula.velocidad))
                green_widget = QTableWidgetItem(str(particula.green))
                red_widget = QTableWidgetItem(str(particula.red))
                blue_widget = QTableWidgetItem(str(particula.blue))
                distancia_widget = QTableWidgetItem(str(particula.distancia))

                self.ui.tabla_tableWidget.setItem(0, 0, id_widget)
                self.ui.tabla_tableWidget.setItem(0, 1, origen_x_widget)
                self.ui.tabla_tableWidget.setItem(0, 2, origen_y_widget)
                self.ui.tabla_tableWidget.setItem(0, 3, destino_x_widget)
                self.ui.tabla_tableWidget.setItem(0, 4, destino_y_widget)
                self.ui.tabla_tableWidget.setItem(0, 5, velocidad_widget)
                self.ui.tabla_tableWidget.setItem(0, 6, green_widget)
                self.ui.tabla_tableWidget.setItem(0, 7, red_widget)
                self.ui.tabla_tableWidget.setItem(0, 8, blue_widget)
                self.ui.tabla_tableWidget.setItem(0, 9, distancia_widget)

                encontrado = True
                return
        if not encontrado:
            QMessageBox.warning(
                self,
                "Atención",
                f'La particula con la id: "{id}" no fue encontrada'
            )

    @Slot()
    def mostrar_tabla(self):
        self.ui.tabla_tableWidget.setColumnCount(10)
        headers =["Id", "Origen X", "Origen Y ", "Destino X", "Destino Y", "Velocidad", "Red", "Green", "Blue", "Distancia"]
        self.ui.tabla_tableWidget.setHorizontalHeaderLabels(headers)

        self.ui.tabla_tableWidget.setRowCount(len(self.myListaParticulas))

        row = 0
        for particula in self.myListaParticulas:
            id_widget = QTableWidgetItem(str(particula.id))
            origen_x_widget = QTableWidgetItem(str(particula.origen_x))
            origen_y_widget = QTableWidgetItem(str(particula.origen_y))
            destino_x_widget = QTableWidgetItem(str(particula.destino_x))
            destino_y_widget = QTableWidgetItem(str(particula.destino_y))
            velocidad_widget = QTableWidgetItem(str(particula.velocidad))
            red_widget = QTableWidgetItem(str(particula.red))
            green_widget = QTableWidgetItem(str(particula.green))
            blue_widget = QTableWidgetItem(str(particula.blue))
            distancia_widget = QTableWidgetItem(str(particula.distancia))

            self.ui.tabla_tableWidget.setItem(row, 0, id_widget)
            self.ui.tabla_tableWidget.setItem(row, 1, origen_x_widget)
            self.ui.tabla_tableWidget.setItem(row, 2, origen_y_widget)
            self.ui.tabla_tableWidget.setItem(row, 3, destino_x_widget)
            self.ui.tabla_tableWidget.setItem(row, 4, destino_y_widget)
            self.ui.tabla_tableWidget.setItem(row, 5, velocidad_widget)
            self.ui.tabla_tableWidget.setItem(row, 7, green_widget)
            self.ui.tabla_tableWidget.setItem(row, 6, red_widget)
            self.ui.tabla_tableWidget.setItem(row, 8, blue_widget)
            self.ui.tabla_tableWidget.setItem(row, 9, distancia_widget)
            
            row += 1

    @Slot()
    def action_abrir_archivo(self):
        ubicacion = QFileDialog.getOpenFileName(
            self,
            'Abrir Archivo',
            '.',
            'JSON (*.json)'
        )[0]
        if self.myListaParticulas.abrir(ubicacion):
            QMessageBox.information(
                self,
                "Exito",
                "Se ha abierto el archivo " + ubicacion
            )
        else:
            QMessageBox.critical(
                self,
                "Error",
                "No se ha abierto el archivo " + ubicacion
            )

    @Slot()
    def action_guardar_archivo(self):
        #print('Guardar archivo')
        ubicacion = QFileDialog.getSaveFileName(
            self,
            'Guardar Archivo',
            '.',
            'JSON (*.json)'
        )[0]
        print(ubicacion)
        if self.myListaParticulas.guardar(ubicacion):
            QMessageBox.information(
                self,
                "Exito",
                "Se ha guardado el archivo " + ubicacion
            )
        else:
            QMessageBox.critical(
                self,
                "Error",
                "No se ha creado el archivo " + ubicacion
            )

    @Slot()
    def click_mostrar(self):
        self.ui.out_plainTextEdit.clear()
        self.ui.out_plainTextEdit.insertPlainText(str(self.myListaParticulas))

    @Slot()
    def click_agregar_inicio(self):
        myId = self.ui.id_lineEdit.text()
        myOrigenX = self.ui.origenX_spinBox.value()
        myOrigenY = self.ui.origenY_spinBox.value()
        myDestinoX = self.ui.destinoX_spinBox.value()
        myDestinoY = self.ui.destinoY_spinBox.value()
        myVelocidad = self.ui.velocidad_spinBox.value()
        myRed = self.ui.red_spinBox.value()
        myGreen = self.ui.green_spinBox.value()
        myBlue = self.ui.blue__spinBox.value()

        myParticula = Particula(myId, myOrigenX, myOrigenY, myDestinoX,myDestinoY,myVelocidad,myRed,myGreen,myBlue)
        self.myListaParticulas.agregar_inicio(myParticula)

    @Slot()
    def click_agregar_final(self):
        myId = self.ui.id_lineEdit.text()
        myOrigenX = self.ui.origenX_spinBox.value()
        myOrigenY = self.ui.origenY_spinBox.value()
        myDestinoX = self.ui.destinoX_spinBox.value()
        myDestinoY = self.ui.destinoY_spinBox.value()
        myVelocidad = self.ui.velocidad_spinBox.value()
        myRed = self.ui.red_spinBox.value()
        myGreen = self.ui.green_spinBox.value()
        myBlue = self.ui.blue__spinBox.value()

        myParticula = Particula(myId, myOrigenX, myOrigenY, myDestinoX,myDestinoY,myVelocidad,myRed,myGreen,myBlue)
        self.myListaParticulas.agregar_final(myParticula)

#DIBUJAR
    @Slot()
    def dibujar_grafos(self):
        self.scene.clear()
        pen = QPen()
        pen.setWidth(2)
        
        for particula in self.myListaParticulas:
            r = particula.red
            g = particula.green
            b = particula.blue
            
            color = QColor(r,g,b)
            pen.setColor(color)
            
            origen_x = particula.origen_x
            origen_y = particula.origen_y
            destino_x = particula.destino_x
            destino_y = particula.destino_y

            self.scene.addEllipse(origen_x,origen_y,3,3, pen)
            self.scene.addEllipse(destino_x,destino_y,3,3,pen)
            self.scene.addLine(origen_x+3,origen_y+3,destino_x,destino_y,pen)

    @Slot()
    def limpiar(self):
        self.scene.clear()
        self.myListaParticulas = ListaParticulas()
        self.puntos = []
        self.puntos_cercanos = []

    @Slot()
    def sort_by_id(self):
        self.myListaParticulas.sort_by_id()
    
    @Slot()
    def sort_by_distancia(self):
        self.myListaParticulas.sort_by_distancia()

    @Slot()
    def sort_by_velocidad(self):
        self.myListaParticulas.sort_by_velocidad()

    
    @Slot()
    def dibujar_puntos(self):
        self.scene.clear()
        self.puntos = self.myListaParticulas.get_puntos()
        for punto in self.puntos:
            x = punto.x
            y = punto.y
            red = punto.red
            green = punto.green
            blue = punto.blue
            color = QColor(red, green, blue)
            pen = QPen()
            pen.setColor(color)

            self.scene.addRect(x, y, 10, 10, pen)
    
    @Slot()
    def dibujar_puntos_mas_cercanos(self):
        for punto01, punto02 in self.puntos_cercanos:
            pen = QPen()
            color = QColor(punto01.red, punto01.green, punto01.blue)
            pen.setColor(color)
            self.scene.addLine(punto01.x+5, punto01.y+5, punto02.x+5, punto02.y+5, pen)



    @Slot()
    def calcular_puntos_mas_cercanos(self):
        for punto01 in self.puntos:
            distMin = 1000
            punto = Punto
            for todos in self.puntos:
                if punto01 == todos:
                        continue
                dist = distancia_euclidiana(punto01.x, punto01.y, todos.x, todos.y)
                if dist < distMin:
                    distMin = dist
                    punto = todos
            self.puntos_cercanos.append([punto01, punto])
        self.dibujar_puntos_mas_cercanos()
    