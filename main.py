# key auth login

import binascii  # hex encoding
import hashlib
import json as jsond  # json
import os
import platform  # check platform
import subprocess  # needed for mac device
import sys
import time  # sleep before exit
from datetime import datetime
from time import sleep
from uuid import uuid4  # gen random guid
import keyauth
from keyauth import *
import hashlib
from hashlib import *
getchecksum = lambda: hashlib.sha256(open(sys.argv[0], 'rb').read()).hexdigest()
keyauthapp = api(
    name = "mercierr",
    ownerid = "Z3CpLM1OGC",
    secret = "f8c18d81795e34295c295599e1c78514ad16d3b40ec5d358e851b5752eb83939",
    version = "1.0",
    hash_to_check = getchecksum()
)

def main():
    print("""
    -----------------------
    1: Register
    2: Login
    3: Exit
    -----------------------
    """)
    option= input(">> ")
    if option == '1':
        reg()
    elif option == '2':
        login()

    
    



def reg():
    print("Welcome")
    username = input("Username: ")
    password = input("Password: ")
    license = input("License: ")
    hwid = subprocess.check_output('wmic csproduct get uuid').decode().split('\n')[1].strip()
    register = keyauthapp.register(username, password,  license, hwid)
    if register['success']:
        print("Registered successfully!")
        input()
        main()
    else:
        print(register['message'])
        input()
        main()



def login():
    print("Welcome")
    username = input("Username: ")
    password = input("Password: ")
    hwid = subprocess.check_output('wmic csproduct get uuid').decode().split('\n')[1].strip()
    login = keyauthapp.login(username, password, hwid)
    if login['success']:
        print("Welcome to keyauth login")
        input()
        main1()
    else:
        print(login['message'])
        input()
        main()














def main1():
    print("Logged in successfully!")
    input()

main()
