import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic, QtGui
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
        self.setMouseTracking(True)

    def changeBackground(self):
        if self.flagbackground == 0:
            self.centralwidget.setStyleSheet("background-color: #999999;")
            self.flagbackground = 1
        else:
            self.centralwidget.setStyleSheet("background-color: #ffffff;")
            self.flagbackground = 0

    def addListValue(self):
        self.valuesList.append(self.textEdit.toPlainText())
        sti = QtGui.QStandardItemModel(parent=w)
        for i in self.valuesList:
            item = QtGui.QStandardItem(i)
            sti.appendRow(item)
        self.listView.setModel(sti)

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

# жмём кнопку -> меняется цвет фона.
    def keyPressEvent(self, event):
        if event.key() == Qt.Key_L:
            self.centralwidget.setStyleSheet("background-color: #3ff33f;")

    def keyReleaseEvent(self, event):
        if event.key() == Qt.Key_L:
            self.centralwidget.setStyleSheet("background-color: #ffffff;")

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
