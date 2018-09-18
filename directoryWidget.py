# -*- coding: utf-8 -*-
import sys
sys.path.append('C:/Users/MAE/Documents/MayaPython/QtFiles/InterruptSaveWidget')
from PySide2 import QtCore, QtGui, QtWidgets
import PEG_Settings as PEG
import maya.cmds as cmds
import directoryMain as DM
import checkFileLocation as CFL

class directoryWidget(QtWidgets.QWidget):
    def __init__(self, parent = None):
        #call the widget constructor
        super(directoryWidget, self).__init__(parent=parent)

        #create widget object from ui file
        self.ui = PEG.Ui_Form()
        self.ui.setupUi(self)

        #currentDirectory = CFL.getDirectory()
        currentDirectory = CFL.getFile("Directory")
        self.ui.directoriesTextBrowser.setText('\n'.join(str(result) for result in currentDirectory))

        currentDescList = CFL.getFile("DescriptionList")
        self.ui.DescTextBrowser.setText('\n'.join(str(result) for result in currentDescList))

        currentStateList = CFL.getFile("StateList")
        self.ui.StatesTextBrowser.setText('\n'.join(str(result) for result in currentStateList))

        #making slot for add button on directory
        @QtCore.Slot(name='clickedAddDirect')
        def clickedAddDirect ():
            #add current thing to the directory list
            newPath = self.ui.directoriesLineEdit.text()
            newPath = cleanPath(newPath)
            #print(newPath)
            currentDirectory = CFL.getFile("Directory")
            CFL.addToList(currentDirectory,newListItem=newPath,type="Directory")
            currentDirectory = CFL.getFile("Directory")
            self.ui.directoriesTextBrowser.setText('\n'.join(str(result) for result in currentDirectory))

        # making slot for delete button on directory
        @QtCore.Slot(name='clickedDeleteDirect')
        def clickedDeleteDirect():
            # add current thing to the directory list
            newPath = self.ui.directoriesLineEdit.text()
            newPath = cleanPath(newPath)
            #print(newPath)
            currentDirectory = CFL.getFile("Directory")
            CFL.subFromList( currentDirectory ,newListItem=newPath,type="Directory")
            currentDirectory = CFL.getFile("Directory")
            self.ui.directoriesTextBrowser.setText('\n'.join(str(result) for result in currentDirectory))

        @QtCore.Slot(name='clickedAddDesc')
        def clickedAddDesc():
            #add current thing to the desc list
            newItem = self.ui.DescLineEdit.text()
            #get current list
            currentDescList = CFL.getFile("DescriptionList")
            CFL.addToList(currentDescList,newListItem=newItem, type="DescList")
            currentDescList = CFL.getFile("DescriptionList")
            self.ui.DescTextBrowser.setText('\n'.join(str(result) for result in currentDescList))

        @QtCore.Slot(name='clickedDelDesc')
        def clickedDelDesc():
            # add current thing to the desc list
            newItem = self.ui.DescLineEdit.text()
            # get current list
            currentDescList = CFL.getFile("DescriptionList")
            CFL.subFromList(currentDescList, newListItem=newItem, type="DescList")
            currentDescList = CFL.getFile("DescriptionList")
            self.ui.DescTextBrowser.setText('\n'.join(str(result) for result in currentDescList))

        @QtCore.Slot(name='clickedAddState')
        def clickedAddState():
            # add current thing to the desc list
            newItem = self.ui.StatesLineEdit.text()
            # get current list
            currentStateList = CFL.getFile("StateList")
            CFL.addToList(currentStateList, newListItem=newItem, type="StateList")
            currentStateList = CFL.getFile("StateList")
            self.ui.StatesTextBrowser.setText('\n'.join(str(result) for result in currentStateList))

        @QtCore.Slot(name='clickedDelState')
        def clickedDelState():
            # add current thing to the desc list
            newItem = self.ui.StatesLineEdit.text()
            # get current list
            currentStateList = CFL.getFile("StateList")
            CFL.subFromList(currentStateList, newListItem=newItem, type="StateList")
            currentStateList = CFL.getFile("StateList")
            self.ui.StatesTextBrowser.setText('\n'.join(str(result) for result in currentStateList))

        #making slot for help button
        @QtCore.Slot(name='clickedHelp')
        def clickedHelp():
            # open help UI
            #newPath = self.ui.directoriesLineEdit.text()
            #print(newPath)
            DM.makeDirectoryHelpWidgetMain()

        def cleanPath(path):
            #need to clean up all paths
            #TO DO make this cleanup more robust making sure they can't pass in things that are not file paths!
            newPath = str(path).replace('\\', '/')
            #print(newPath+ " Clean!")
            return newPath

        #connecting slots
        self.ui.AddButtonDirect.clicked.connect(clickedAddDirect)
        self.ui.DelButtonDirect.clicked.connect(clickedDeleteDirect)
        self.ui.helpButton.clicked.connect(clickedHelp)
        self.ui.DescAddButton.clicked.connect(clickedAddDesc)
        self.ui.DescDelButton.clicked.connect(clickedDelDesc)
        self.ui.StatesAddButton.clicked.connect(clickedAddState)
        self.ui.StatesDelButton.clicked.connect(clickedDelState)


