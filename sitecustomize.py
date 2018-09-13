import sys
import os


#set module folder to be added to the list of places to look for scripts.
homePath = os.path.expanduser('~');
print (homePath);
moduleLocation = os.path.join(homePath, 'maya/2018/scripts/FileNameValidator');

#quick fix for this right now
#sys.path.append("D:/StudentData/Documents/maya/2018/scripts/FileNameValidator")
#this doesn't work because of the inheirent space between Student and Data from the homepath that Windows is supplying.
#sys.path.append(str(moduleLocation));

