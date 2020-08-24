import os
from sys import argv

filenames = os.listdir(argv[1])
numLines = 0
for fname in filenames:
    try:
        with open("NeuralArt/static/css" + fname, "r") as f:
            content = f.readlines()
            numLines += len(content)
            print(fname, len(content))
    except:
        pass

print("Total:", numLines)


