import requests
import colorama
from colorama import Fore
import os
import time

os.system("@echo off")
temizle = lambda: os.system("clear||cls")
baslat = lambda: os.system("py ipsorgu.py")

def check(): 
    r = requests.get("https://ipinfo.io/") 
    if r.status_code == 200: 
        print(Fore.GREEN + "\n[+] Sunucu Çevrimiçi!\n") 
    else:
        print(Fore.RED + "\n[!] Sunucu Çevrimdışı!\n") 
        exit() 

ip = input(Fore.BLUE + "Lütfen hedef ip giriniz: ") 

check()

ip_cikti = requests.get("https://ipinfo.io/widget/demo/{}".format(ip)).text
print(str(ip_cikti))

geri_don = input("{}Yeni Sorgu İçin {}+{}, Ana Menü İçin {}- {}Tuşlayınız {}+{}/{}-{}: {}".format(Fore.BLUE, Fore.GREEN, Fore.BLUE, Fore.RED, Fore.BLUE, Fore.GREEN, Fore.BLUE, Fore.RED, Fore.BLUE, Fore.RESET))
if geri_don == ("+"):
    temizle()
    baslat()
if geri_don == ("-"):
    temizle()
    os.chdir("..")
    os.system("py tools.py")
if geri_don != ("+","-"):
    temizle()
    print(Fore.LIGHTRED_EX + "Hata Tespit Edildi En Başa Yönlendiriliyorsunuz... @zupppe")
    time.sleep(3)
    baslat()
