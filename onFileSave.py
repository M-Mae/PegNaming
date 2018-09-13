import sys
sys.path.append('c:/Users/MAE/PycharmProjects/Capstone/');
import fileValidation as V;
from types import *
#import maya.cmds as cmds;
reload(V);

# initialize the hardcoded lists for testing
GoodNames = ["Charlie_Character_Modeling_v02",
             "Charlie_Character_Texturing_v04",
             "Charlie_Character_Rigging_v12",
             "Staff_Prop_Modeling_v01",
             "Staff_Prop_Texturing_v05",
             "Staff_Prop_Texturing_test",
             "Staff_Prop_Texturing_final"
             ];

BadNames = ["Charlie_Modeling_v02",
             "Charlie_Brown_Character_Texturing_",
             "Charlie_Ch_Rigging_v12",
             "Staff Prop Modeling_v01",
             "Staff_Prop_painted_v05",
             "staff__Prop_textured_v067",
             "test",
             "Staff_Prop_Texturing_Final04",
             "Staff_Prop_Texturing_Finalfinal"
             ];

# define the testing loop, using it to only call the important file and print the results.
def testLoop(fileNameList):
    #print (str(fileNameList));
    for fileName in fileNameList:
        #print(str(fileName));
        validateResult = V.validateFileName(fileName);
        #print("result of validation before none check is: " + str(type(validateResult)));
        if type(validateResult) is not NoneType:
            print("This name has one or more formatting errors, they are as follows: " + str(validateResult));
        if type(validateResult) is NoneType:
            print("These names passed all the rules!");
print("defined Test Loop");

