# Import the os module, for the os.walk function
import os
 
# Set the directory you want to start from
rootDir = os.path.join(os.getenv('APPDATA'), 'Mozilla', 'Firefox', 'Profiles')
prefsFilePaths = []
for dirPath, subdirList, fileList in os.walk(rootDir):
    #print('Found directory: %s' % dirName)
    for fname in fileList:
        if fname == 'prefs.js':
            prefsFilePaths.append(os.path.join(dirPath, fname))
print prefsFilePaths