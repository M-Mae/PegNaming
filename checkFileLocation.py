import maya.cmds as cmds
import os


#check on load if there is a directory. If so use it, if not, make a blank one.
homePath = os.path.expanduser('~')
directory = os.path.join(homePath, 'maya/2018/scripts/', 'directoryFile.txt')
if os.path.isfile(directory):
    print("directory was available for use")
else:
    fileLocations = []
    with open(os.path.join(homePath, 'maya/2018/scripts/', 'directoryFile.txt'), 'w') as filehandle:
        for listitem in fileLocations:
            filehandle.write('%s\n' % listitem)
    print("there was no directory, so we made one.")

#fetch the current state of the directory list
def getDirectory():
    homePath = os.path.expanduser('~')
    currentDirectory = []
    with open(os.path.join(homePath, 'maya/2018/scripts/', 'directoryFile.txt'), 'r') as filehandle:
        for line in filehandle:
            # remove linebreaks as last character in string
            currentPlace = line[:-1]
            currentDirectory.append(currentPlace)
    return currentDirectory

#overwrite the old directory with a new one
def writeDirectory(currentDirectory):
    #rewrite the directory file using the most recent stuff
    with open(os.path.join(homePath, 'maya/2018/scripts/', 'directoryFile.txt'), 'w') as filehandle:
        for listitem in currentDirectory:
            filehandle.write('%s\n' % listitem)

#add to the current directory
def addToDirectory(currentDirectory=getDirectory(), newLocation=None):
    #new location must be trimmed before entering here so it can be added directly.
    if newLocation in currentDirectory:
        print(str(newLocation)+" already logged")
    elif newLocation not in currentDirectory:
        currentDirectory.append(newLocation)
        print("added " + str(newLocation))
        writeDirectory(currentDirectory)


#substract from the current directory
def subFromDirectory(currentDirectory=getDirectory(), badLocation=None):
    #again, locations MUST be trimmed of scene name before entering this stage.
    if badLocation not in currentDirectory:
        print(str(badLocation)+ " not in list")
    elif badLocation in currentDirectory:
        currentDirectory.remove(badLocation)
        print("took out "+ str(badLocation))
        writeDirectory(currentDirectory)

#check that the location is in the list.
def checkSaveLocation(currentLocation=None, currentSceneName=None):
    print("we made it in!")
    currentDirectory = getDirectory()
    #print(currentLocation)
    #print(currentSceneName)
    currentLocation = currentLocation.rstrip(currentSceneName)
    #trim off final / from current location
    currentLocation = currentLocation[:-1]

    if currentLocation in currentDirectory:
        print("it was good")
        return True
    elif currentLocation not in currentDirectory:
        print("bad location")
        return False

def checking123():
    print("hi")

