import requests

def check(): 
    r = requests.get("https://ipinfo.io/") 
    if r.status_code == 200: 
        print("\n[+] Sunucu Çevrimiçi!\n") 
    else:
        print("\n[!] Sunucu Çevrimdışı!\n") 
        exit() 

ip = input("Lütfen hedef ip giriniz: ") 

check()

ip_cikti = requests.get("https://ipinfo.io/widget/demo/{}".format(ip)).text

print(ip_cikti)
