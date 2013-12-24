import sys
import os


def getPrefsFilePaths():
    rootDir = os.path.join(os.getenv('APPDATA'), 'Mozilla', 'Firefox', 'Profiles')
    prefsFilePaths = []
    for dirPath, subdirList, fileList in os.walk(rootDir):
        for fname in fileList:
            if fname == 'prefs.js':
                prefsFilePaths.append(os.path.join(dirPath, fname))
    return prefsFilePaths


def updateBlockItCurrFile(setState, currFile, sitesString):
    try:
        with open(currFile, 'r+') as f:
            lines = f.readlines()
            f.seek(0)
            f.truncate()
            for line in lines:
                if 'jid1-blockit@jetpack.domains' in line:
                    tmpStr = line[:line.find(',')+2]
                    if setState == 'ON':
                        tmpStr += '"' + sitesString + '");'
                    else:
                        tmpStr += '"");'
                    f.write(tmpStr+"\n")
                else:
                    f.write(line)
            f.close()
    except IOError:
        if f:
            f.close()


def updateBlockIt(setState, sitesString=None):
    prefsFilePaths = getPrefsFilePaths()
    for currFile in prefsFilePaths:
        updateBlockItCurrFile(setState, currFile, sitesString)


def setBlockingOn():
    f_sites = open('sites.txt')
    sitesToBlock = []
    for line in f_sites.readlines():
        sitesToBlock.append(line.rstrip("\n"))
    f_sites.close()
    sitesString = '|'.join(x for x in sitesToBlock)
    updateBlockIt('ON', sitesString)


def setBlockingOff():
    updateBlockIt('OFF')


def main():
    setState = sys.argv[1]
    if setState.upper() == 'ON':
        setBlockingOn()
    else:
        setBlockingOff()

if __name__ == '__main__':
    if len(sys.argv) > 1:
        if sys.argv[1].upper() == 'ON' or sys.argv[1].upper() == 'OFF':
            main()