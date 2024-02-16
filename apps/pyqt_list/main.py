from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow, QGridLayout, QWidget, QListWidget, QListWidgetItem, QPushButton, QLineEdit
from PyQt5.QtCore import Qt
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.setGeometry(200, 200, 800, 600)
        self.setWindowTitle('General Item List')
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.layout = QGridLayout(self.central_widget)
        self.initUI()
    
        
    def initUI(self):
        # Create 
        self.title = QLabel('Items in list:', self)
        self.list_widget = QListWidget()
        self.enter_text = QLineEdit()
        self.add_button = QPushButton('Add to list')

        self.add_button.clicked.connect(self.add_to_list)

        with open('python_projects/pyqt_list/data.txt', 'r') as file: # change this
            data_str = file.read()
        self.data = data_str.split(',')

        for item_text in self.data:
            item = QListWidgetItem(item_text)
            self.list_widget.addItem(item)
        

        # Layout
        self.layout.addWidget(self.title, 0, 0, alignment=Qt.AlignBottom)
        self.layout.addWidget(self.list_widget, 1, 0, alignment=Qt.AlignLeft)
        self.layout.addWidget(self.enter_text, 1, 1, alignment=Qt.AlignBottom)
        self.layout.addWidget(self.add_button, 2, 1, alignment=Qt.AlignTop)


    def add_to_list(self):
        self.list_widget.addItem(self.enter_text.text())
        self.data.append(f'{self.enter_text.text()}')
        data_str = ','.join([str(elem) for elem in self.data])

        with open('python_projects/pyqt_list/data.txt', 'w') as file:
            file.write(data_str)
        
            
    
        


app = QApplication(sys.argv)
win = MainWindow()

win.show()
sys.exit(app.exec_())