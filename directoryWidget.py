# -*- coding: utf-8 -*-
import sys
sys.path.append('C:/Users/MAE/Documents/MayaPython/QtFiles/InterruptSaveWidget')
from PySide2 import QtCore, QtGui, QtWidgets
import changedirectorylist as cDL
import maya.cmds as cmds
import directoryMain as DM
import checkFileLocation as CFL

class directoryWidget(QtWidgets.QWidget):
    def __init__(self, parent = None):
        #call the widget constructor
        super(directoryWidget, self).__init__(parent=parent)

        #create widget object from ui file
        self.ui = cDL.Ui_Form()
        self.ui.setupUi(self)

        #currentDirectory = CFL.getDirectory()
        currentDirectory = CFL.getFile("Directory")
        self.ui.directoriesTextBrowser.setText('\n'.join(str(result) for result in currentDirectory))

        #making slot for add button
        @QtCore.Slot(name='clickedAdd')
        def clickedAdd ():
            #add current thing to the directory list
            newPath = self.ui.lineEdit.text()
            newPath = cleanPath(newPath)
            print(newPath)
            currentDirectory = CFL.getFile("Directory")
            CFL.addToList(currentDirectory,newListItem=newPath,type="Directory")
            currentDirectory = CFL.getFile("Directory")
            self.ui.directoriesTextBrowser.setText('\n'.join(str(result) for result in currentDirectory))

        # making slot for delete button
        @QtCore.Slot(name='clickedDelete')
        def clickedDelete():
            # add current thing to the directory list
            newPath = self.ui.lineEdit.text()
            newPath = cleanPath(newPath)
            print(newPath)
            currentDirectory = CFL.getFile("Directory")
            CFL.subFromList( currentDirectory ,newListItem=newPath,type="Directory")
            currentDirectory = CFL.getFile("Directory")
            self.ui.directoriesTextBrowser.setText('\n'.join(str(result) for result in currentDirectory))
        #making slot for help button
        @QtCore.Slot(name='clickedHelp')
        def clickedHelp():
            # add current thing to the directory list
            newPath = self.ui.lineEdit.text()
            print(newPath)
            DM.makeDirectoryHelpWidgetMain()

        def cleanPath(path):
            #need to clean up all paths
            #TO DO make this cleanup more robust making sure they can't pass in things that are not file paths!
            newPath = str(path).replace('\\', '/')
            print(newPath+ " Clean!")
            return newPath

        #connecting slots
        self.ui.addButton.clicked.connect(clickedAdd)
        self.ui.deleteButton.clicked.connect(clickedDelete)
        self.ui.helpButton.clicked.connect(clickedHelp)


