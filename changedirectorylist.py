# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:/Users/MAE/Documents/MayaPython/QtFiles/InterruptSaveWidget/changedirectorylist.ui'
#
# Created: Sun Aug 19 13:58:21 2018
#      by: pyside2-uic  running on PySide2 2.0.0~alpha0
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(406, 403)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(Form)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setWordWrap(True)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.directoriesTextBrowser = QtWidgets.QTextBrowser(Form)
        self.directoriesTextBrowser.setObjectName("directoriesTextBrowser")
        self.verticalLayout.addWidget(self.directoriesTextBrowser)
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout.addWidget(self.lineEdit)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.addButton = QtWidgets.QPushButton(Form)
        self.addButton.setObjectName("addButton")
        self.horizontalLayout.addWidget(self.addButton)
        self.helpButton = QtWidgets.QPushButton(Form)
        self.helpButton.setObjectName("helpButton")
        self.horizontalLayout.addWidget(self.helpButton)
        self.deleteButton = QtWidgets.QPushButton(Form)
        self.deleteButton.setObjectName("deleteButton")
        self.horizontalLayout.addWidget(self.deleteButton)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtWidgets.QApplication.translate("Form", "Form", None, -1))
        self.label.setText(QtWidgets.QApplication.translate("Form", "Here\'s the list of places that you\'re okay with having controlled file names! Add or subtract from this list as you please, come back and edit at anytime! NOTE: These locations should NEVER have spaces in them!", None, -1))
        self.lineEdit.setPlaceholderText(QtWidgets.QApplication.translate("Form", "Hey! add a file path here! ", None, -1))
        self.addButton.setText(QtWidgets.QApplication.translate("Form", "Add Path!", None, -1))
        self.helpButton.setText(QtWidgets.QApplication.translate("Form", "HELP!", None, -1))
        self.deleteButton.setText(QtWidgets.QApplication.translate("Form", "Delete Path!", None, -1))

