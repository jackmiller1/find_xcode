import os
from subprocess import call

formatting = {
    'reset':    '\033[0m',
    'red': '\033[31m',
    'green': '\033[32m',
    'bold': '\033[1m'
}

xcodeFileExt = (".xcworkspace", ".xcodeproj")
xcodeFiles = []

for root, dirs, files in os.walk("./"):
    for dirName in dirs:
        if dirName.endswith(xcodeFileExt):
            xcodeFiles.append(os.path.abspath(os.path.join(root, dirName)))

if len(xcodeFiles) == 0:
    print formatting['red'] + formatting['bold'] + "ERROR: No xcode workspace or project found!" + formatting['reset']
elif len(xcodeFiles) == 1:
    os.system("open '" + str(xcodeFiles[0][1]) + "'")
else:
    print "Enter the number for the file you would like to open"
    for i, f in enumerate(xcodeFiles):
        print str(i) + "\t" + str(os.path.relpath(f))
    shouldQuestion = True
    while (shouldQuestion):
        fi = int(input("file: "))
        if fi < len(xcodeFiles):
            print formatting['green'] + formatting['bold'] + "Opening {fileName}!".format(fileName=xcodeFiles[fi]) + formatting['reset']
            os.system("open '" + str(xcodeFiles[fi]) + "'")
            shouldQuestion = False
        else:
            print formatting['red'] + formatting['bold'] + "ERROR: Not a valid number!" + formatting['reset']
