# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'login.ui'
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QDialog, QDialogButtonBox,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QWidget)

class Ui_login_frm(object):
    def setupUi(self, login_frm):
        if not login_frm.objectName():
            login_frm.setObjectName(u"login_frm")
        login_frm.resize(400, 300)
        login_frm.setWindowTitle(u"Login")
        self.loginbtn = QPushButton(login_frm)
        self.loginbtn.setObjectName(u"loginbtn")
        self.loginbtn.setGeometry(QRect(100, 200, 75, 51))
        font = QFont()
        font.setStyleStrategy(QFont.PreferDefault)
        self.loginbtn.setFont(font)
        self.loginbtn.setMouseTracking(False)
        self.loginbtn.setTabletTracking(False)
        self.Register = QPushButton(login_frm)
        self.Register.setObjectName(u"Register")
        self.Register.setGeometry(QRect(230, 200, 75, 51))
#        self.testbutton = QDialogButtonBox(login_frm)
#        self.testbutton.setObjectName(u"testbutton")
#        self.testbutton.setGeometry(QRect(274, 200, 77, 61))
#        self.testbutton.setStandardButtons(QDialogButtonBox.Cancel)
        self.label = QLabel(login_frm)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(160, 30, 61, 16))
        self.label_2 = QLabel(login_frm)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(170, 110, 49, 16))
        self.lineEdit = QLineEdit(login_frm)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(82, 131, 241, 41))
        self.lineEdit.setEchoMode(QLineEdit.Password)
        self.lineEdit_2 = QLineEdit(login_frm)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(80, 60, 241, 41))
        self.lineEdit_2.setEchoMode(QLineEdit.Normal)
        QWidget.setTabOrder(self.lineEdit_2, self.lineEdit)
        QWidget.setTabOrder(self.lineEdit, self.loginbtn)
        QWidget.setTabOrder(self.loginbtn, self.Register)

        self.retranslateUi(login_frm)

        self.loginbtn.setDefault(True)
        self.Register.setDefault(True)


        QMetaObject.connectSlotsByName(login_frm)
    # setupUi

    def retranslateUi(self, login_frm):
        self.loginbtn.setText(QCoreApplication.translate("login_frm", u"Anmelden", None))
        self.Register.setText(QCoreApplication.translate("login_frm", u"Registrieren", None))
        self.label.setText(QCoreApplication.translate("login_frm", u"User-Name", None))
        self.label_2.setText(QCoreApplication.translate("login_frm", u"Passwort", None))
        pass
    # retranslateUi

