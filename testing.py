
# import OS module
import os
 
# Get the list of all files and directories
path = os.getcwd() + r'/assets\Lively_NPCs_v3.0\individual sprites\medieval\adventurer_02'
dir_list = os.listdir(path)
 
print("Files and directories in '", path, "' :")
 
# prints all files
print(dir_list)

print(len(dir_list))