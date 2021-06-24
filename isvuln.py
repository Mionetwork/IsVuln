import requests
import threading
import time
import sys
import hashlib
import urllib.parse
import random
from colorama import init
from colorama import Fore, Back, Style
init()
import random
import os 
deger2 = 0
import re
proxiesc = open("isvuln.conf", encoding='utf8', errors = 'ignore').read()

filesd = input("List : ")
def combo():

        combos = open(str(filesd), encoding='utf8', errors = 'ignore').readlines()
        User = []
        Pass = []
        for y in combos:
            ez = y.replace("\n", "").split(":")
            try:
                User.append(y)
                Pass.append(y)
            except:
                pass
        return User,Pass




def find_between( s, first, last ):
    try:
        start = s.index( first ) + len( first )
        end = s.index( last, start )
        return s[start:end]
    except ValueError:
        return ""




def crack(koko,koko2):
    renkler = ["Green","Yellow","Blue","Red","White"]
    renk = random.choice(renkler)
    if renk == "Green":
        blobber = Fore.WHITE
    elif renk == "Yellow":
        blobber = Fore.WHITE
    elif renk == "Blue":
        blobber = Fore.WHITE
    elif renk == "Red":
        blobber = Fore.WHITE
    elif renk == "White":
        blobber = Fore.WHITE
    if 'PROXIES="YES"' in proxiesc:
        findprxy = re.findall('PROXY="(.*?)"',proxiesc)
        proxies = {
        'http':str(findprxy[0])
        }
    if 'PROXIES="NO"' in proxiesc:
        vulnsayf = requests.get(koko+'<script>alert("My First Test")</script>')
    if 'PROXIES="YES"' in proxiesc:
        vulnsayf = requests.get(koko+'<script>alert("My First Test")</script>',proxies=proxies)
    print("Website: "+koko)
    if '<script>alert("My First Test")</script>' in vulnsayf.text:
        print(blobber +" Vulnerability Founded (XSS)")
        xssave = open('xssvuln.txt', 'a')
        xssave.write(koko)
    else:
        print(blobber + " No XSS Vulnerability Founded")
    try:
        if 'PROXIES="NO"' in proxiesc:
            vulnsayf = requests.get(koko+"'", timeout=10)
        if 'PROXIES="YES"' in proxiesc:
            vulnsayf = requests.get(koko+"'",proxies=proxies)
            
        if 'Warning: mysql_fetch_array()' or 'You have an error in your SQL syntax;' in vulnsayf.text:
            print("Vulnerability Founded (SQL)")
            xssave = open('sqlvuln.txt', 'a')
            xssave.write(koko)
        else:
            print("No SQL Vulnerability Founded")
    except:
        print("An Error")
    print("------------------------------------------------")


def başlatıcı():
    num=int('0')
    User,Pass=combo()
    threadsnum = sys.argv[2]
    while 1:
        if threading.active_count() < int(threadsnum):
                if len(User) > num:
     #                   randomproxy = proxys3[random.randint(1,len(proxys3))]
     #                   proxsel = {
     #                       'http': 'http://'+randomproxy,
     #                       'https': 'https://'+randomproxy
     #                       }
                    threading.Thread(target=crack, args=(User[num], Pass[num])).start()
                    num += 1
                    #kalan -= 1
                else:
                    
                    exit()
                    time.sleep(0.6)
                    
        else:
            #print("Checking done!")
            time.sleep(0.3)
başlatıcı()
