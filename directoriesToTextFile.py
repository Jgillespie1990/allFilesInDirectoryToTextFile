import os

with open("D:\\testArea\AllTheFiles.txt", "w") as a:
    for path, subdirs, files in os.walk( raw_input('Type in the directory    ')):
       for filename in files:
         f = os.path.join(path, filename)
         a.write(str(f) + os.linesep)