#! python3
# -*- coding: utf-8 -*-


""" File rename program for a sequential pattern """


import os
import sys
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QSize    


class Renomator(QMainWindow):
    """ Main Class """
    def __init__(self):
        super().__init__()
        self.title = 'RENOMATOR - By WhoisBsa'
        self.width = 500
        self.height = 180
        
        # Importants Variables
        self.directory = ''
        self.source = ''
        self.date = ''
        self.type = ''

        self.initUI()


    def initUI(self):
        self.setWindowTitle(self.title)
        self.setMinimumSize(QSize(500, 180))

        self.centralWidget = QWidget(self)          
        self.setCentralWidget(self.centralWidget)   
        self.gridLayout = QGridLayout(self)     
        self.centralWidget.setLayout(self.gridLayout)

        # Methods
        self.search_directory()
        self.select_souce()
        self.select_year()
        self.type_file()
        self.buttons()
        self.show()


    def search_directory(self):
        # Create textbox_search
        self.textbox_search = QLineEdit(self)
        self.label_search = QLabel()
        self.label_search.setText('Select the Directory:')    

        # Create a button in the window
        self.button = QPushButton('BROWSE', self)
        self.button.move(340,20)
        self.button.resize(120, 30)

        self.gridLayout.addWidget(self.label_search, 0, 0)
        self.gridLayout.addWidget(self.textbox_search, 0, 1)
        self.gridLayout.addWidget(self.button, 0, 2)
        

        # connect button to function on_click
        self.button.clicked.connect(self.get_directory)


    def get_directory(self):
        directory = QtWidgets.QFileDialog.getExistingDirectory(self, 'Select directory')
        self.textbox_search.setText(str(directory))
        self.directory = self.textbox_search.text()


    def select_souce(self):
        self.textbox_source = QLineEdit(self)
        self.label_source = QLabel()
        self.label_source.setText('Select the Source:')
        
        self.gridLayout.addWidget(self.label_source, 1, 0)
        self.gridLayout.addWidget(self.textbox_source, 1, 1)


    def select_year(self):
        self.textbox_year = QLineEdit(self)
        self.label_year = QLabel()
        self.label_year.setText('Select the year:')
        
        self.gridLayout.addWidget(self.label_year, 2, 0)
        self.gridLayout.addWidget(self.textbox_year, 2, 1)


    def type_file(self):
        self.label_type = QLabel()
        self.label_type.setText('Select the Type of File:')
        self.types = QComboBox()
        self.types.addItems(["pdf", "txt", "xls", "docx"])

        self.gridLayout.addWidget(self.label_type, 3, 0)
        self.gridLayout.addWidget(self.types, 3, 1)


    def buttons(self):
        self.okButton = QPushButton("Renomear")
        self.cancelButton = QPushButton("Cancel")

        self.gridLayout.addWidget(self.okButton, 4, 1)
        self.gridLayout.addWidget(self.cancelButton, 4, 2)

        self.cancelButton.clicked.connect(self.cancel)
        self.okButton.clicked.connect(self.ok_button)

    
    def cancel(self):
        QtCore.QCoreApplication.instance().quit()
    

    def ok_button(self):
        self.directory = self.directory + '/'
        self.source = self.textbox_source.text()
        self.date = self.textbox_year.text()
        self.type = str(self.types.currentText())

        os.chdir(self.directory)

        for root, _, files in os.walk(self.directory):
            for i, file in enumerate(files):
                if file.endswith(self.type):
                    os.rename(os.path.join(root, file), 
                        f'{self.source}_{i+1:03}_{self.date}.{self.type}')

        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)

        msg.setText("Successfully Renamed Files!")
        retval = msg.exec_()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mainWin = Renomator()
    mainWin.show()
    sys.exit(app.exec_())
