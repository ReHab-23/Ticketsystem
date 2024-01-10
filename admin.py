'''
ÜBERBLICK: Admin
    > erbt alles von Supporter <
    - Button: User-Verwaltung
'''

import sys
import mysql.connector
from PySide6.QtWidgets import QApplication, QTreeWidget, QTreeWidgetItem, QPushButton, QVBoxLayout, QWidget, QLabel, \
    QLineEdit, QTextEdit, QSpinBox, QDialog
import supporter
import PySide6

import windowUser


class guiAdmin(supporter.guiSupporter, windowUser.guiUser):
    def __init__(self):
        super().__init__()

        #initalisiere das UI
        self.initAdminUI()


    def initAdminUI(self):
        #CODE-ERGÄNZUNGEN CHILD
        self.btn_userverwaltung = QPushButton("User-Verwaltung")
        windowUser.guiUser.layout(self).addWidget(self.btn_userverwaltung)
        self.btn_userverwaltung.clicked.connect(self.oeffne_userverwaltung)
        self.admin_window = QDialog()


        pass



    #UNTERFUNKTIONEN
    def oeffne_userverwaltung(self):
        #Öffne Fenster für Userverwaltung
        print("User-Verwaltung öffnen...")
        pass


#FUNKTIONSAUFRUF
if __name__ == "__main__":
    app = QApplication([])
    guiAdmin = guiAdmin()
    guiAdmin.show()
    app.exec_()