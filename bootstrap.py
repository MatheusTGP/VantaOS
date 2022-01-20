from os.path import getsize, isfile, isdir
import sqlite3 as DataBase
from time import sleep as loading
from platform import node as InfoUser
from platform import system as systeminfo
from Hardware import *
from os import system as shell


def run ():
	R = '\033[01;31m'
	G = '\033[01;32m'
	Y = '\033[01;33m'
	B = '\033[01;34m'
	M = '\033[01;35m'
	C = '\033[01;36m'
	W = '\033[01;37m'
	N = '\033[00;00m'
	
	def printing (Texto):
		for Text in Texto:
			print(Text, end='', flush=True)
			loading(0.1)

	printing(f"{'Iniciando sistema VantaOS...':>47}{N}\n")
	loading(2)
	print(f"{W}-"*67)
	printing(f"Loading {G}Bootstrap...\n")

	printing(f"\n {W} System Name:{G}VantaOS ")
	printing(f"\n {W} System_Version: {G}1.0")
	printing(f"\n {W} System_MemoryHDD = {G}512GB")
	printing(f"\n {W} System_MemoryRAM = {R} 4GB")
	printing(f"\n {W} System_Processor = {R} Nativo")
	printing(f"\n {W} System_OS = {C}VantaOS-Linux-build1.0{N}")
	
	loading(2)
	print("Aguarde a inicialização...")
	print(f"{W}-"*47)
	loading(4)
	
	shell('clear')
	printing(f"{'Starting VantaOS...':>47}")
	loading(5)

	login = 'secret'
	passwd = 'secret'
	login_user = input(f"{W}{'Username: ':>47}")
	passwd_user = input(f"{W}{'Password: ':>47}")
	
	if login_user == login and passwd_user == passwd:
		loading(2)
		shell('clear')
		printing(f"{'Welcome Secret...':>47}")
	else:
		print("{R} Login incorreto")

def Stop ():
	print("Stoping System...")
	
run()