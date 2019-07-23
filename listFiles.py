#!/usr/bin/python
import os
import fnmatch
stream = open("Songs.tex", "w")
for chapter in sorted(fnmatch.filter(os.listdir("songs"), "*.tex")):
    stream.write("\\input{songs/%s}\n" % chapter)
stream.close()