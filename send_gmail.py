#!/usr/bin/python

import smtplib

FROM    = "georgeacraig@gmail.com"
TO      = "georgeacraig@gmail.com"
SUBJECT = "helloworld"
TEXT    = "Hello world."

message = """\
From: %s
To: %s
Subject: %s

%s
""" % (FROM, TO, SUBJECT, TEXT)
#", ".join(TO)

server = smtplib.SMTP('smtp.gmail.com',587) #port 465 or 587
server.ehlo()
server.starttls()
server.ehlo()
server.login('georgeacraig@gmail.com','xxx')
server.sendmail('georgeacraig@gmail.com','georgeacraig@gmail.com',message)
server.close()