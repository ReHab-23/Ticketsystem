# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'verwaltung.ui'
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
    QPalette, QPixmap, QRadialGradient, QTransform, QStandardItemModel, QStandardItem)
from PySide6.QtWidgets import (QApplication, QDialog, QHeaderView, QLabel,
                               QLineEdit, QPushButton, QSizePolicy, QSpinBox,
                               QTreeView, QWidget, QTreeWidget, QBoxLayout, QTreeWidgetItem)

import mysql.connector


class Ui_verwaltung(object):
    test = open("user.txt", "r")
    userdbcon = []

    for zeile in test:
        userdbcon.append(zeile.strip())
    test.close()

    mydb = mysql.connector.connect(
        host=userdbcon[0],
        user=userdbcon[1],
        password=userdbcon[2],
        database=userdbcon[3]
        )
    def setupUi(self, verwaltung):
        if not verwaltung.objectName():
            verwaltung.setObjectName(u"verwaltung")
        verwaltung.resize(755, 609)
        self.treeView = QTreeWidget(verwaltung)
        self.treeView.setObjectName(u"treeView")
        self.treeView.setGeometry(QRect(10, 40, 731, 181))
        self.treeView.setHeaderLabels(["ID","Vorname","Nachname","Passwort","Kurs","Raum","Mail","Klasse"])

        self.label = QLabel(verwaltung)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(340, 20, 211, 16))

        self.spinBox = QSpinBox(verwaltung)
        self.spinBox.setObjectName(u"spinBox")
        self.spinBox.setGeometry(QRect(10, 250, 42, 22))
        self.spinBox.setMaximum(3)

        self.lineEdit = QLineEdit(verwaltung)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(90, 250, 113, 22))

        self.label_2 = QLabel(verwaltung)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(10, 230, 71, 16))

        self.label_3 = QLabel(verwaltung)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(90, 230, 49, 16))

        self.zuweisenbtn = QPushButton(verwaltung)
        self.zuweisenbtn.setObjectName(u"zuweisenbtn")
        self.zuweisenbtn.setGeometry(QRect(220, 250, 101, 24))
        self.loeschenbtn = QPushButton(verwaltung)

        self.resetbtn = QPushButton(verwaltung)
        self.resetbtn.setObjectName(u"zuweisenbtn")
        self.resetbtn.setGeometry(QRect(350,250, 130,24))

        self.loeschenbtn.setObjectName(u"loeschenbtn")
        self.loeschenbtn.setGeometry(QRect(640, 250, 81, 24))

        self.treeView_2 = QTreeWidget(verwaltung)
        self.treeView_2.setObjectName(u"treeView_2")
        self.treeView_2.setGeometry(QRect(10, 370, 731, 181))
        self.treeView_2.setHeaderLabels(["ID", "Vorname", "Nachname","Passwort", "Kurs", "Raum", "Mail", "Klasse"])

        self.label_4 = QLabel(verwaltung)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(10, 280, 61, 16))

        self.label_5 = QLabel(verwaltung)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(10, 300, 91, 16))

        self.label_6 = QLabel(verwaltung)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(120, 300, 61, 16))

        self.label_7 = QLabel(verwaltung)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(120, 280, 71, 16))

        self.retranslateUi(verwaltung)

        self.zuweisenbtn.setDefault(True)

        QMetaObject.connectSlotsByName(verwaltung)
    # setupUi

    def retranslateUi(self, verwaltung):
        verwaltung.setWindowTitle(QCoreApplication.translate("verwaltung", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("verwaltung", u"Neue Nutzer", None))
        self.label_2.setText(QCoreApplication.translate("verwaltung", u"User Rechte", None))
        self.label_3.setText(QCoreApplication.translate("verwaltung", u"User ID", None))
        self.zuweisenbtn.setText(QCoreApplication.translate("verwaltung", u"Rechte zuweisen", None))
        self.loeschenbtn.setText(QCoreApplication.translate("verwaltung", u"User L\u00f6schen", None))
        self.resetbtn.setText(QCoreApplication.translate("verwaltung", u"Passwort Zurücksetzten", None))
        self.label_4.setText(QCoreApplication.translate("verwaltung", u"0= Gesperrt", None))
        self.label_5.setText(QCoreApplication.translate("verwaltung", u"1= Standard User", None))
        self.label_6.setText(QCoreApplication.translate("verwaltung", u"3= Admin", None))
        self.label_7.setText(QCoreApplication.translate("verwaltung", u"2= Supporter", None))
    # retranslateUi



    def datenladenneu(self):
        self.treeView.clear()
        cursor1 = self.mydb.cursor()
        cursor1.execute("SELECT * from benutzer WHERE Klasse = 0")
        for row in cursor1.fetchall():
            item = QTreeWidgetItem(self.treeView)
            pass
            for i in range(len(row)):
                item.setText(i, str(row[i]))
                pass
        cursor1.close()


    def datenladenalt(self):
        self.treeView_2.clear()
        cursor2 = self.mydb.cursor()
        cursor2.execute("SELECT * from benutzer WHERE Klasse > 0")
        for row in cursor2.fetchall():
            item = QTreeWidgetItem(self.treeView_2)
            pass
            for i in range(len(row)):
                item.setText(i, str(row[i]))
                pass
        cursor2.close()


#        header = [i[0] for i in cursor.description]

#        model = QStandardItemModel()
#        model.setHorizontalHeaderLabels(header)
#        self.treeView_2.setModel(model)

#        for row in cursor.fetchall():
#            items = [QStandardItem(str(data)) for data in row]
#            model.appendRow(items)
