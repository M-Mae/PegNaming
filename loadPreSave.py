import maya.cmds as cmds
import maya.OpenMaya as om
from types import *
import fileValidation as FV
import sys
sys.path.append('C:/Users/MAE/Documents/MayaPython/QtFiles/InterruptSaveWidget')
import InterruptionMain as IM
import checkFileLocation as CFL
reload(CFL)
import directoryMain
import maya.cmds as cmds
#check local list of directories


#define global user wants
popWantBool = True;

#can now use file validation function in the before save callback.
def load(*args):
    def onSave(*args):
        dir = CFL.getDirectory()
        if len(dir)< 1:
            directoryMain.makeDirectoryWidgetMain()
        currentLocation = cmds.file(q=True, loc=True)
        currentSceneName = cmds.file(file, q=True, shn=True, sn=True)
        if CFL.checkSaveLocation(currentLocation, currentSceneName) is True:
            # print("hey, we're doing it!")
            # get the current name, trimming the file location data
            currentName = cmds.file(file, q=True, sn=True, shn=True);
            # make sure it's a string, and give it to the validation
            stringName = str(currentName);
            # ask it to validate the name
            validateResult = FV.validateFileName(stringName);
            if type(validateResult) is not NoneType:
                # if things weren't right then we need to open the UI to tell the user that
                cmds.file(rename='TEMP.ma')
                if popWantBool is False:
                    errorMessage = "This name has one or more formatting errors, they are as follows: " + str(validateResult)
                    om.MGlobal.displayError(errorMessage)
                    cmds.evalDeferred('om.MGlobal.displayError("This name has one or more formatting errors, check log! Click on semicolon to the right of this line.")');
                else:
                    IM.makeInterruptSaveWidgetMain(desiredName=stringName);
            if type(validateResult) is NoneType:
                print("This name passed all the rules!");
        if CFL.checkSaveLocation(currentLocation, currentSceneName) is False:
            print("We don't need to check file names in this location")
    #add onSave to the callback, this is session based too!
    om.MSceneMessage.addCallback(om.MSceneMessage.kBeforeSave,onSave);
#to do, decide how to deal with when their name is wrong, can we cancel the save?