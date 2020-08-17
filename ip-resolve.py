import sys
import os
import socket
os.system("clear")
os.system("figlet -f mono9  Ip Resolver") 
print
print 'Author  :  Rahat Khan Tusar(RKT)'
print
print 'Github  : https://github.com/r3k4t'
print
hostname = raw_input("Enter Domain Name :")
print
print socket.gethostbyname(hostname)
print


