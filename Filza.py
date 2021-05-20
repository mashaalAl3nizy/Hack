import time as mm
import py_compile
import sys as n
import requests
import colorama
import random
import os
import time
done = 0
count = 0
filza77 = requests.session()


def slow(M):
    for c in M + '\n':
        n.stdout.write(c)
        n.stdout.flush()
        mm.sleep(1. / 130)


slow("""
                   _             _     _  
                  (_)           (_)   | | 
 ___  ___  ___ ___ _  ___  _ __  _  __| | 
/ __|/ _ \/ __/ __| |/ _ \| '_ \| |/ _` | 
\__ \  __/\__ \__ \ | (_) | | | | | (_| | 
|___/\___||___/___/_|\___/|_| |_|_|\__,_|

            ╔═╗ ┬ ┬   ──┐ ┌─┐
            ╠╣  │ │   ┌─┘ ├─┤
            ╚   ┴ ┴─┘ └── ┴ ┴ •••
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
""")
time.sleep(1)
slow('''

[1] استخراج كوكيز الانستا 
[2] استخراج هيدوزر الانستا 
[3] استخراج SessionId الانستا 
[4] تشفير الملفات 
[5] تشيكر انستا 
[6] تشيكر تيك توك

cheinsta need user.txt
chetik need user.txt
list maker need file named (list)
''')

filza = input('ضع رقم الاداة  to 6 -->: ')

if filza == '1':
    filza55 = input("ادخل يوزر وهمي : ")
    flza14 = "ishehhrkjf"

    url = 'https://www.instagram.com/accounts/login/ajax/'

    data = {
        'username': f'{filza55}',
        'enc_password': f'#PWD_INSTAGRAM_BROWSER:0:1589682409:{flza14}',
        'queryParams': '{}',
        'optIntoOneTap': 'false'
    }
    filza5555 = requests.get(url, data=data)
    print(filza5555.cookies)
    print('================================')


elif filza == '2':
    filza77 = input("ادخل يوزر وهمي : ")
    flza1 = "ishehhrkjf"

    url = 'https://www.instagram.com/accounts/login/ajax/'

    data = {
        'username': f'{filza77}',
        'enc_password': f'#PWD_INSTAGRAM_BROWSER:0:1589682409:{flza1}',
        'queryParams': '{}',
        'optIntoOneTap': 'false'
    }

    solo = requests.get(url, data=data)
    print(solo.headers)
    print('===============================')


elif filza == '3':
    print('==================================')
    flz = input(">> ادخل يوزر حسابك : ")
    flza = input(">> ادخل كلمة السر : ")
    url = 'https://www.instagram.com/accounts/login/ajax/'

    headers = {
        'accept': '/',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'en-US,en;q=0.9',
        'content-length': '280',
        'content-type': 'application/x-www-form-urlencoded',
        'cookie': 'ig_did=CBE027FC-62A2-4383-85BB-63843B14C94F; ig_nrcb=1; mid=X85qiQALAAFugGOZjugz_zBUZQHx; rur=FTW; csrftoken=StAq7OrFQoEnjWE5hM2rAGfLJ1rlYIDw; urlgen="{\"92.99.169.35\": 5384\054 \"92.99.169.72\": 5384\054 \"86.97.38.223\": 5384}:1kzMQx:MlJ6OtOcQFBcQVtyCVX1ovmWQgo"',
        'origin': 'https://www.instagram.com',
        'referer': 'https://www.instagram.com/',
        'sec-ch-ua': '"Google Chrome";v="87", " Not;A Brand";v="99", "Chromium";v="87"',
        'sec-ch-ua-mobile': '?0',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36',
        'x-csrftoken': 'StAq7OrFQoEnjWE5hM2rAGfLJ1rlYIDw',
        'x-ig-app-id': '936619743392459',
        'x-ig-www-claim': 'hmac.AR1E27wkqxwu9UGaCTOBjN7TvkEIsagJ9ARc3XDbRk-sEjXF',
        'x-instagram-ajax': 'ec08b20500dd',
        'x-requested-with': 'XMLHttpRequest'

    }

    data = {
        'username': f'{flz}',
        'enc_password': f'#PWD_INSTAGRAM_BROWSER:0:1589682409:{flza}',
        'queryParams': '{}',
        'optIntoOneTap': 'false'
    }

    joker = filza77.post(url, headers=headers, data=data)

    if 'authenticated": true' in joker.text:
        print("Done Login ..")
        time.sleep(1)
        print("____________________________")
        req = filza77.cookies["sessionid"]
        print(f"sessionid >> ( {req} )")

    elif 'authenticated": false' in joker:
        print('')
        print("  >>  Error Login !")

    else:
        print("  >>  Errors ... ")

