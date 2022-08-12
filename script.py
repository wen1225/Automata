# used for os-python interaction
import os
# used for matching specific file name patterns in a directory
import glob

filePath = '../../Downloads/'

# check if path is valid
if os.path.exists(filePath) is False:
    print('path dne!')
else:
    print('path exists')
    # list all files and folders in filePath
    list = os.listdir(filePath)
    for entries in list:
        print(entries)
    # show only .pdf files
    list = glob.glob(filePath + '*.heic')
    for entry in list:
        print(entry)

