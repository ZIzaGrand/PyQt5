from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys


class Window(QMainWindow):
    def __init__(self):
        super(Window, self).__init__()

        self.setWindowTitle("Мышинная программа")
        self.setGeometry(300, 250, 350, 200)

        self.some_text = QtWidgets.QLabel(self)

        self.main_label = QtWidgets.QLabel(self)
        self.main_label.setText("Мыши бегают по бардюрам")
        self.main_label.move(100, 100)
        self.main_label.adjustSize()

        self.button = QtWidgets.QPushButton(self)
        self.button.move(70, 150)
        self.button.setText("Нажми на мышь!!!")
        self.button.setFixedWidth(200) 
        self.button.clicked.connect(self.mouse)



    def mouse(self):
        
        self.some_text.setText("Мышь 2")
        self.some_text.move(100, 50)
        self.some_text.adjustSize()



def application():
    app = QApplication(sys.argv)
    main_window = Window()

    main_window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    application()