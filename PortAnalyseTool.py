#!/usr/bin/env python

import os

os.system("apt -get install figlet")
os.system("clear")
os.system("figlet PORT_ANALIZ")

print ("""
PORT ANALIZ PROGRAMINA XOS GELDINIZ :) 
 
 1) SURETTLI ANALIZ
 2)SERVIS VE VERSIYA MELUMATI 
 3) EMELIYAT SISTEMI MELUMATI
 """)
EmrNomer = input("EMELIYAT NOMRESINI YAZIN ")

if (EmrNomer=="1"):
    HedefIp = input("HEDEFIN IP ADDRESIN YAZIN  :")
    os.system("nmap " +HedefIp)
elif(EmrNomer=="2"):
    HedefIp = input("HEDEFIN IP ADDRESIN YAZIN  :")
    os.system("nmap -sS -sV " +HedefIp)

elif(EmrNomer=="3"):
    HedefIp = input("HEDEFIN IP ADDRESIN YAZIN  :")
    os.system("nmap -0" +HedefIp)

else:
    print("SEHV EMR NOMRESI YAZDINIZ , YENIDEN YOXLAYIN")