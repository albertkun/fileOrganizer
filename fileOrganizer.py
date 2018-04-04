import shutil
import os
source = os.listdir("./")

fileTypes = []


for root, dirs, files in os.walk("."):
    for filename in files:
        theType = filename.split(".")[-1]
        if theType not in fileTypes:
            fileTypes.append(theType)
print fileTypes

for fileType in fileTypes:
    destination = "./"+fileType+"/"
    def create_path(path):
        if not os.path.isdir(path):
            os.mkdir(path)

    create_path(fileType)

    for files in source:
        if files.endswith("."+fileType):
            if files == 'fileOrganizer.py':
                print "found file organizer"
            else:
                shutil.move(files,destination)
