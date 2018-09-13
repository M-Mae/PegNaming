# -*- coding: utf-8 -*-
import sys
sys.path.append('C:/Users/MAE/Documents/MayaPython/QtFiles/InterruptSaveWidget')
from PySide2 import QtCore, QtGui, QtWidgets
import directoryhelp as DH
import maya.cmds as cmds


class directoryHelpWidget(QtWidgets.QWidget):
    def __init__(self, parent = None):
        #call the widget constructor
        super(directoryHelpWidget, self).__init__(parent=parent)

        #create widget object from ui file
        self.ui = DH.Ui_Form()
        self.ui.setupUi(self)


        #making slot for add button
        @QtCore.Slot(name='clickedOkay')
        def clickedOkay ():
            #add current thing to the directory list
            self.parent().close()

        #connecting slots
        self.ui.pushButton.clicked.connect(clickedOkay)