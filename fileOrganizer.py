import shutil
import os

#define the folders to look through
folders = os.listdir("./")

#set an array for the file types
file_types = []

#create a list of file types
for root, dirs, files in os.walk("."):
    for filename in files:
        the_type = filename.split(".")[-1]
        if the_type not in file_types:
            file_types.append(the_type)
            
##OPTIONAL: print out the list of file types ##
print ('These are file types: \n {}').format(file_types)

for file_type in file_types:
    #define the function for making folders
    def create_path(path):
        if not os.path.isdir(path):
            os.mkdir(path)

    #use the function
    create_path(file_type)
    
    #make a variable for the target destinations
    destination = "./"+file_type+"/"
    
    #loop through each file in the folders
    for files in folders:
        if files.endswith("."+file_type):
            if files == 'fileOrganizer.py':
                print "Found file organizer so ignoring it."
            else:
                shutil.move(files,destination)
print "Script has completed"