elif filza == '4':
    print('==================================')


    def slow(M):
        for c in M + '\n':
            n.stdout.write(c)
            n.stdout.flush()
            mm.sleep(1. / 200)


    done = 0
    print(" ")
    time.sleep(1)
    slow("""

█   __ _ _          
  / _(_) |         
 | |_ _| |______ _ 
 |  _| | |_  / _` |
 | | | | |/ / (_| |
 |_| |_|_/___\__,_|
            Coded By | Filza
•••••••••••••••••••••••                                                              
Rights : الحقوق
𝚃𝙴𝙻𝙴𝙶𝚁𝙰𝙼 ~ تلجرام   
my user: @Filza_507
•••••••••••••••••••••••
            ╔═╗ ┬ ┬   ──┐ ┌─┐
            ╠╣  │ │   ┌─┘ ├─┤
            ╚   ┴ ┴─┘ └── ┴ ┴ •••
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
""")

    time.sleep(1)
    slow('[!] @Filza_507 ')
    print(" ")
    time.sleep(1)
    filza875 = input('[?] اكتب اسم الملف : ')
    py_compile.compile(filza875)
    print(" ")
    slow("=                    1% ")
    time.sleep(1)
    slow("======               25%")
    time.sleep(1)
    slow("==========           50%")
    time.sleep(1)
    slow("===============      75%")
    time.sleep(1)
    slow("==================== 100%")
    print(" ")
    slow('Encryption successful ')
    print(" ")
    print(" ")
    slow('')
    py_compile.compile(filza875)
    print('')
    print("")

elif filza == '5':
    colorama.init()
    id = input(" ضع ايدي حسابك : ")
    time.sleep(1)
    token = input(" ضع توكن بوتك : ")
    time.sleep(1)

    done = """[$] user insta 🏴‍☠️ :
〰️〰️〰️〰️〰️〰️〰️〰️"""

    use = "[$] >> "

    floz50 = """〰️〰️〰️〰️〰️〰️〰️〰️
@Filza_507 / 🏴‍☠️"""

    user = "user.txt"
    file = open(user, "r")


    def checker():
        while True:
            user = file.readline().split('\n')[0]
            req = requests.get("https://www.instagram.com/" + user)

            if req.status_code == 404:
                print(f'\n[+] IS AVAILABLE OR BANNED {user}')
                tlg = (
                    f'https://api.telegram.org/bot{token}/sendMessage?chat_id={id}&text={done}\n{use} {user}\n{floz50}')
                req = requests.post(tlg)

            elif req.status_code == 200:
                print(f'\n[-]{user} IS NOT AVAILABLE')


    checker()

elif filza == '6':
    slow("""
	<----------------------------------------->
	           [ Rights | الحقوق ]
	           ( by @Filza_507 )
	         | (VPN) تنبيه الاداه تحتاج | 

	<----------------------------------------->

	""")
    username = input("[!]يرجى ادخال اسم الملف الي فيه اليوزرات -> : ")
    use = username
    headers = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36",
        "Connection": "close",
        "Host": "www.tiktok.com",
        "Accept-Encoding": "gzip, deflate",
        "Cache-Control": "max-age=0"
    }
    file = open(username, "r")

    while True:
        Check = file.readline().split('\n')[0]
        tiklog = f'https://www.tiktok.com/@{Check}'
        rq = requests.get(tiklog, headers=headers)
        if rq.status_code == 404:
            print("|==============================|")
            print("[√] هاذة اليوزر متاح او مبند  ✅ -> : " + Check)
        elif rq.status_code == 200:
            print("|==============================|")
            print("[!] هاذة اليوزر غير متاح ❌ -> : " + Check)
            if (Check == ""):
                break




input("تم الانتهاء من الاداه يرجى ضغط انتر للخروج.")
slow('''

        ♡––––––––––––––——♡☠THANK YOU FOR DOWNLOADING THIS FILE♡––––––––––––––——♡
     ✅    📌special thanks :📌
       ✅   🔕<@M3GON>📵               
         ✅   🔕<@vv1ck>📵
            ✅  🔕<@J_Q_N>📵           
               ✅ 🔕<@berlivoutt>📵
                  ✅ 🔕<JOKER>📵
        <<<<<<<<<<<<<<<<<special thanks to group:https://t.me/sol4o>>>>>>>>>>>>>>>
                                  Coded By | filza
''')
print('ending of file ✅ ')
