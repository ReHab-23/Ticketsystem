# Import der Frame Works
import bcrypt
from PySide6.QtWidgets import QApplication, QMainWindow, QTreeWidgetItem
import user_help
from login import Ui_login_frm
from pwinput import *
import mysql.connector
import ctypes
from register import Ui_Registrieren
from register import *
from verwaltung import Ui_verwaltung
from windowUser import *
from supporter import *
from admin import *
from PySide6.QtCore import QObject, Signal
from user_help import set_user,get_user
import ctypes

# auslesen der txt datei
auslesen = open("user.txt", "r")
userdbcon = []
salt = bcrypt.gensalt()
for zeile in auslesen:
    userdbcon.append(zeile.strip())
auslesen.close()

# aufbauen der Datenbank verbindung mit den Daten aus der txt datei
mydb = mysql.connector.connect(
    host=userdbcon[0],
    user=userdbcon[1],
    password=userdbcon[2],
    database=userdbcon[3]
)

#erstellen des Main Frames
class Frm_main(QMainWindow):
    def __init__(self):
        super().__init__()
        #Initatlisieren der einzelnen Frames
        self.ui = Ui_login_frm()
        self.ui.setupUi(self)
        self.ui_register = Ui_Registrieren()
        self.ui_verwalt = Ui_verwaltung()
        self.ui_user = guiUser()
        self.ui_supp = guiSupporter()
        self.ui_admin = guiAdmin()



        # Verknüpfung der Schaltflächen mit Funktionen
        self.ui.loginbtn.clicked.connect(self.login)
        self.ui.Register.clicked.connect(self.register)


    # Aufbau der UIs
    def user_ui(self):
        self.ui_user.show()

    def supp_ui(self):
        self.ui_supp.show()

    def admin_ui(self):
        self.ui_admin.btn_userverwaltung.clicked.connect(self.verwaltung)
        self.ui_admin.show()

# Beschreibung der Funktionen der main datei, teilweise notwendig sie aus den anderen Klassen hier hin aus zu lagern
# da sonst einige Fehler aufgetreten sind die nicht nachvollziehbar waren.
    def login(self):
        # Auslesen des Usernames und des Passwortes

        username = self.ui.lineEdit_2.text()
        passworteingabe = self.ui.lineEdit.text()
        password = passworteingabe

        mycursor = mydb.cursor()
        #fraglich ob die while schleife von nöten ist erstmal belassen da alles so funktioniert
        while True:
            try:
                #Aufbau des Cursors zum auslesen des Passwortes in der Datenbank und auslesen des Ergebnis
                mycursor.execute(f"SELECT passwort From benutzer where ID = {username};")
                result = mycursor.fetchone()
                storedpw = result[0]

                #überprüfen des gehashten Passwortes das aus der Datenbank ausgelsen wurde
                if bcrypt.checkpw(password.encode('utf-8'),storedpw.encode('utf-8')):
                    ctypes.windll.user32.MessageBoxW(0, "Die Eingaben sind richtig", "Erfolg", 1)

                    #Überprüfung der Berechtigung wird eingeleitet
                    mycursor.execute(f"SELECT Klasse From benutzer where ID = {username}")
                    klasse = mycursor.fetchone()
                    user_help.set_user(username)

                    #Je nach User Rechten wird das entsprechende Fenster geöffnet.
                    if klasse[0] == 0:
                        break
                    elif klasse[0] == 1:
                        print(f"Hallo User {user_help.user_id}")
                        self.ui_user.btn_passwort.clicked.connect(self.passwort)

                        self.user_ui()
                        self.ui_user.ladeTreeview()
                        break
                    elif klasse[0] == 2:
                        print("Hallo Supporter")

                        self.supp_ui()
                        self.ui_supp.btn_passwort.clicked.connect(self.passwort)
                        self.ui_supp.ladeTreeview()
                        break
                    elif klasse[0] == 3:
                        print("Hallo Admin")

                        self.admin_ui()
                        self.ui_admin.btn_passwort.clicked.connect(self.passwort)
                        self.ui_admin.ladeTreeview()

                        break

                else:
                    ctypes.windll.user32.MessageBoxW(0, "Die Eingaben sind Fehlerhaft bitte erneut versuchen!", "Fehler", 1)
                    break
            except ValueError:
                ctypes.windll.user32.MessageBoxW(0, "Die Eingaben sind Fehlerhaft bitte erneut versuchen!", "Fehler", 1)
                break

    def register(self):
        # Aufbau für das Register Fenster
        self.register_window = QDialog()  # Hier ein geeignetes QWidget-Objekt erstellen
        self.ui_register.setupUi(self.register_window)
        self.ui_register.pushButtonRegister.clicked.connect(self.ui_register.registrieren)
        self.ui_register.pushButtonZurueck.clicked.connect(self.zurueck)
        self.register_window.show()
        self.close()
        try:
            self.login_window.close()
        except AttributeError:
            pass
