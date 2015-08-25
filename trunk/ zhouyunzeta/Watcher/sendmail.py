#!/usr/bin/python
#sendmail.py

#A simple application of mimemail.py

import os, sys, getpass
recep = sys.argv[1]
msg = sys.argv[2]
appd = sys.argv[3]
usr_name = raw_input("smtp user name: ")
pwd = getpass.getpass("smtp passwd: ")