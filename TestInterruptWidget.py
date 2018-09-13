# -*- coding: utf-8 -*-
import sys
sys.path.append('C:/Users/MAE/Documents/MayaPython/QtFiles/InterruptSaveWidget')
from PySide2 import QtCore, QtGui, QtWidgets
import testbutnamestillwrong
from types import *
import fileValidation as FV
import maya.cmds as cmds


class testIntWidget(QtWidgets.QWidget):
    def __init__(self, parent = None, currentName=None):
        #call the widget constructor
        super(testIntWidget, self).__init__(parent=parent)

        #create widget object from ui file
        self.ui = testbutnamestillwrong.Ui_Form()
        self.ui.setupUi(self)

        #get the current scene file name and trim the file extension
        if currentName is NoneType:
            currentName = cmds.file(file, q=True, sn=True, shn=True);
        name = str(currentName).split(".")
        #set the text in the line edit to be that to start.
        self.ui.lineEdit.setText(str(name[0]))
        #set name to a temp name so the save can go through without harming anything


        #get list of results from the original check? or just check it again
        showResults = FV.validateFileName(currentName)
        self.ui.resultsTextBrowser.setText('\n\n'.join(str(result) for result in showResults))

        #making slot for button
        @QtCore.Slot(name='clickedOkay')
        def clickedOkay ():
            #they clicked okay so we should check the new name in the line edit
            #if the name was okay, rename the file and let it finish saving, close the window
            #if it was not, update the text field
            newName = self.ui.lineEdit.text()
            print (newName)

            validateResult = FV.validateFileName(newName);
            if type(validateResult) is not NoneType:
                #if it's not a test, doesn't matter
                # if things weren't right then we need to update the UI to tell the user that
                self.ui.resultsTextBrowser.clear()
                self.ui.resultsTextBrowser.setText('\n\n'.join(str(result) for result in validateResult))
                # here also we need to stop the save by retuning some sort of value I'd imagine.
                print("This name has one or more formatting errors, they are as follows: " + str(validateResult))

            if type(validateResult) is NoneType:
                print("This name passed all the rules!")
                cmds.file(rename=str(newName))
                cmds.file(save=True, f=True)
                self.parent().close()


        #connecting slots
        self.ui.okayButton.clicked.connect(clickedOkay)



