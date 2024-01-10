'''
ÜBERBLICK: Supporter
    erbt alles von User
    +
    erweiterte Funktionalitäten:
        - Support-Notiz erstellen können
        - Priorität einstellen
'''

import sys
import mysql.connector
from PySide6.QtWidgets import QApplication, QTreeWidget, QTreeWidgetItem, QPushButton, QVBoxLayout, QWidget, QLabel, \
    QLineEdit, QTextEdit, QSpinBox, QDialog
import time
import user_help
import windowUser
import logging


class guiSupporter(windowUser.guiUser):
    def __init__(self):
        super().__init__()

        #initalisiere das UI
        self.initSupporterUI()


    def initSupporterUI(self):
        #CODE-ERGÄNZUNGEN CHILD
        self.lbl_erweiterteFunktionalitaeten = QLabel("ERWEITERTE FUNKTIONALITÄTEN (Supporter & Admin)")
        self.lbl_supportnotiz = QLabel("Support-Notiz:")
        self.txt_supportnotiz = QTextEdit()
        self.btn_uebernehmen = QPushButton("übernehmen")

        self.lbl_prioritaetskategorie = QLabel("Prioritätskategorie:")

        self.sb_prioritaetskategorie = QSpinBox()
        self.sb_prioritaetskategorie.setMaximum(3)

        windowUser.guiUser.layout(self).addWidget(self.lbl_erweiterteFunktionalitaeten)
        windowUser.guiUser.layout(self).addWidget(self.lbl_supportnotiz)
        windowUser.guiUser.layout(self).addWidget(self.txt_supportnotiz)
        windowUser.guiUser.layout(self).addWidget(self.lbl_prioritaetskategorie)
        windowUser.guiUser.layout(self).addWidget(self.sb_prioritaetskategorie)
        windowUser.guiUser.layout(self).addWidget(self.btn_uebernehmen)

        self.btn_uebernehmen.clicked.connect(self.uebernehmeAenderungen)

        self.supp_window = QDialog()

        pass

    #UNTERFUNKTIONENy
    def erstelleSupportnotiz(self):
        #Support-Notiz soll aus Textfeld in DB übernommen werden
        self.wert_supportnotiz = self.txt_supportnotiz.toPlainText()
        pass

    def vergebePrioritaetskategorie(self):
        #Prioritaetskategorie für Ticket soll aus Spinbox in DB übernommen werden
        self.wert_prioritaetskategorie = self.sb_prioritaetskategorie.value()
        pass

    def uebernehmeAenderungen(self):
        print("Änderungen übernehmen...")
        pass
#CHECK
    def leereFelder(self):
        super().leereFelder()
        #Parent-Erweiterung
        self.txt_supportnotiz.clear()
        self.sb_prioritaetskategorie.setValue(0)
        pass
#CHECK
    def klickeItem(self, item, column):
        super().klickeItem(item, column)
        #Parent-Erweiterung
        self.inhalte_supportnotiz = item.text(7)
        self.inhalte_prioritaetskategorie = item.text(8)
        self.inhalte_ticketid = item.text(0)
        pass
#CHECK
    def kopiereInhalte(self):
        super().kopiereInhalte()
        #Parent-Erweiterung
        if hasattr(self, 'inhalte_supportnotiz'):
            self.txt_supportnotiz.setPlainText(str(self.inhalte_supportnotiz))
            pass

        if hasattr(self, 'inhalte_prioritaetskategorie'):
            self.sb_prioritaetskategorie.setValue(int(self.inhalte_prioritaetskategorie))
            pass

        if hasattr(self, 'inhalte_ticketid'):
            self.ticketid_treeview = int(self.inhalte_ticketid)
            pass


    # !!!
    def uebernehmeAenderungen(self):

        try:
            print("ÄNDERUNGEN ÜBERNEHMEN")

            # Daten aus den UI-Elementen extrahieren
            ticketid = self.ticketid_treeview
            bezeichnung = self.txt_bezeichnung.text()
            problembeschreibung = self.txt_problembeschreibung.toPlainText()
            supportnotiz = self.txt_supportnotiz.toPlainText()
            prioritaetskategorie = self.sb_prioritaetskategorie.value()

            # SQL-Befehl: Update
            update_query = f"UPDATE ticket SET bezeichnung = %s, problembeschreibung = %s, supportnotiz = %s, prioritaetskategorie = %s WHERE ticketid = {ticketid}"
            data_to_update = (bezeichnung, problembeschreibung, supportnotiz, prioritaetskategorie)
            bearbeiter = user_help.user_id
            append_query = f"UPDATE Ticket SET bearbeiter = CONCAT(bearbeiter,' {bearbeiter},') WHERE ticketid = {ticketid}"
            cursor = self.connection.cursor()
            cursor.execute(append_query)
            cursor.execute(update_query, data_to_update)
            self.connection.commit()

        except Exception as e:
            logging.error(f"Fehler bei der Änderungsübernahme: {str(e)}")

    def erstelleTicket02(self):
        try:
            timestamp = time.strftime('%Y-%m-%d %H:%M:%S')
            bezeichnung = self.txt_bezeichnung.text()
            problembeschreibung = self.txt_problembeschreibung.toPlainText()
            supportnotiz = self.txt_supportnotiz.toPlainText()
            prioritaetskategorie = self.sb_prioritaetskategorie.value()
            insert_query = "INSERT INTO ticket (ticketid, bezeichnung, ersteller, problembeschreibung, zeitstempel, bearbeiter, status, supportnotiz, prioritaetskategorie) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
            data_to_insert = ("", bezeichnung, user_help.user_id, problembeschreibung, timestamp, "", "", supportnotiz, prioritaetskategorie)
            cursor = self.connection.cursor(prepared=True)
            cursor.execute(insert_query, data_to_insert)
            self.connection.commit()

        except Exception as e:
            logging.error(f"Fehler während der Ticket-Erstellung: {str(e)}")

    supporter = 1
    def erstelleTicket(self):
        super().erstelleTicket()
        if self.supporter == 1:
            self.erstelleTicket02()
            pass


#FUNKTIONSAUFRUF
if __name__ == "__main__":
    app = QApplication([])
    guiSupporter = guiSupporter()
    guiSupporter.show()
    app.exec_()