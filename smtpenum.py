#!/usr/bin/python
import socket,sys

# script for smtp enumeration

if len(sys.argv) !=3:
    print "Usage: python smtpenum.py IP user"
    sys.exit(0)

tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcp.connect((sys.argv[1],25))

banner = tcp.recv(1024)
print banner

tcp.send("VRFY " + sys.argv[2] + "\r\n")
user = tcp.recv(1024)
print user
