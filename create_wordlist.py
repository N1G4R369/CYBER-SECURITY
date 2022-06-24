#!usr/bin/env python
import os

from numpy import minimum
os.system ("apt-get install figlet")
os.system ("clear")
os.system ("figlet WORDLIST YARATMAQ")

print ("""
wordlist yaratmaq programina xos gelmisiz :
""")

minimum = input("minimim karakter sayi yazin :")
maximum  = input("maximum  karakter sayi yazin :")
herfler= input("istediyiniz herfleri yazin  :")

os.system("crunch "+ minimum + " "+ maximum)
print("ugurla tamamlandi")