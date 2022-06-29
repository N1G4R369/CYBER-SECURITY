#!/usr/bin/env/python
import os 
os.system("apt-get update")
os.system("apt-get install figlet")
os.system("clear")
os.system("figlet wordpress analiz")


print(""" 

1) suretli analiz
2)elave analiz
3)movzu analiz
4) istifadece adi analizi 
""")

emeliyat_no = input("emeliyat nomresi yazin ")

if(emeliyat_no=="1"):
	sayt = input("sayt addresi yazin ")
	os.system("wpscan --url " + sayt)

elif (emeliyat_no=="2"):
	sayt = input("sayt addresi yazin ")
	os.system("wpscan --url " + sayt + " -- enumerate p " )

elif (emeliyat_no=="3"):
	sayt = input("sayt addresi yazin ")
	os.system("wpscan --url " + sayt + " -- enumerate t " )

elif (emeliyat_no=="4"):
	sayt = input("sayt addresi yazin ")
	os.system("wpscan --url " + sayt + " -- enumerate u " )

else :
	print("xetali secim elediniz . program baglanir . . .")
