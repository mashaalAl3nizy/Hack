import requests
import json
import pyfiglet,time
rs = requests.session()
R = "\033[1;31m"
G = "\033[1;32m"
B = "\033[0;94m"
Y = "\033[1;33m"
nu = 0
n = 0
br = pyfiglet.figlet_format("Reports")
print(B+br)
print(B+"""Send automatic reports to Instagram
---------------------------------------
""")
print('''
\x41\x62\x64\x75\x6C\x6C\x61\x68 \x41\x4C\x2D\x72\x75\x71\x61\x69\x73\x68\x69
  \x69\x6E\x73\x74\x61 \x3A\x40\x37\x2E\x37\x61\x78
________________________________________
''')
print(Y+"Log in to your Instagram account:")
print("")     
username = input("username :")
password = input("password :")
Target = input("Target :")
url = 'https://www.instagram.com/accounts/login/ajax/'
headers = {
     'accept': '*/*',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'ar,en-US;q=0.9,en;q=0.8',
    'content-length': '275',
    'content-type': 'application/x-www-form-urlencoded',
    'cookie': 'csrftoken=DqBQgbH1p7xEAaettRA0nmApvVJTi1mR; ig_did=C3F0FA00-E82D-41C4-99E9-19345C41EEF2; mid=X8DW0gALAAEmlgpqxmIc4sSTEXE3; ig_nrcb=1',
    'origin': 'https://www.instagram.com',
    'referer': 'https://www.instagram.com/',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Mobile Safari/537.36',
    'x-csrftoken': 'DqBQgbH1p7xEAaettRA0nmApvVJTi1mR',
    'x-ig-app-id': '936619743392459',
    'x-ig-www-claim': '0',
    'x-instagram-ajax': 'bc3d5af829ea',
    'x-requested-with': 'XMLHttpRequest'
    }
data = {
         'username': f'{username}',
         'enc_password': f'#PWD_INSTAGRAM_BROWSER:0:1589682409:{password}',
         'queryParams': '{}',
         'optIntoOneTap': 'false'
    }    
r = rs.post(url, headers=headers, data=data)
if  'authenticated": true' in r.text:
    rs.headers.update({'X-CSRFToken': r.cookies['csrftoken']})
    print("")
    print(G+"*"*25)	
    print("")
    print(G+"Login :"+username)
    try:
        u = rs.get(f"https://www.instagram.com/{Target}/?__a=1")
        id =  str(u.json()["graphql"]["user"]["id"])
        print(G+f"{Target} : {id}")
        print("")
        print(G+"*"*25)
    except:
    	print(R+"[!]Check the victim's account")
    	exit()
    print(R+"""
Choose the type of report :	
[1] - spam
[2] - violence
[3] - Impersonation
[4] - Sexual activity
[5] - harassment
[6] - Self-harm
[7] - Hate on

    """)
    xx = int(input("Enter the report number :"))
    print('_'*30)
    print("")
    if xx == 1:
    	P1= int(input(Y+"How many reports :"))
    	tu = int(input("time wait :"))
    	print('-'*30)
    	for i_1 in range(P1):
    		url_1=f'https://www.instagram.com/users/{id}/report/'
    		data_1={'source_name':'','reason_id':'1','frx_context':''}
    		report_1=rs.post(url_1,data=data_1)
    		if '"status": "ok"' in report_1.text:
    			nu += 1
    		else:
    			n += 1
    		print(G+f"\rSent = {nu}  {R}Error ={n}",end="")
    		time.sleep(tu)
    		
    elif xx == 2:
    	P2 = int(input(Y+"How many reports :"))
    	tu = int(input("time wait :"))
    	print('-'*30)
    	for i_2 in range(P2):
    		url_2=f'https://www.instagram.com/users/{id}/report/'
    		data_2={'source_name':'','reason_id':'5','frx_context':''}
    		report_2=rs.post(url_2,data=data_2)
    		if '"status": "ok"' in report_2.text:
    			nu += 1
    		else:
    			n += 1
    		print(G+f"\rSent = {nu}  {R}Error ={n}",end="")
    		time.sleep(tu)
    elif xx == 3:
    	P3 = int(input(Y+"How many reports :"))
    	tu = int(input("time wait :"))
    	print('-'*30)
    	for i_3 in range(P3):
    		url_3=f'https://www.instagram.com/users/{id}/report/'
    		data_3={'source_name':'','reason_id':'8','frx_context':''}
    		report_3=rs.post(url_3,data=data_3)
    		if '"status": "ok"' in report_3.text:
    			nu += 1
    		else:
    			n += 1
    		print(G+f"\rSent = {nu}  {R}Error ={n}",end="")
    		time.sleep(tu)
    elif xx == 4:
    	P4 = int(input(Y+"How many reports :"))
    	tu = int(input("time wait :"))
    	print('-'*30)
    	for i_4 in range(P4):
    		url_4=f'https://www.instagram.com/users/{id}/report/'
    		data_4={'source_name':'','reason_id':'4','frx_context':''}
    		report_4=rs.post(url_4,data=data_4)
    		if '"status": "ok"' in report_4.text:
    			nu += 1
    		else:
    			n += 1
    		print(G+f"\rSent = {nu}  {R}Error ={n}",end="")
    		time.sleep(tu)	
    elif xx == 5:
    	P5 = int(input(Y+"How many reports :"))
    	tu = int(input("time wait :"))
    	print('-'*30)
    	for i_5 in range(P5):
    		url_5=f'https://www.instagram.com/users/{id}/report/'
    		data_5={'source_name':'','reason_id':'7','frx_context':''}
    		report_5=rs.post(url_5,data=data_5)
    		if '"status": "ok"' in report_5.text:
    			nu += 1
    		else:
    			n += 1
    		print(G+f"\rSent = {nu}  {R}Error ={n}",end="")
    		time.sleep(tu)    		
    elif xx == 6:
    	P6 = int(input(Y+"How many reports :"))
    	tu = int(input("time wait :"))
    	print('-'*30)
    	for i_6 in range(P6):
    		url_6=f'https://www.instagram.com/users/{id}/report/'
    		data_6={'source_name':'','reason_id':'2','frx_context':''}
    		report_6=rs.post(url_6,data=data_6)
    		if '"status": "ok"' in report_6.text:
    			nu += 1
    		else:
    			n += 1
    		print(G+f"\rSent = {nu}  {R}Error ={n}",end="")
    		time.sleep(tu)
    elif xx == 7:
    	P7 = int(input(Y+"How many reports :"))
    	tu = int(input("time wait :"))
    	print('-'*30)
    	for i_7 in range(P7):
    		url_7=f'https://www.instagram.com/users/{id}/report/'
    		data_7={'source_name':'','reason_id':'6','frx_context':''}
    		report_7=rs.post(url_7,data=data_7)
    		if '"status": "ok"' in report_7.text:
    			nu += 1
    		else:
    			n += 1
    		print(G+f"\rSent = {nu}  {R}Error ={n}",end="")
    		time.sleep(tu)		
elif ('{"message": "checkpoint_required"') in r.text:
	print(R+"[!]checkpoint")
else:
	print(R+"Error, Try again")