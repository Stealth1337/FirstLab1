import random
import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic, QtGui
from PyQt5.QtGui import QPainter, QColor, QFont
from PyQt5.QtCore import QTimer, QDateTime, Qt


class MyWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        uic.loadUi('design.ui', self)
        self.pushButton.clicked.connect(self.changeBackground)
        self.flagbackground = 0
        self.pushButton_2.clicked.connect(self.addListValue)
        self.valuesList = []
        self.label1.hide()
        self.checkBox.clicked.connect(self.showLabelOne)
        self.slide1.setMaximum(200)
        self.slide1.valueChanged.connect(self.setValueLCD)
        self.pushButton_4.setEnabled(False)
        self.timer = QTimer()
        self.timer.timeout.connect(self.showTime)
        self.pushButton_3.clicked.connect(self.startTimer)
        self.pushButton_4.clicked.connect(self.stopTimer)
        ##
        self.standmodel = QtGui.QStandardItemModel()
        self.rootitem1 = QtGui.QStandardItem('Заголовок 1')
        self.descitem1 = QtGui.QStandardItem('Описание заголовка')
        self.item1 = QtGui.QStandardItem('Подзаголовок заголовка 1 (1)')
        self.item2 = QtGui.QStandardItem('Подзаголовок заголовка 1 (2)')
        self.rootitem1.appendRow([self.item1, self.item2])
        self.item1 = QtGui.QStandardItem('Подзаголовок заголовка 1 (1)')
        self.item2 = QtGui.QStandardItem('Подзаголовок заголовка 1 (2)')
        self.rootitem1.appendRow([self.item1, self.item2])
        self.standmodel.appendRow([self.rootitem1, self.descitem1])
        self.rootitem2 = QtGui.QStandardItem('Заголовок 2')
        self.descitem2 = QtGui.QStandardItem('Описание заголовка')
        self.item3 = QtGui.QStandardItem('123')
        self.item4 = QtGui.QStandardItem('123')
        self.rootitem2.appendRow([self.item3, self.item4])
        self.standmodel.appendRow([self.rootitem2, self.descitem2])
        self.standmodel.setHorizontalHeaderLabels(["Что-то здесь", "Что-то там"])
        self.tree.setModel(self.standmodel)
        self.tree.setColumnWidth(0, 80)
        ### плохая реализация tableview.
        self.tablemodel = QtGui.QStandardItemModel()
        lst1 = ['Perl', 'PHP', 'Python', 'Ruby']
        lst2 = ['www.perl.com', 'www.php.com', 'www.python.org', 'www.ruby.com']
        for i in range(4):
            table_item1 = QtGui.QStandardItem(lst1[i])
            table_item2 = QtGui.QStandardItem(lst2[i])
            self.tablemodel.appendRow([table_item1, table_item2])
        self.tablemodel.setHorizontalHeaderLabels(['Название', 'Сайт'])
        self.table.setModel(self.tablemodel)
        self.table.setColumnWidth(0, 70)
        self.table.setColumnWidth(0, 100)
        ##
        self.fillComboBox(['Java', 'Python', 'PHP'], self.comboBox)
        self.comboBox.activated[str].connect(self.selectedComboBox)


    def changeBackground(self):
        if self.flagbackground == 0:
            self.centralform.setStyleSheet("background-color: #999999;")
            self.flagbackground = 1
        else:
            self.centralform.setStyleSheet("background-color: #ffffff;")
            self.flagbackground = 0

    def addListValue(self):
        self.valuesList.append(self.textEdit.toPlainText())
        sti = QtGui.QStandardItemModel()
        for i in self.valuesList:
            item = QtGui.QStandardItem(i)
            sti.appendRow(item)
        self.listView.setModel(sti)
        self.textEdit.setText('')

    def showLabelOne(self):
        if self.checkBox.isChecked():
            self.label1.show()
        else:
            self.label1.hide()

    def setValueLCD(self):
        val = self.slide1.value()
        self.lcdNumber.display(val)

    def showTime(self):
        time = QDateTime.currentDateTime()
        normaltime = time.toString("yyyy-MM-dd hh:mm:ss")
        self.timelabel.setText(normaltime)

    def startTimer(self):
        self.timer.start(1000)
        self.pushButton_4.setEnabled(True)
        self.pushButton_3.setEnabled(False)

    def stopTimer(self):
        self.timer.stop()
        self.pushButton_4.setEnabled(False)
        self.pushButton_3.setEnabled(True)


    def closeEvent(self, e):
        result = QMessageBox.question(self, "Хотите закрыть?",
                                      "Действительно хотите закрыть окно?", QMessageBox.Yes | QMessageBox.No,
                                      QMessageBox.No)
        if result == QMessageBox.Yes:
            e.accept()
            QWidget.closeEvent(self, e)
        else:
            e.ignore()

    def paintEvent(self, event):
        qp = QPainter(self)
        qp.begin(self)
        self.drawPoints(qp)
        self.drawRectangles(qp)


    def drawPoints(self, qp):
        qp.setPen(Qt.black)
        size = self.size()
        for i in range(2000):
            x = random.randint(1, size.width() - 1)
            y = random.randint(1, size.height() - 1)
            qp.drawPoint(x, y)


    def drawRectangles(self, qp):
        qp.setPen(Qt.black)
        size = self.size()
        qp.setBrush(Qt.red)
        qp.drawRect(size.width() - 50, size.height() - 50, 45, 45)
        qp.setBrush(Qt.green)
        qp.drawRect(size.width() - 100, size.height() - 50, 45, 45)

    def fillComboBox(self, values, element):
        for i in range(len(values)):
            element.addItem(values[i])

    def selectedComboBox(self, textvalue):
        textvalue = f'Selected: {textvalue}'
        self.combolabel.setText(textvalue)




# жмём кнопку -> меняется цвет фона.
    def keyPressEvent(self, event):
        if event.key() == Qt.Key_L:
            self.centralform.setStyleSheet("background-color: #3ff33f;")

    def keyReleaseEvent(self, event):
        if event.key() == Qt.Key_L:
            self.centralform.setStyleSheet("background-color: #ffffff;")

    def mouseMoveEvent(self, event):

        self.mousetracklabel.setText(f"Mouse coords: {event.x()} : {event.y()}")
        print(event.x(), event.y())


# что-то типо отладчика


def my_excepthook(type, value, tback):
    QMessageBox.critical(
        w, "CRITICAL ERROR", str(value),
        QMessageBox.Cancel
    )

    sys.__excepthook__(type, value, tback)


sys.excepthook = my_excepthook

if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MyWindow()
    w.show()
    sys.exit(app.exec_())
