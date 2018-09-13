# -*- coding: utf-8 -*-
import sys
sys.path.append('C:/Users/MAE/Documents/MayaPython/QtFiles/InterruptSaveWidget')
from PySide2 import QtCore, QtGui, QtWidgets
import stopshowingresponse
from types import *
import loadPreSave as LPS
import fileValidation as FV
import maya.cmds as cmds


class PopIntWidget(QtWidgets.QWidget):
    def __init__(self, parent = None, currentName=None):
        #call the widget constructor
        super(PopIntWidget, self).__init__(parent=parent)

        #create widget object from ui file
        self.ui = stopshowingresponse.Ui_Form()
        self.ui.setupUi(self)


        #making slot for button
        @QtCore.Slot(name='clickedOkay')
        def clickedOkay ():
            #they clicked okay, check the understands box?
            if self.ui.userUnderstands.isChecked():
                LPS.popWantBool = False;
                self.parent().close()

        @QtCore.Slot(name='clickedCancel')
        def clickedCancel ():
            #they clicked cancel, exit window and reset bool to default
            LPS.popWantBool = True;
            self.parent().close()
        #connecting slots
        self.ui.okayButton.clicked.connect(clickedOkay)
        self.ui.cancelButton.clicked.connect(clickedCancel)



