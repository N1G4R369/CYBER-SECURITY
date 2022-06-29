#!/usr/bin/env/python
import os 

os.system("apt-get install figlet")
os.system("clear")
os.system("figlet mac address deyisme ")


print(""" 

mac address deyisme programina xos gelmisiniz :) 


1) mac addressin  random yaratmaq 
2)mac addresin manual teyin etmek
3)mac addressin orginala qaytarmaq 

""")

emr_no=input("emr nomresini yazin :")
if (emr_no=="1"):
	os.system("ifconfig eth0 down")
	os.system("macchanger -r eth0")
	os.system("ifconfig eth0 up")
	print("\033[92mYeni mac addresi teyin olundu ")
elif (emr_no=="2"):
	macaddress= input("yeni mac addresi yazin :" )
	os.system("ifconfig eth0 down")
	os.system("macchanger --mac "+macaddress + "eth0")
	os.system("ifconfig eth0 up")
	print("\033[92mYeni mac addresi teyin olundu ")
elif (emr_no=="3"):
	macaddress= input("yeni mac addresi yazin :" )
	os.system("ifconfig eth0 down")
	os.system("macchanger --mac "+macaddress + "eth0")
	os.system("ifconfig eth0 up")
	print("\033[92mYeni mac addresi orginal hala qaytarildi ")

else:
	print("\033[92mYanlis duyme secdiniz , program yeniden basladilir ") 

	os.system("python change_mac_address.py")
