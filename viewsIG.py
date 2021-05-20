import requests,random,threading,time
import sys as n
import time as mm
from instabot import Bot
r=requests.session()
proxy =  open("proxy.txt",'r').read().splitlines()
b=Bot
def slow(M):
	for c in M + '\n':
		n.stdout.write(c)
		n.stdout.flush()
		mm.sleep(1. / 10)

print("""
██╗   ██╗██╗███████╗██╗    ██╗███████╗ 
██║   ██║██║██╔════╝██║    ██║██╔════╝  V2
██║   ██║██║█████╗  ██║ █╗ ██║███████╗
╚██╗ ██╔╝██║██╔══╝  ██║███╗██║╚════██║
 ╚████╔╝ ██║███████╗╚███╔███╔╝███████║
  ╚═══╝  ╚═╝╚══════╝ ╚══╝╚══╝ ╚══════╝
           INSTAGRAM @t.uo""")
slow('By JOKER AND Mustafa Kurdish ')

time.sleep(1)
POST = input('\nEnter url post : ')

idd = b.get_media_id_from_link(self='',link=POST)
print(' ')
url = 'https://sifresiz.instahile.co/c/views.php'

def vv1ck():
	while True:
		proxylist = []
		for pro in proxy:
			proxylist.append(pro)
			run = str(random.choice(proxylist))
		try:
			PROXY = {"https":run,"http":run}
			headers = {
				'Accept': 'application/json, text/javascript, */*; q=0.01',
				'Accept-Encoding': 'gzip, deflate, br',
				'Accept-Language': 'en-US,en;q=0.9',
				'Connection': 'keep-alive',
				'Content-Length': '51',
				'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
				'Cookie': '',
				'Host': 'sifresiz.instahile.co',
				'Origin': 'https://sifresiz.instahile.co',
				'Referer': 'https://sifresiz.instahile.co/views',
				'Sec-Fetch-Dest': 'empty',
				'Sec-Fetch-Mode': 'cors',
				'Sec-Fetch-Site': 'same-origin',
				'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36',
				'X-Requested-With': 'XMLHttpRequest'}
			data={
				'media_id': idd,
				'quantity': '10'}
			j=r.post(url,headers=headers,data=data,proxies=PROXY).text
			if '"sent":5' in j:
				print('[$]>> 5 views posted ')
			
			elif '"sent":4' in j:
				print('[$]>> 4 views posted ')
			
			elif '"sent":3' in j:
				print('[$]>> 3 views posted ') 
			
			elif '"sent":2' in j:
				print('[$]>> 2 views posted ')
			
			elif '"sent":1' in j:
				print('[$]>> 1 views posted ')
			
			else:
				print('Error 404 { bad proxy } !')
			
		except requests.exceptions.ConnectionError:
			pass
			
theards =[]
for i in range(300):
	th1 = threading.Thread(target=vv1ck)
	th1.start()
	theards.append(th1)
for th2 in theards:
	th2.join()      
