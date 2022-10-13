from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow, QMenuBar, QMenu, QFileDialog, QMessageBox
import sys


class Window(QMainWindow):

    def __init__(self):
        super(Window, self).__init__()

        self.setWindowTitle("Редактор текста")
        self.setGeometry(300, 250, 350, 350)

        self.text_editor = QtWidgets.QTextEdit(self)
        self.setCentralWidget(self.text_editor)

        self.createMenuBar()
            

    def createMenuBar(self):
        self.menu_bar = QMenuBar(self)
        self.setMenuBar(self.menu_bar)

        file_menu = QMenu("&Файл", self)
        self.menu_bar.addMenu(file_menu)

        file_menu.addAction("Открыть", self.action_clicked)
        file_menu.addAction("Сохранить", self.action_clicked)

        
    @QtCore.pyqtSlot()
    def action_clicked(self):
        action = self.sender()
        if action.text() == "Открыть":
            fname = QFileDialog.getOpenFileName(self)[0]

            try:

                f = open(fname, "r")
                with f:
                    data = f.read()
                    self.text_editor.setText(data)

                f.close

            except FileNotFoundError:
                error = QMessageBox()
                error.setWindowTitle("Файл не выбран")
                error.setText("Выберите файл для того чтобы открыть в редакторе")
                error.setIcon(QMessageBox.Warning)
                error.setStandardButtons(QMessageBox.Ok)

                error.exec_()

        elif action.text() == "Сохранить":
            fname = QFileDialog.getSaveFileName(self)[0]
            try:

                f = open(fname, "w")
                text = self.text_editor.toPlainText()
                f.write(text)
                f.close

            except FileNotFoundError:
                error = QMessageBox()
                error.setWindowTitle("Файл не сохранён")
                error.setText("Файл не сохранён")
                error.setIcon(QMessageBox.Warning)
                error.setStandardButtons(QMessageBox.Ok)

                error.exec_()



def application():
    app = QApplication(sys.argv)
    window = Window()

    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    application()
