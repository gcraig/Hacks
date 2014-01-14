#!/usr/bin/env python
# -*- coding: utf-8 -*-

import subprocess
import zipfile

print 'Karl is gettin'' paaaid!'

gitcmd = 'C:\\Program Files (x86)\\Git\\cmd\\git.cmd'
tarcmd = "C:\\Program Files (x86)\\Gow\\bin\\tar.exe"

proc = subprocess.Popen([gitcmd, 'status'], stdout=subprocess.PIPE)
files = []
num = 0
while True:
    line = proc.stdout.readline()
    if line != '':
        if 'modified:' in line:
            f = line.rstrip()[14:]
            files.append(f)
            print '\t' + f
            num += 1
    else:
        break

zfile = "latest.zip"
zout = zipfile.ZipFile(zfile, "w")
for fname in files:
    zout.write(fname)
zout.close()

if zipfile.is_zipfile(zfile):
    print "Success!\n%s created with %s files." % (zfile, num)
else:
    print "Error: %s is not a valid zip file." % zfile