# Die closes müssen noch überarbeitet werden 02.01.2024
# Closes überarbeitet mit einem try except verfahren was den AttributeError abfängt




    def verwaltung(self):
        self.verwaltung_window = QDialog()
        self.ui_verwalt = Ui_verwaltung()
        self.ui_verwalt.setupUi(self.verwaltung_window)

        self.ui_verwalt.zuweisenbtn.clicked.connect(self.zuweisung)
        self.ui_verwalt.loeschenbtn.clicked.connect(self.entfernen)
        self.ui_verwalt.resetbtn.clicked.connect(self.zuruecksetzten)
        self.verwaltung_window.showEvent = self.on_verwaltung_window_shown

        self.verwaltung_window.show()

    def passwort(self):
            try:

                username = user_help.get_user()
                passwortcursosr = mydb.cursor()
                self.user = user_help.get_user()
                mycursor = mydb.cursor()
                mycursor.execute(f"SELECT Klasse From benutzer where ID = {username}")
                klasse = mycursor.fetchone()
                if klasse[0] == 1:
                    password = self.ui_user.txt_passwort.text()

                elif klasse[0] == 2:
                    password = self.ui_supp.txt_passwort.text()

                elif klasse[0] == 3:
                    password = self.ui_admin.txt_passwort.text()


                salt = bcrypt.gensalt()
                hashed_password = bcrypt.hashpw(password.encode('utf-8'),salt)
                value = (hashed_password.decode('utf-8'), self.user)
                statement = f'UPDATE benutzer SET Passwort = %s WHERE ID = %s'
                passwortcursosr.execute(statement, value)
                mydb.commit()

                passwortcursosr.close()
                ctypes.windll.user32.MessageBoxW(0,"Ihre Änderung wurde vorgenommen!", "Passwort geändert",1)
            except Exception as e:
                ctypes.windll.user32.MessageBoxW(f"Fehler beim Updaten: {e}")

    def on_verwaltung_window_shown(self, event):
        self.ui_verwalt.treeView_2.clear()
        cursor2 = mydb.cursor()
        cursor2.execute("SELECT * from benutzer WHERE Klasse > 0")
        for row in cursor2.fetchall():
            item = QTreeWidgetItem(self.ui_verwalt.treeView_2)
            pass
            for i in range(len(row)):
                item.setText(i, str(row[i]))
                pass
        self.ui_verwalt.treeView.clear()
        cursor1 = mydb.cursor()
        cursor1.execute("SELECT * from benutzer WHERE Klasse = 0")
        for row in cursor1.fetchall():
            item = QTreeWidgetItem(self.ui_verwalt.treeView)
            pass

            for i in range(len(row)):
                item.setText(i, str(row[i]))
                pass
        cursor1.close()
        cursor2.close()
    def zurueck(self):
        self.register_window.close()
        self.login_window = QMainWindow()
        self.ui = Ui_login_frm()
        self.ui.setupUi(self.login_window)
        self.ui.loginbtn.clicked.connect(self.login)
        self.ui.Register.clicked.connect(self.register)
        self.login_window.show()

    def zuweisung(self):
        zuweiser = mydb.cursor()
        userid = self.ui_verwalt.lineEdit.text()
        klasse = self.ui_verwalt.spinBox.text()
        values = klasse, userid
        statment = f'UPDATE benutzer SET Klasse=%s WHERE ID = %s'
        zuweiser.execute(statment, values)
        mydb.commit()
        zuweiser.close()
        self.ui_verwalt.treeView_2.clear()
        cursor2 = mydb.cursor()
        cursor2.execute("SELECT * from benutzer WHERE Klasse > 0")
        for row in cursor2.fetchall():
            item = QTreeWidgetItem(self.ui_verwalt.treeView_2)
            pass
            for i in range(len(row)):
                item.setText(i, str(row[i]))
                pass
        self.ui_verwalt.treeView.clear()
        cursor1 = mydb.cursor()
        cursor1.execute("SELECT * from benutzer WHERE Klasse = 0")
        for row in cursor1.fetchall():
            item = QTreeWidgetItem(self.ui_verwalt.treeView)
            pass

            for i in range(len(row)):
                item.setText(i, str(row[i]))
                pass
        cursor1.close()
        cursor2.close()

    def entfernen(self):
        entfernencursor = mydb.cursor()
        userid = self.ui_verwalt.lineEdit.text()
        value = userid
        statmentent= f'DELETE FROM benutzer WHERE ID = %s'
        entfernencursor.execute(statmentent, (value,))
        mydb.commit()
        entfernencursor.close()
        self.ui_verwalt.treeView_2.clear()
        cursor2 = mydb.cursor()
        cursor2.execute("SELECT * from benutzer WHERE Klasse > 0")
        for row in cursor2.fetchall():
            item = QTreeWidgetItem(self.ui_verwalt.treeView_2)
            pass
            for i in range(len(row)):
                item.setText(i, str(row[i]))
                pass
        self.ui_verwalt.treeView.clear()
        cursor1 = mydb.cursor()
        cursor1.execute("SELECT * from benutzer WHERE Klasse = 0")
        for row in cursor1.fetchall():
            item = QTreeWidgetItem(self.ui_verwalt.treeView)
            pass

            for i in range(len(row)):
                item.setText(i, str(row[i]))
                pass
        cursor1.close()
        cursor2.close()

    def zuruecksetzten(self):
        cursor = mydb.cursor()
        userid = self.ui_verwalt.lineEdit.text()
        password = "Hamburg1"
        salt = bcrypt.gensalt()
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
        value = (hashed_password.decode('utf-8'), userid)
        statement = f'UPDATE benutzer SET Passwort = %s  WHERE ID = %s'
        try:
            cursor.execute(statement, value)
            mydb.commit()
            cursor.close()
            ctypes.windll.user32.MessageBoxW(0,'Passwort Erfolgreich zurückgesetzt, vorläufiges Passwort ist: Hamburg1',"Passwort Änderung",1)
        except Exception as e:
            ctypes.windll.user32.MessageBoxW(f"Fehler beim Zurücksetzten des Passwortes: {e}")


seite = "__main__"
name = __name__
if name == seite:
    app = QApplication([])
    frm_main = Frm_main()
    frm_main.show()



    app.exec()