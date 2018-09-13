# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:/Users/MAE/Documents/MayaPython/QtFiles/InterruptSaveWidget/interruptFront.ui'
#
# Created: Tue Jul 31 17:13:43 2018
#      by: pyside2-uic  running on PySide2 2.0.0~alpha0
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(353, 408)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(Form)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setWordWrap(True)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        spacerItem = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem1 = QtWidgets.QSpacerItem(30, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setWordWrap(True)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        spacerItem2 = QtWidgets.QSpacerItem(30, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.verticalLayout.addLayout(self.horizontalLayout)
        spacerItem3 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem3)
        self.resultsTextBrowser = QtWidgets.QTextBrowser(Form)
        self.resultsTextBrowser.setObjectName("resultsTextBrowser")
        self.verticalLayout.addWidget(self.resultsTextBrowser)
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout.addWidget(self.lineEdit)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.Testing = QtWidgets.QCheckBox(Form)
        self.Testing.setObjectName("Testing")
        self.horizontalLayout_2.addWidget(self.Testing)
        self.okayButton = QtWidgets.QPushButton(Form)
        self.okayButton.setObjectName("okayButton")
        self.horizontalLayout_2.addWidget(self.okayButton)
        self.DoNotShow = QtWidgets.QCheckBox(Form)
        self.DoNotShow.setObjectName("DoNotShow")
        self.horizontalLayout_2.addWidget(self.DoNotShow)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtWidgets.QApplication.translate("Form", "Oops!", None, -1))
        self.label.setText(QtWidgets.QApplication.translate("Form", "Whoops! Looks like the file name you entered doesn\'t follow the conventions required for this project!", None, -1))
        self.label_2.setText(QtWidgets.QApplication.translate("Form", "Here is a list of things that need to be fixed. Please change these and try again!", None, -1))
        self.lineEdit.setPlaceholderText(QtWidgets.QApplication.translate("Form", "PreviousFileName which you can edit here", None, -1))
        self.Testing.setText(QtWidgets.QApplication.translate("Form", "This was a test", None, -1))
        self.okayButton.setText(QtWidgets.QApplication.translate("Form", "Okay", None, -1))
        self.DoNotShow.setText(QtWidgets.QApplication.translate("Form", "Don\'t show me again", None, -1))

