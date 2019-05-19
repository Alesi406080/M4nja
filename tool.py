#!/bin/usr/python

import os
import sys
import time
import request
import random
import mechanize

def banner():
	os.system('clear')
	print ("\033[1;31m       《□》---《□》---《□》---《□》---《□》 ")
	print ("\033[1;33m       |       KHAZUL YUSSERY SHADIQ       | ")
	print ("\033[1;33m       |        TOOLS ABANG GANTENG        | ")
	print ("\033[1;31m       《□》---《□》---《□》---《□》---《□》 ")
	print ("\033[1;37m         Author    : Khazul Yussery Shadiq   ")
	print ("\033[1;37m         Instagram : khazulyussery_          ")
	print (" ")
	os.system('date | lolcat')
	print (" ")

banner()


try:
	print ("\033[31;1m Berikut Daftar Toolnya : \n")	
	print ("\033[1;35m 01]. Trojan	      ")
	print ("\033[1;35m 02]. Spam Sms      ")
	print ("\033[1;35m 03]. Spam Panggilan")
	print ("\033[1;35m 04]. Auto Followers ")
	print ("\033[1;35m 05]. Facebook Hack ")
	print (" ")
	print ("\033[1;33m ╭────[Option]>[ZuLF4] ")
	u=input("\033[1;33m ╰────>>>  ")
	if u == "01" or u == "1":
		print
		os.system('clear')
		os.system('python3 modul/virus.py')
	elif u == "02" or u == "2":
		os.system('clear')
		os.system('python3 modul/spam.py')
	elif u == "03" or u == "3":
		os.system('clear')
		os.system('python3 modul/call.py')
	elif u == "04" or u == "4":
		os.system('clear')
		os.system('python3 source/autof.py')
	elif u == "05" or u == "5":
		print ("""\033[1;39m

         -----------------------------
         | FACEBOOK HACKED BY KHAZUL |
	 -----------------------------
		""")
		os.system('date | lolcat')
		print ("\033[1;33m Pilih metode : ")
		print (" -------------- ")
		print ("\033[1;33m 1). Phising      ")
		print ("\033[1;33m 2). No BF/Phising")
		print ("\033[1;33m 3). Brute Force")

		a=input("\033[1;32m Pilih >>>>: ")
		if a == "1":
			os.system('clear')
			os.system('bash modul/sc.sh')
		elif a == "2":
			os.system('clear')
			os.system('python3 source/fbi.py')
		elif a == "3":
			print (" ")
			print ("\033[1;33m Brute Force : ")
			print ("\033[1;31m ------------- ")
			print ("\033[1;33m 1). Single    ")
			print ("\033[1;33m 2). Multi     ")
			print ("\033[1;31m ------------- ")
			b=input("\033[1;35m Pilih >>>>: ")
			if b == "1":
				os.system('clear')
				os.system('python2 source/bf.py')
			elif b == "2":
				os.system('clear')
				os.system('python2 source/flb.py')
except KeyboardInterrupt:
	os.system('python3 tool.py')
