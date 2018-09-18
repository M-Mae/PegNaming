import maya.cmds as cmds
import os


#check on load if there is a directory. If so use it, if not, make a blank one.
homePath = os.path.expanduser('~')
directory = os.path.join(homePath, 'maya/2018/scripts/', 'directoryFile.txt')
description = os.path.join(homePath, 'maya/2018/scripts/', 'DescriptionList.txt')
states = os.path.join(homePath, 'maya/2018/scripts/', 'StateList.txt')

#find if there is/ is not a directory on initialization
if os.path.isfile(directory):
    print("directory was available for use")
    print(directory)
else:
    fileLocations = []
    with open(os.path.join(homePath, 'maya/2018/scripts/', 'directoryFile.txt'), 'w') as filehandle:
        for listitem in fileLocations:
            filehandle.write('%s\n' % listitem)
    print("there was no directory, so we made one.")

#find if there is/ is not a Description list on initialization
if os.path.isfile(description):
    print("Description List was available for use")
    print(description)
else:
    descriptions = []
    with open(os.path.join(homePath, 'maya/2018/scripts/', 'DescriptionList.txt'), 'w') as filehandle:
        for listitem in descriptions:
            filehandle.write('%s\n' % listitem)
    print("there was no Description list, so we made one.")

#find if there is/ is not a state list on initialization
if os.path.isfile(states):
    print("States List was available for use")
    print(states)
else:
    stateList = []
    with open(os.path.join(homePath, 'maya/2018/scripts/', 'StateList.txt'), 'w') as filehandle:
        for listitem in descriptions:
            filehandle.write('%s\n' % listitem)
    print("there was no State list, so we made one.")

#fetch the current state of the file.
def getFile(fileName):
    if fileName is "Directory":
        homePath = os.path.expanduser('~')
        currentDirectory = []
        with open(os.path.join(homePath, 'maya/2018/scripts/', 'directoryFile.txt'), 'r') as filehandle:
            for line in filehandle:
                # remove linebreaks as last character in string
                currentPlace = line[:-1]
                currentDirectory.append(currentPlace)
        return currentDirectory
    elif fileName is "DescriptionList":
        homePath = os.path.expanduser('~')
        currentDescList = []
        with open(os.path.join(homePath, 'maya/2018/scripts/', 'DescriptionList.txt'), 'r') as filehandle:
            for line in filehandle:
                # remove linebreaks as last character in string
                currentPlace = line[:-1]
                currentDescList.append(currentPlace)
        return currentDescList
    elif fileName is "StateList":
        homePath = os.path.expanduser('~')
        currentStateList = []
        with open(os.path.join(homePath, 'maya/2018/scripts/', 'StateList.txt'), 'r') as filehandle:
            for line in filehandle:
                # remove linebreaks as last character in string
                currentPlace = line[:-1]
                currentStateList.append(currentPlace)
        return currentStateList

#refactored into function above as getFile()
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

#overwrite the old file with a new one
def writeFile(currentList, type):
    #rewrite the file using most recent stuff
    if type is "Directory":
        with open(os.path.join(homePath, 'maya/2018/scripts/', 'directoryFile.txt'), 'w') as filehandle:
            for listitem in currentList:
                filehandle.write('%s\n' % listitem)
    elif type is "DescList":
        with open(os.path.join(homePath, 'maya/2018/scripts/', 'DescriptionList.txt'), 'w') as filehandle:
            for listitem in currentList:
                filehandle.write('%s\n' % listitem)
    elif type is "StateList":
        with open(os.path.join(homePath, 'maya/2018/scripts/', 'StateList.txt'), 'w') as filehandle:
            for listitem in currentList:
                filehandle.write('%s\n' % listitem)

#refactored into new function above writeFile()
#overwrite the old directory with a new one
def writeDirectory(currentDirectory):
    #rewrite the directory file using the most recent stuff
    with open(os.path.join(homePath, 'maya/2018/scripts/', 'directoryFile.txt'), 'w') as filehandle:
        for listitem in currentDirectory:
            filehandle.write('%s\n' % listitem)

#add to current list
def addToList(currentList, newListItem=None, type=None):
    if type is "Directory":
        if newListItem in currentList:
            print(str(newListItem) + " already logged in Directory List")
        elif newListItem not in currentList:
            currentList.append(newListItem)
            print("added " + str(newListItem))
            writeFile(currentList, "Directory")
    elif type is "StateList":
        if newListItem in currentList:
            print(str(newListItem) + " already logged in State List")
        elif newListItem not in currentList:
            currentList.append(newListItem)
            print("added " + str(newListItem))
            writeFile(currentList, "StateList")
    elif type is "DescList":
        if newListItem in currentList:
            print(str(newListItem) + " already logged in Description List")
        elif newListItem not in currentList:
            currentList.append(newListItem)
            print("added " + str(newListItem))
            writeFile(currentList, "DescList")

#refactored into new function above
#add to the current directory
def addToDirectory(currentDirectory=getDirectory(), newLocation=None):
    #new location must be trimmed before entering here so it can be added directly.
    if newLocation in currentDirectory:
        print(str(newLocation)+" already logged")
    elif newLocation not in currentDirectory:
        currentDirectory.append(newLocation)
        print("added " + str(newLocation))
        writeDirectory(currentDirectory)


#subtract from current list
def subFromList(currentList, newListItem=None, type=None):
    if type is "Directory":
        if newListItem not in currentList:
            print(str(newListItem) + " not in Directory list")
        elif newListItem in currentList:
            currentList.remove(newListItem)
            print("took out " + str(newListItem) + " from directory")
            writeFile(currentList, "Directory")
    elif type is "DescList":
        if newListItem not in currentList:
            print(str(newListItem) + " not in Description list")
        elif newListItem in currentList:
            currentList.remove(newListItem)
            print("took out " + str(newListItem) + " from Description List")
            writeFile(currentList, "DescList")
    elif type is "StateList":
        if newListItem not in currentList:
            print(str(newListItem) + " not in State list")
        elif newListItem in currentList:
            currentList.remove(newListItem)
            print("took out " + str(newListItem) + " from State List")
            writeFile(currentList, "StateList")

#refactored into the funtion SubFromList() Above
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
    #print("we made it in!")
    currentDirectory = getDirectory()
    #print(currentLocation)
    #print(currentSceneName)
    currentLocation = currentLocation.rstrip(currentSceneName)
    #trim off final / from current location
    currentLocation = currentLocation[:-1]

    if currentLocation in currentDirectory:
        #print("it was good")
        return True
    elif currentLocation not in currentDirectory:
        #print("bad location")
        return False



