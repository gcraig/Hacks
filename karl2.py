#!/usr/bin/env python
# -*- coding: utf-8 -*-

import subprocess
#import zipfile
from zipfile import ZipFile, is_zipfile
import fileinput
import sys

print 'Karl is gettin'' paaaid!'

# changes > files.txt

files = []
num = 0

for line in fileinput.input():
    files.append(line.strip())

files = filter(None, files) # fastest

zfile = "latest.zip"
zout = ZipFile(zfile, "w")
for fname in files:
    num = num + 1
    zout.write(fname)
zout.close()

if is_zipfile(zfile):
    print "Success!\n%s created with %s files." % (zfile, num)
else:
    print "Error: %s is not a valid zip file." % zfile
