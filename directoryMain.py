# -*- coding: utf-8 -*-
#custom path for now
import sys
sys.path.append('C:/Users/MAE/Documents/MayaPython/QtFiles/InterruptSaveWidget')
#all Qt and maya stuff
from PySide2 import QtCore, QtWidgets, QtGui
import maya.cmds as cmds
from maya.app.general.mayaMixin import MayaQWidgetDockableMixin
#import our widgets to run
from directoryWidget import directoryWidget as dirWidget
from directoryHelpWidget import directoryHelpWidget as dirHelpWidget



def deleteControl(control):
    if cmds.workspaceControl(control, q=True, exists=True):
        cmds.workspaceControl(control,e=True, close=True)
        cmds.deleteUI(control,control=True)

class dockableDirWidget(MayaQWidgetDockableMixin, QtWidgets.QDialog):
    def __init__(self, parent=None):
        super(dockableDirWidget, self).__init__(parent=parent)
        #set the name and title of the widget
        self.setObjectName('dockableDirWidget')
        self.setWindowTitle('Location, location, location...')
        self.setLayout(self.createLayout())

    #create a interrupt widget and lay it out vertically
    def createLayout(self):
        self.main_layout = QtWidgets.QVBoxLayout()
        self.central_widget = dirWidget(parent=self)
        self.main_layout.addWidget(self.central_widget)
        return self.main_layout

class dockableDirHelpWidget(MayaQWidgetDockableMixin, QtWidgets.QDialog):
    def __init__(self, parent=None):
        super(dockableDirHelpWidget, self).__init__(parent=parent)
        #set the name and title of the widget
        self.setObjectName('dockableDirHelpWidget')
        self.setWindowTitle('HELP!')
        self.setLayout(self.createLayout())

    #create a interrupt widget and lay it out vertically
    def createLayout(self):
        self.main_layout = QtWidgets.QVBoxLayout()
        self.central_widget = dirHelpWidget(parent=self)
        self.main_layout.addWidget(self.central_widget)
        return self.main_layout

def makeDirectoryWidgetMain():
    #delete any pre-existing widget before making a new one
    #deleteControl("DirectoryControl")
    directory = dockableDirWidget()

    #configure and show the new widget
    directory.show()
    #for some reason, this line makes a new empty window instead of renaming the window I want.
    #cmds.workspaceControl("interruptSaveFrontControl")

    #bring to the front
    directory.raise_()


def makeDirectoryHelpWidgetMain():
    #delete any pre-existing widget before making a new one
    #deleteControl("DirectoryControl")
    directoryHelp = dockableDirHelpWidget()

    #configure and show the new widget
    directoryHelp.show()
    #for some reason, this line makes a new empty window instead of renaming the window I want.
    #cmds.workspaceControl("interruptSaveFrontControl")

    #bring to the front
    directoryHelp.raise_()

