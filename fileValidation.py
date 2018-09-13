import re
from types import *
#Validating a file name
# must be a four part name
# with specific values in parts 2, 3, and 4

descList = [
    "character", "char", "characters", "chars",
    "prop", "set", "item", "environment", "envir", "other"
];

stateList = [
    "modeling", "texturing", "rigging", "ready",
    "animation", "anim", "rig", "other"
];

versionList = [
    "version", "v", "ver"

];

testList = [
    "test", "testing", "t"
];

#define the validation function
print("defined validation function");
def validateFileName(name):
    results = [];
    print(str(name));
    nameParts = name.split("_");
    print(str(nameParts));
    if len(nameParts) > 4:
        #print("was too many parts");
        results.append(
            "This name had too many pieces to it,"
            " please make names four parts like this: Name_Description_State_Version");
    elif len(nameParts) < 4:
        #print("had too few parts");
        results.append(
            "This name had too few pieces to it, "
            "please make names four parts like this: Name_Description_State_Version");

    partsCount = len(nameParts);
    i = 1;
    while i < partsCount:
        #print(str(i));
        # to do replace with string formatting
        # take Description[part 2] from the name and compare against the description list.
        if i is 1 and str(nameParts[1]).lower() not in descList:
            results.append("Part two of your name must be one of the following: " + str(descList));
        # take State from the name and compare against the state list.
        elif i is 2 and str(nameParts[2]).lower() not in stateList:
            results.append("Part three of your name must be one of the following: " + str(stateList));
        elif i is 3:
            #taking off the .ma at the end of the file name by splitting it and never using the second part
            version = str(nameParts[3]).split(".")
            match = re.search("([a-zA-Z]+)(\d*)", str(version[0]))
            if match:
                #match.group(1)  # the string part
                #print(str(match.group(1)).lower());
                if type(match.group(2)) is NoneType:
                    print("It was nothing");
                # trying to catch people saying finalfinal, a very common practice.
                if str(match.group(1)).lower() == "finalfinal":
                    results.append("Finalfinal is not an allowed declaration of a final version.");
                elif str(match.group(1)).lower() == "final" and match.group(2).__len__() > 0:
                    #print("final isn't supposed to have a number dummy");
                    results.append("Final versions are not allowed to include numbers, the final is the final.");
                elif str(match.group(1)).lower() == "final":
                    break;
                elif str(match.group(1)).lower() in versionList:
                    if len(match.group(2)) <=  1:
                        results.append("Version tags must have more than one number behind them. If the number is less"
                                       " than 10, start with a 0. Eg. Ver03")
                elif str(match.group(1)).lower() in testList:
                    break;
                elif str(match.group(1)).lower() not in versionList:
                    results.append(
                        "The version portion of the name must include one of the following: " + str(versionList));
                else:
                    results.append("The final part of the file name must be either some form of Test,"
                                   " final, or a version identifier");
                match.group(2)  # the number part
                print(str(match.group(2)));

        i = i + 1;


    if results.__len__() > 0:
        return results;
    else:
        return None;

