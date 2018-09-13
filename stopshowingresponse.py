# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:/Users/MAE/Documents/MayaPython/QtFiles/InterruptSaveWidget/stopshowingresponse.ui'
#
# Created: Fri Aug 17 13:25:21 2018
#      by: pyside2-uic  running on PySide2 2.0.0~alpha0
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(336, 202)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(Form)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(Form)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setWordWrap(True)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.userUnderstands = QtWidgets.QCheckBox(Form)
        self.userUnderstands.setObjectName("userUnderstands")
        self.horizontalLayout_2.addWidget(self.userUnderstands)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.okayButton = QtWidgets.QPushButton(Form)
        self.okayButton.setObjectName("okayButton")
        self.horizontalLayout.addWidget(self.okayButton)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        self.cancelButton = QtWidgets.QPushButton(Form)
        self.cancelButton.setObjectName("cancelButton")
        self.horizontalLayout.addWidget(self.cancelButton)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem4)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_3.addLayout(self.verticalLayout)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtWidgets.QApplication.translate("Form", "Stop popping up on me!", None, -1))
        self.label.setText(QtWidgets.QApplication.translate("Form", "Alright! I won\'t pop up anymore until the next time you open maya. If your file names have issues, they will show up in the little bar at the bottom of maya, and it will still stop you from saving, so please be careful! ", None, -1))
        self.userUnderstands.setText(QtWidgets.QApplication.translate("Form", "I understand", None, -1))
        self.okayButton.setText(QtWidgets.QApplication.translate("Form", "Okay", None, -1))
        self.cancelButton.setText(QtWidgets.QApplication.translate("Form", " Wait no! I want the popup! ", None, -1))

