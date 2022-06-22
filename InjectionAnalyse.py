#!/usr/bin/env python
import os
os.system("apt-get install figlet ")
os.system("clear")
os.system("figlet SERVICE_ZEIFLIK_ANALIZI")
print(""" 

SERVISLERIN ZEIFLIYIN YOXLAYAN TOOLA XOS GELMIZINIZ :)

""")
hedef_ip = input(" HEDEFIN IP ADDRESIN YAZIN : ")

os.system("nikto -h " + hedef_ip)