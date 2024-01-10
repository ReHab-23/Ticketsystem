'''
ÜBERBLICK: User
    - eigene Tickets einsehen (= selbsterstellte)
    - Tickets erstellen
        - User-Inputs: Bezeichnung + Problembeschreibung
'''

import sys
import mysql.connector
from PySide6.QtWidgets import QApplication, QTreeWidget, QTreeWidgetItem, QPushButton, QVBoxLayout, QWidget, QLabel, \
    QLineEdit, QTextEdit, QDialog
from PySide6.QtCore import QObject, Slot
import time
import user_help
from user_help import get_user,set_user


import bcrypt
from PySide6.QtCore import QObject, Signal
dbtxt = open("user.txt", "r")
userdbcon = []

for zeile in dbtxt:
    userdbcon.append(zeile.strip())
dbtxt.close()

class guiUser(QWidget):
    def __init__(self):
        super().__init__()

        self.user = user_help.get_user()

        #DB-VERBINDUNG ANGABEN
        self.connection = mysql.connector.connect(
            host=userdbcon[0],
            user=userdbcon[1],
            password=userdbcon[2],
            database=userdbcon[3]
        )

        #initialisiere das UI
        self.initUserUI()
    #MAIN-FUNKTION
    def initUserUI(self):
        #FENSTER ERZEUGEN
        self.setWindowTitle("BFW-Ticketsystem")
        self.setGeometry(100, 100, 1000, 950)

        #TREEVIEW ERSTELLEN
        self.tree = QTreeWidget()
        self.tree.setHeaderLabels(
            ["ticketid", "bezeichnung", "ersteller", "problembeschreibung", "zeitstempel", "bearbeiter", "status",
             "supportnotiz", "prioritaetskategorie"])


        #GUI-ELEMENTE ERZEUGEN & ANORDNEN
        #--->BUTTONS
        self.btn_ticket_erstellen = QPushButton("Ticket erstellen")
        self.btn_ticket_einsehen = QPushButton("Tickets einsehen")
        self.btn_daten_aktualisieren = QPushButton("Daten aktualisieren")
        self.btn_felder_leeren = QPushButton("Felder leeren")
        self.btn_logout = QPushButton("Logout")
        self.btn_passwort = QPushButton("Passwort zurücksetzten")

        #--->LABELS
        self.lbl_erweiterteNeuesTicket = QLabel("TICKET EINSEHEN & NEUES TICKET ERSTELLEN")
        self.lbl_bezeichnung = QLabel("Bezeichnung:")
        self.lbl_problembeschreibung = QLabel("Problembeschreibung:")
        self.lbl_passwort = QLabel("Neues Passwort eingeben:")

        #--->TEXTFELDER
        self.txt_bezeichnung = QLineEdit()
        self.txt_problembeschreibung = QTextEdit()
        self.txt_passwort = QLineEdit()

        #LAYOUT ERSTELLEN & ELEMENTE POSITIONIEREN
        layout = QVBoxLayout()
        layout.addWidget(self.tree)
        layout.addWidget(self.btn_ticket_einsehen)
        layout.addWidget(self.lbl_erweiterteNeuesTicket)
        layout.addWidget(self.lbl_bezeichnung)
        layout.addWidget(self.txt_bezeichnung)
        layout.addWidget(self.lbl_problembeschreibung)
        layout.addWidget(self.txt_problembeschreibung)
        layout.addWidget(self.btn_ticket_erstellen)
        layout.addWidget(self.btn_daten_aktualisieren)
        layout.addWidget(self.btn_felder_leeren)
        layout.addWidget(self.btn_logout)
        layout.addWidget(self.lbl_passwort)
        layout.addWidget(self.txt_passwort)
        layout.addWidget(self.btn_passwort)

        self.setLayout(layout)

        #BUTTON-FUNKTIONEN ZUWEISEN
        self.tree.itemClicked.connect(self.klickeItem)
        self.btn_ticket_einsehen.clicked.connect(self.kopiereInhalte)
        self.btn_ticket_erstellen.clicked.connect(self.erstelleTicket)
        self.btn_daten_aktualisieren.clicked.connect(self.ladeTreeview)
        self.btn_felder_leeren.clicked.connect(self.leereFelder)
        self.btn_logout.clicked.connect(self.logout)


        self.user_window = QDialog()


    #UNTERFUNKTIONEN
    def ladeTreeview(self):
        #Daten aus der DB im Treeview abrufen
        class_cursor = self.connection.cursor()

        class_cursor.execute(f"Select Klasse From benutzer WHERE ID = {user_help.user_id}")
        user_klasse = class_cursor.fetchone()[0]
        self.tree.clear()
        cursor = self.connection.cursor()
        if user_klasse >= 2:
            cursor.execute("SELECT * FROM ticket")
        else:
            cursor.execute(f"SELECT * FROM ticket WHERE Ersteller = {user_help.user_id}")
        #Daten dem Treeview hinzufügen
        for row in cursor.fetchall():
            item = QTreeWidgetItem(self.tree)
            pass
            for i in range(len(row)):
                item.setText(i, str(row[i]))
                pass

    #TICKETS EINSEHEN = itemclick + kopierenInhalte
    def klickeItem(self, item, column):
        #Daten aus ausgewähltem Item extrahieren
        self.inhalte_problembeschreibung = item.text(3)
        self.inhalte_bezeichnung = item.text(1)
        pass

    def kopiereInhalte(self):
        #kopiere markierten Text aus Textfeld
        if hasattr(self, 'inhalte_problembeschreibung'):
            self.txt_problembeschreibung.setPlainText(self.inhalte_problembeschreibung)
            pass
        if hasattr(self, 'inhalte_bezeichnung'):
            self.txt_bezeichnung.setText(self.inhalte_bezeichnung)
            pass

    def erstelleTicket1(self):
        #erstelle ein neues Ticket, nutze die Daten aus den Feldern Problembeschr. + Bezeichnung
        #bezeichnung = Inhalte des Textfelds txt_bezeichnung
        bezeichnung = self.txt_bezeichnung.text()
        problembeschreibung = self.txt_problembeschreibung.toPlainText()


        timestamp = time.strftime('%Y-%m-%d %H:%M:%S')
        print(timestamp)
        insert_query = "INSERT INTO ticket (ticketid, bezeichnung, ersteller, problembeschreibung, zeitstempel, bearbeiter, status, supportnotiz, prioritaetskategorie) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
        data_to_insert = ("", bezeichnung, user_help.user_id, problembeschreibung, timestamp, "", "", "", 0)

        cursor = self.connection.cursor()

        cursor.execute(insert_query, data_to_insert)

        self.connection.commit()

    supporter = 0
    def erstelleTicket(self):
        if self.supporter == 0:
            self.erstelleTicket1()
            pass
    def leereFelder(self):
        self.txt_bezeichnung.clear()
        self.txt_problembeschreibung.clear()
        pass

    def logout(self):
        self.connection.close()
        
        sys.exit()
        pass






#FUNKTIONSAUFRUF
if __name__ == "__main__":
    app = QApplication([])


    gui_user = guiUser()  # Übergebe den Benutzerwert beim Erstellen von guiUser
    gui_user.show()




    app.exec()