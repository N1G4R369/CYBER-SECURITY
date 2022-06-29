#!/usr/bin/env python 

import os
import py_compile

os.system ("apt-get install figlet")
os.system ("clear")
os.system ("figlet shifreleme  ")

print ("""
shiffreleme programina xos gelmisiz :
""")

tertib = input("programin pathini yazin :")
py_compile.compile(tertib)
