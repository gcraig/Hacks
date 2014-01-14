import os, sys
from datetime import date, timedelta, datetime
from time import localtime
import re
 
files = os.listdir('.')
 
files = [ f for f in files if re.search('.dll$', f, re.I)]
 
files.sort()
 
d = datetime.now() - timedelta(days=30)
d = d.timetuple()
 
oldfiles = 0
newfiles = 0
for file in files:
    filetimesecs = os.path.getmtime('./' + file)
    filetime = localtime(filetimesecs)
 
#       print "*******************************"
#       print file
#       print filetime
#       print "*******************************"
 
if filetime < d:
    oldfiles += 1
    print file
    print filetime

if filetime > d:
    newfiles += 1
 
print "Old Files: %s" % oldfiles
print "New Files: %s" % newfiles