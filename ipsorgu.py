import requests
import json
from time import sleep
from os import system, chdir
from colorama import Fore
import keyboard

sil = lambda: system("cls")
dark = Fore.LIGHTBLACK_EX
red = Fore.RED
system("title Ip Lookup by @zupppe")
sil()

def ipsorgu():
    soru = input(red + "Hedef Ip Adresini Giriniz: {}".format(dark))
    sil()

    sonuc = requests.get("https://ipinfo.io/widget/demo/{}".format(soru))
    sonuc2 = json.loads(sonuc.text)

    if sonuc.status_code == 200:
        print(red + "İp Adresi:", dark +  sonuc2["data"]["ip"])
        print(red + "Ülke:", dark + sonuc2["data"]["country"])      
        print(red + "Şehir:", dark  + sonuc2["data"]["city"])
        print(red + "Posta Kodu:", dark + sonuc2["data"]["postal"])
        print(red + "Yakın Konum:", dark + sonuc2["data"]["loc"])
        print(red + "Hizmet:", dark + sonuc2["data"]["asn"]["name"])
        print(red + "Hizmet Domaini:", dark + sonuc2["data"]["asn"]["domain"])
        if sonuc2["data"]["privacy"]["vpn"] == False:
            print("{}Vpn: {}Kapalı".format(red, dark))
        else:
            print("{}Vpn: {}Açık".format(red, dark))
        if sonuc2["data"]["privacy"]["proxy"] == False:
            print("{}Proxy: {}Kapalı".format(red, dark))
        else:
            print("{}Proxy: {}Açık".format(red, dark))
        if sonuc2["data"]["privacy"]["tor"] == False:
            print("{}Tor Tarayıcı: {}Kapalı".format(red, dark))
        else:

            print("{}Tor Tarayıcı: {}Açık".format(red, dark))
        print("""
              
                    {}Anamenüye dönmek için {}-{}, Yeni sorgu için {}+ {}tuşuna basınız..{}
              """.format(red, dark, red, dark, red, dark))
    while True:
        if keyboard.is_pressed('+'):
            sil()
            ipsorgu()
            keyboard.wait('+')
        elif keyboard.is_pressed('-'):
            sil()
            chdir("..")
            chdir("..")
            system("python multitool.py")
            keyboard.wait('-')
    else:
        print(red + "Hatalı ip adresi..")
        sleep(3)
        sil()
        ipsorgu()
ipsorgu()
