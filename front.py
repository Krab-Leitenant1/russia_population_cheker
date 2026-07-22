#from PyQt6.QtCore import Qt, QSize
from PyQt6.QtWidgets import  QMainWindow, QWidget, QVBoxLayout, QLabel, QApplication, QPushButton
import sys
import sqlite3



class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Russia population checker")
        self.setMinimumSize(300, 500)
        self.label = QLabel("Russia Population Checker")
        self.label1 = QLabel("Date:")
        self.label2 = QLabel("Count:")
        self.label3 = QLabel("Previous:")
        self.button = QPushButton("Update")
        self.button.clicked.connect(self.update_info)
        layout = QVBoxLayout()
        layout.addWidget(self.button)
        layout.addWidget(self.label)
        layout.addWidget(self.label1)
        layout.addWidget(self.label2)
        layout.addWidget(self.label3)
        con = QWidget()
        con.setLayout(layout)
        self.setCentralWidget(con)
        self.last_data = ()
        self.prev_data = ()

    def update_info(self):
        with sqlite3.connect('db.sqlite3') as con:
            cursor = con.cursor()
            data = cursor.execute('SELECT count, date FROM data').fetchall()
            print(data)

            if len(data) > 0:



                if data[-1] != self.last_data:
                    self.last_data = data[-1]
            if len(data) > 1:
                for i in data[::-1]:
                    if i[-1] !=self.last_data[-1]:
                        self.prev_data = i
                        break

        print(self.prev_data)
        try:
            self.label1.setText(f"Date: {self.last_data[-1]}")
            self.label2.setText(f"Count: {self.last_data[0]}")
        except:
            pass
        try:
            self.label3.setText(f"Previous: {self.prev_data[-1]}, {self.prev_data[0]}")
        except:
            pass

app = QApplication(sys.argv)
window = MainWindow()
window.update_info()
window.show()
app.exec()