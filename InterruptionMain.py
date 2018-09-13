# -*- coding: utf-8 -*-
#custom path for now
import sys
sys.path.append('C:/Users/MAE/Documents/MayaPython/QtFiles/InterruptSaveWidget')
#all Qt and maya stuff
from PySide2 import QtCore, QtWidgets, QtGui
import maya.cmds as cmds
from maya.app.general.mayaMixin import MayaQWidgetDockableMixin
#import our widget to run
from InterruptSaveWidget import interruptWidget as intWidget
from TestInterruptWidget import testIntWidget as testWidget
from PopUpInterruptWidget import PopIntWidget as PopWidget

def deleteControl(control):
    if cmds.workspaceControl(control, q=True, exists=True):
        cmds.workspaceControl(control,e=True, close=True)
        cmds.deleteUI(control,control=True)

class dockableIntWidget(MayaQWidgetDockableMixin, QtWidgets.QDialog):
    def __init__(self, parent=None, desiredName=None):
        super(dockableIntWidget, self).__init__(parent=parent)
        #set the name and title of the widget
        self.setObjectName('dockableIntWidget')
        self.setWindowTitle('Sorry to Interrupt...')
        self.setLayout(self.createLayout(desiredName))

    #create a interrupt widget and lay it out vertically
    def createLayout(self, desiredName=None):
        self.main_layout = QtWidgets.QVBoxLayout()
        self.central_widget = intWidget(parent=self, currentName=desiredName)
        self.main_layout.addWidget(self.central_widget)
        return self.main_layout

class dockableTestWidget(MayaQWidgetDockableMixin, QtWidgets.QDialog):
    def __init__(self, parent=None, desiredName=None):
        super(dockableTestWidget, self).__init__(parent=parent)
        #set the name and title of the widget
        self.setObjectName('dockableTestWidget')
        self.setWindowTitle('Oh! It is a test!')
        self.setLayout(self.createLayout(desiredName))

    #create a interrupt widget and lay it out vertically
    def createLayout(self, desiredName=None):
        self.main_layout = QtWidgets.QVBoxLayout()
        self.central_widget = testWidget(parent=self, currentName=desiredName)
        self.main_layout.addWidget(self.central_widget)
        return self.main_layout

class dockablePopWidget(MayaQWidgetDockableMixin, QtWidgets.QDialog):
    def __init__(self, parent=None, desiredName=None):
        super(dockablePopWidget, self).__init__(parent=parent)
        #set the name and title of the widget
        self.setObjectName('dockablePopWidget')
        self.setWindowTitle('Careful now...')
        self.setLayout(self.createLayout(desiredName))

    #create a interrupt widget and lay it out vertically
    def createLayout(self, desiredName=None):
        self.main_layout = QtWidgets.QVBoxLayout()
        self.central_widget = PopWidget(parent=self, currentName=desiredName)
        self.main_layout.addWidget(self.central_widget)
        return self.main_layout

def makeInterruptSaveWidgetMain(desiredName):
    #delete any pre-existing widget before making a new one
    deleteControl("interruptSaveFrontControl")
    interrupt = dockableIntWidget(desiredName=desiredName)

    #configure and show the new widget
    interrupt.show()
    #for some reason, this line makes a new empty window instead of renaming the window I want.
    #cmds.workspaceControl("interruptSaveFrontControl")

    #bring to the front
    interrupt.raise_()

def makeTestInterruptWidget(desiredName):
    #delete any pre-existing widget before making a new one
    deleteControl("interruptSaveFrontControl")
    testInt = dockableTestWidget(desiredName=desiredName)

    #configure and show the new widget
    testInt.show()
    #for some reason, this line makes a new empty window instead of renaming the window I want.
    #cmds.workspaceControl("interruptSaveFrontControl")

    #bring to the front
    testInt.raise_()

def makePopInterruptWidget(desiredName):
    #delete any pre-existing widget before making a new one
    deleteControl("interruptSaveFrontControl")
    PopInt = dockablePopWidget(desiredName=desiredName)

    #configure and show the new widget
    PopInt.show()
    #for some reason, this line makes a new empty window instead of renaming the window I want.
    #cmds.workspaceControl("interruptSaveFrontControl")

    #bring to the front
    PopInt.raise_()
