# -*- coding: utf-8 -*-
import ctypes

################################################################################
## Form generated from reading UI file 'register.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QDialog, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QWidget)
import mysql.connector
import bcrypt
from passworthash import PasswordHasher

auslesen = open("user.txt", "r")
userdbcon = []

for zeile in auslesen:
    userdbcon.append(zeile.strip())
auslesen.close()


mydb = mysql.connector.connect(
    host=userdbcon[0],
    user=userdbcon[1],
    password=userdbcon[2],
    database=userdbcon[3]
)
class Ui_Registrieren(object):
    def setupUi(self, Registrieren):
        if not Registrieren.objectName():
            Registrieren.setObjectName(u"Registrieren")
        Registrieren.resize(505, 527)

        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Registrieren.sizePolicy().hasHeightForWidth())
        Registrieren.setSizePolicy(sizePolicy)

        self.lineEditVorname = QLineEdit(Registrieren)
        self.lineEditVorname.setObjectName(u"lineEditVorname")
        self.lineEditVorname.setGeometry(QRect(190, 100, 113, 22))

        self.lineEditNachname = QLineEdit(Registrieren)
        self.lineEditNachname.setObjectName(u"lineEditNachname")
        self.lineEditNachname.setGeometry(QRect(190, 150, 113, 22))

        self.lineEditRaum = QLineEdit(Registrieren)
        self.lineEditRaum.setObjectName(u"lineEditRaum")
        self.lineEditRaum.setGeometry(QRect(190, 290, 113, 22))

        self.lineEditKurs = QLineEdit(Registrieren)
        self.lineEditKurs.setObjectName(u"lineEditKurs")
        self.lineEditKurs.setGeometry(QRect(190, 240, 113, 22))

        self.lineEditEMail = QLineEdit(Registrieren)
        self.lineEditEMail.setObjectName(u"lineEditEMail")
        self.lineEditEMail.setGeometry(QRect(190, 340, 113, 22))

        self.label = QLabel(Registrieren)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(191, 80, 49, 16))

        self.label_2 = QLabel(Registrieren)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(191, 130, 71, 16))

        self.label_3 = QLabel(Registrieren)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(191, 220, 31, 20))

        self.label_4 = QLabel(Registrieren)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(191, 270, 49, 16))

        self.label_5 = QLabel(Registrieren)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(191, 320, 49, 16))

        self.pushButtonRegister = QPushButton(Registrieren)
        self.pushButtonRegister.setObjectName(u"pushButtonRegister")
        self.pushButtonRegister.setGeometry(QRect(195, 380, 101, 51))

        self.pushButtonZurueck = QPushButton(Registrieren)
        self.pushButtonZurueck.setObjectName(u"pushButtonZurueck")
        self.pushButtonZurueck.setGeometry(QRect(210, 450, 75, 24))

        self.lineEditPasswort = QLineEdit(Registrieren)
        self.lineEditPasswort.setObjectName(u"lineEditPasswort")
        self.lineEditPasswort.setGeometry(QRect(190, 200, 113, 22))

        self.label_6 = QLabel(Registrieren)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(191, 180, 49, 16))

        QWidget.setTabOrder(self.lineEditVorname, self.lineEditNachname)
        QWidget.setTabOrder(self.lineEditNachname, self.lineEditPasswort)
        QWidget.setTabOrder(self.lineEditPasswort, self.lineEditKurs)
        QWidget.setTabOrder(self.lineEditKurs, self.lineEditRaum)
        QWidget.setTabOrder(self.lineEditRaum, self.lineEditEMail)
        QWidget.setTabOrder(self.lineEditEMail, self.pushButtonRegister)
        QWidget.setTabOrder(self.pushButtonRegister, self.pushButtonZurueck)

        self.retranslateUi(Registrieren)
        """self.pushButtonRegister.pressed.connect(self.lineEditEMail.undo)
        self.pushButtonRegister.pressed.connect(self.lineEditRaum.undo)
        self.pushButtonRegister.pressed.connect(self.lineEditKurs.undo)
        self.pushButtonRegister.pressed.connect(self.lineEditPasswort.undo)
        self.pushButtonRegister.pressed.connect(self.lineEditNachname.undo)
        self.pushButtonRegister.pressed.connect(self.lineEditVorname.undo)"""

        QMetaObject.connectSlotsByName(Registrieren)
    # setupUi

    def retranslateUi(self, Registrieren):
        Registrieren.setWindowTitle(QCoreApplication.translate("Registrieren", u"Registrieren", None))
        self.label.setText(QCoreApplication.translate("Registrieren", u"Vorname", None))
        self.label_2.setText(QCoreApplication.translate("Registrieren", u"Nachname", None))
        self.label_3.setText(QCoreApplication.translate("Registrieren", u"Kurs", None))
        self.label_4.setText(QCoreApplication.translate("Registrieren", u"Raum", None))
        self.label_5.setText(QCoreApplication.translate("Registrieren", u"E-Mail", None))
        self.pushButtonRegister.setText(QCoreApplication.translate("Registrieren", u"Registrieren", None))
        self.pushButtonZurueck.setText(QCoreApplication.translate("Registrieren", u"Zur\u00fcck", None))
        self.label_6.setText(QCoreApplication.translate("Registrieren", u"Passwort", None))
    # retranslateUi


    def registrieren(self):
        vorname = self.lineEditVorname.text()
        nachname = self.lineEditNachname.text()
        passworteingabe = self.lineEditPasswort.text()

        passwort = PasswordHasher.hash_password(passworteingabe)
        kurs = self.lineEditKurs.text()
        raum = self.lineEditRaum.text()
        email = self.lineEditEMail.text()
        dbcursor = mydb.cursor()
        dbcursor2 = mydb.cursor(buffered=True)

        emailcheck = f'Select * from benutzer WHERE mail = %s'
        dbcursor2.execute(emailcheck, (email,))
        existing_email =dbcursor2.fetchone()


        sql = "INSERT INTO benutzer (Vorname,Nachname,passwort,Kurs,Raum,Mail) VALUES (%s, %s, %s, %s,%s,%s)"
        values = vorname, nachname,passwort,kurs,raum,email

        if existing_email:
            ctypes.windll.user32.MessageBoxW(0,"E-Mail wird bereits benutzt","Fehler", 1)
        else:
            try:
                dbcursor.execute(sql,values)
                mydb.commit()
                ctypes.windll.user32.MessageBoxW(0, "Erfolgreich registiert sie werden im Laufe der Woche freigeschaltet","Erfolg",1)
                dbcursor.close()
            except mysql.connector.Error as error:
                ctypes.windll.user32.MessageBoxW(0,f"Fehler beim Registrieren Fehler:{error}", "Fehler",1)


