# simple login/register script for keyauth.cc

import binascii 
import hashlib
import json as jsond  
import os
import platform  
import subprocess  
import sys
import time 
from datetime import datetime
from time import sleep
from uuid import uuid4  
import keyauth
from keyauth import *
import hashlib
from hashlib import *
getchecksum = lambda: hashlib.sha256(open(sys.argv[0], 'rb').read()).hexdigest()
keyauthapp = api(
    name = "your name",
    ownerid = "your owner id",
    secret = "your secret",
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
    elif option == '3':
        exit()


def reg():
    os.system("cls")
    print("Welcome")
    username = input("Username: ")
    password = input("Password: ")
    license = input("License: ")
    hwid = subprocess.check_output('wmic csproduct get uuid').decode().split('\n')[1].strip()
    register = keyauthapp.register(username, password,  license, hwid)
    if register['status'] == 200:
        print("Registered successfully!")
        input()
        main()
        
    else:
        print(register['message'])
        input()
        main()
        
def login():
    os.system('cls')
    print("Welcome")
    username = input("Username: ")
    password = input("Password: ")
    hwid = subprocess.check_output('wmic csproduct get uuid').decode().split('\n')[1].strip()
    login = keyauthapp.login(username, password, hwid)
    if login['status'] == 200:
        print("Logged in successfully!")
        input()
        
    else:
        print(login['message'])
        input()
        



main()
