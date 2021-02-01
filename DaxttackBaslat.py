
# python 3.3.2 üstü çalışılır
# by Daxtill
# Discord: Daxtill•EAUS#6318
# Mail : daxtill@protonmail.com
# İllegal kullanımlarından ben sorumlu değilim.

from queue import Queue
from optparse import OptionParser
import time,sys,socket,threading,logging,urllib.request,random
import argparse
import os 
import tools.addons.clean1
import tools.addons.logo
import tools.addons.clean

#Dosyaya git
os.chdir(os.path.dirname(os.path.realpath(__file__)))




def usage():
	print (''' \033[92m  
        
       ███████                       ██     ██                     ██
      ░██░░░░██                     ░██    ░██                    ░██
      ░██    ░██  ██████   ██   ██ ██████ ██████  ██████    █████ ░██  ██
      ░██    ░██ ░░░░░░██ ░░██ ██ ░░░██░ ░░░██░  ░░░░░░██  ██░░░██░██ ██
      ░██    ░██  ███████  ░░███    ░██    ░██    ███████ ░██  ░░ ░████
      ░██    ██  ██░░░░██   ██░██   ░██    ░██   ██░░░░██ ░██   ██░██░██
      ░███████  ░░████████ ██ ░░██  ░░██   ░░██ ░░████████░░█████ ░██░░██
      ░░░░░░░    ░░░░░░░░ ░░   ░░    ░░     ░░   ░░░░░░░░  ░░░░░  ░░  ░

            
		                                                        By Daxtill
            •••••••••••••••••••••••••••••••••••••
            • Daxttack Tool'a Hoş Geldiniz.     •
            • Daxtill tarafından geliştirildim. •
            • İçimde TCP , UDP ve HTTP          •
            • olmak üzere 3 farklı Ddos Methodu •
            • barındırmaktayım.                 •
            •••••••••••••••••••••••••••••••••••••

                 --S:E:Ç:İ:M--
		  
            1) HTTP  2) TCP 3) UDP
	    
	   
			

		
					
           

			 

       


         NOT:İLLEGAL OLARAK KULLANILMASI BENİM SORUMLULUĞUMDA DEĞİLDİR
  ______________________________________________________________________________________
                                                                                          
																						  \033[0m''')

def usage2():
	print (''' \033[92m  
        
		
            D:A:X:T:T:A:C:K H:T:T:P A:T:T:A:C:K
	    _______________________________________________  
	   Uyarı: Lütfen VDS , VPS gibi sistemlerde kullanınız.
	            bağlantınız hasar görebilir.
	    _______________________________________________
	                   \033[0m''')
	time.sleep(3)

def clear():
    """
        
    """
    # İşletim Sistemi Windows ise
    if os.name == 'nt':
        _ = os.system('cls')
    # İşletim Sistemi MacOS ise
    elif os.name == 'mac':
        _ = os.system('clear')
    # İşletim Sistemi Linux ise
    elif os.name == 'posix':
        _ = os.system('clear')
    # Yabancı bir işletim sistemi ise
    else:
        _ = os.system('clear')




usage()
choice = str(input("\033[35mAttack numarası girin. >"))

if choice == '1':
		os.system('python3 DaxttackHTTP.py')

	
if choice == '2':
		os.system('python3 DaxttackTCP.py')


if choice == '3':
		os.system('python3 DaxttackUDP.py')











	
		








