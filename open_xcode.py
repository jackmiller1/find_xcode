import os
from subprocess import call
from blessings import Terminal
import fnmatch

term = Terminal()

xcodeFileExt = (".xcworkspace", ".xcodeproj")
xcodeFiles = []

for root, dirs, files in os.walk("./"):
    for dirName in dirs:
        if dirName.endswith(xcodeFileExt):
            xcodeFiles.append(os.path.abspath(os.path.join(root, dirName)))

if len(xcodeFiles) == 0:
    print "{t.red}{t.bold}ERROR: No xcode workspace or project found!{t.normal}".format(t=term)
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
            print "{t.green}{t.bold}Opening {fileName}!{t.normal}".format(t=term, fileName=xcodeFiles[fi])
            os.system("open '" + str(xcodeFiles[fi]) + "'")
            shouldQuestion = False
        else:
            print "{t.red}{t.bold}ERROR: Not a valid number!{t.normal}".format(t=term)
