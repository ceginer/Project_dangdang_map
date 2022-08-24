import requests
# from bs4 import BeautifulSoup as bs

# url = "https://www.google.com/search?newwindow=1&tbs=lf:1,lf_ui:9&tbm=lcl&q=%EA%B0%95%EB%A6%89+%EC%95%A0%EA%B2%AC%EB%8F%99%EB%B0%98%EC%B9%B4%ED%8E%98#rlfi=hd:;si:;mv:[[37.91782794217003,129.15929785493162],[37.611137047179426,128.6312674594238],null,[37.76464146543089,128.89528265717772],11]"
# response = requests.get(url)

# soup = bs(response.text,'html.parser')

# raw_result = soup.select_one(".CR1S4b")
# print(raw_result)
import requests

cookies = {
    'SEARCH_SAMESITE': 'CgQIkJUB',
    'OTZ': '6606368_20_20__20_',
    'S': 'billing-ui-v3=CrcBtXNvIfi2c4DwxTcgZFBXcMhiHr3N:billing-ui-v3-efe=CrcBtXNvIfi2c4DwxTcgZFBXcMhiHr3N',
    'HSID': 'A7yc0C1Juq2LPwEUC',
    'SSID': 'ANThYTbtgIvtCBip3',
    'APISID': 'm1Dk7hPiKc9GA-81/AT9z1luD7l8KjxD2w',
    'SAPISID': '-Hgs1bxaLY1NCFaM/A5JF5g3aF_bUxH6M7',
    '__Secure-1PAPISID': '-Hgs1bxaLY1NCFaM/A5JF5g3aF_bUxH6M7',
    '__Secure-3PAPISID': '-Hgs1bxaLY1NCFaM/A5JF5g3aF_bUxH6M7',
    '_ga': 'GA1.1.595943184.1659505270',
    'OGPC': '19022552-1:',
    'SID': 'Mwi90vg3vO0AXx6FZqGA_FEdIwr1vFChOH6mwSejADsTHbqA2FepoDpmj1cbRUquLlUg_w.',
    '__Secure-1PSID': 'Mwi90vg3vO0AXx6FZqGA_FEdIwr1vFChOH6mwSejADsTHbqAvRniJ1KhwZDytmlT_7EV3A.',
    '__Secure-3PSID': 'Mwi90vg3vO0AXx6FZqGA_FEdIwr1vFChOH6mwSejADsTHbqAE9Xkbpq9EgBd8_YVKb4iEA.',
    'AEC': 'AakniGOy6JaTpQnc5G3redclQAWC82FXNINi6iR6zZmUQhI3fOjp4lU_RUI',
    'NID': '511=TL1_1IVBPN7QLnLQE56yJX1R9scM28cMwXKU7UxQEGJ_e646uNKbVpF-pRvmYGZ3H1EbCWTMyMKA00Upi-qvbs0rbQuV7Xrc6mg9j_cRY0zB9zDKAgx1KI0cCs3vtX1MWt-DDy9-I1GZuFTuKcojebYfyaVYARv0lbHJR8_ZBLXroqGnouCQrBBKNui4G2dzvQ6W-00XAz3CgN20BIGPxrv3W7dvsk7vwZVnsNmHtAQMhlFpNuJR78J9XbUlzKZVNvn5Ea08lnaCyEfeW54y908DLrdYJagqZRcjppYAts3wT123Hj8Aq5caKzUU_wmL4Iod79i5nKfep39JjfouuFLHR1cu6w',
    '1P_JAR': '2022-08-04-06',
    'DV': 'kxrllMLF2yRWAGyjKp6JziBbBWF6JliAuClUv9L1XQEAAICGSTB--aTyYAAAANxq3hoRx7yYNAAAAFb_DT3VWQh5FwAAAA',
    'SIDCC': 'AEf-XMS--hA8hXHhfZQMrWZYJQ5DSdapQ6nN5wRdJ53D_H5I1qi1IpVdHO06NomGGLBCnA_Iz0Y',
    '__Secure-1PSIDCC': 'AEf-XMSht1DJmL0i--chAVC3ffDNw__N-7ymMQnrk6HLqEO7KzKVSiseUTFS1J_AO_l7xJhzmHM',
    '__Secure-3PSIDCC': 'AEf-XMQO9t7a8qUAodGR3vlEItDUUBaD8xyN93Yp0Z6YzS11SF8z4Zmtdp3STwXQPA4yCiT34Kk',
}

headers = {
    'authority': 'www.google.com',
    'accept': '*/*',
    'accept-language': 'ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7',
    # Requests sorts cookies= alphabetically
    # 'cookie': 'SEARCH_SAMESITE=CgQIkJUB; OTZ=6606368_20_20__20_; S=billing-ui-v3=CrcBtXNvIfi2c4DwxTcgZFBXcMhiHr3N:billing-ui-v3-efe=CrcBtXNvIfi2c4DwxTcgZFBXcMhiHr3N; HSID=A7yc0C1Juq2LPwEUC; SSID=ANThYTbtgIvtCBip3; APISID=m1Dk7hPiKc9GA-81/AT9z1luD7l8KjxD2w; SAPISID=-Hgs1bxaLY1NCFaM/A5JF5g3aF_bUxH6M7; __Secure-1PAPISID=-Hgs1bxaLY1NCFaM/A5JF5g3aF_bUxH6M7; __Secure-3PAPISID=-Hgs1bxaLY1NCFaM/A5JF5g3aF_bUxH6M7; _ga=GA1.1.595943184.1659505270; OGPC=19022552-1:; SID=Mwi90vg3vO0AXx6FZqGA_FEdIwr1vFChOH6mwSejADsTHbqA2FepoDpmj1cbRUquLlUg_w.; __Secure-1PSID=Mwi90vg3vO0AXx6FZqGA_FEdIwr1vFChOH6mwSejADsTHbqAvRniJ1KhwZDytmlT_7EV3A.; __Secure-3PSID=Mwi90vg3vO0AXx6FZqGA_FEdIwr1vFChOH6mwSejADsTHbqAE9Xkbpq9EgBd8_YVKb4iEA.; AEC=AakniGOy6JaTpQnc5G3redclQAWC82FXNINi6iR6zZmUQhI3fOjp4lU_RUI; NID=511=TL1_1IVBPN7QLnLQE56yJX1R9scM28cMwXKU7UxQEGJ_e646uNKbVpF-pRvmYGZ3H1EbCWTMyMKA00Upi-qvbs0rbQuV7Xrc6mg9j_cRY0zB9zDKAgx1KI0cCs3vtX1MWt-DDy9-I1GZuFTuKcojebYfyaVYARv0lbHJR8_ZBLXroqGnouCQrBBKNui4G2dzvQ6W-00XAz3CgN20BIGPxrv3W7dvsk7vwZVnsNmHtAQMhlFpNuJR78J9XbUlzKZVNvn5Ea08lnaCyEfeW54y908DLrdYJagqZRcjppYAts3wT123Hj8Aq5caKzUU_wmL4Iod79i5nKfep39JjfouuFLHR1cu6w; 1P_JAR=2022-08-04-06; DV=kxrllMLF2yRWAGyjKp6JziBbBWF6JliAuClUv9L1XQEAAICGSTB--aTyYAAAANxq3hoRx7yYNAAAAFb_DT3VWQh5FwAAAA; SIDCC=AEf-XMS--hA8hXHhfZQMrWZYJQ5DSdapQ6nN5wRdJ53D_H5I1qi1IpVdHO06NomGGLBCnA_Iz0Y; __Secure-1PSIDCC=AEf-XMSht1DJmL0i--chAVC3ffDNw__N-7ymMQnrk6HLqEO7KzKVSiseUTFS1J_AO_l7xJhzmHM; __Secure-3PSIDCC=AEf-XMQO9t7a8qUAodGR3vlEItDUUBaD8xyN93Yp0Z6YzS11SF8z4Zmtdp3STwXQPA4yCiT34Kk',
    'referer': 'https://www.google.com/',
    'sec-ch-ua': '".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"',
    'sec-ch-ua-arch': '"x86"',
    'sec-ch-ua-bitness': '"64"',
    'sec-ch-ua-full-version': '"103.0.5060.134"',
    'sec-ch-ua-full-version-list': '".Not/A)Brand";v="99.0.0.0", "Google Chrome";v="103.0.5060.134", "Chromium";v="103.0.5060.134"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-ch-ua-platform-version': '"10.0.0"',
    'sec-ch-ua-wow64': '?0',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
    'x-client-data': 'CIu2yQEIpbbJAQjEtskBCKmdygEI14HLAQiTocsBCNvvywEItLrMAQiJu8wBCL68zAEI4LzMAQiLv8wBCIDBzAEIm8HMAQizwcwBCMTBzAEI18HMAQjdxMwBCN/EzAEIvcbMARirqcoB',
}
import json

response = requests.get('https://www.google.com/search?vet=12ahUKEwiDlqeFzqz5AhXbtVYBHeD6Bw0QoEQoAHoECAIQAw..i&ei=GG7rYoOqENvr2roP4PWfaA&tbs=lrf:!1m4!1u3!2m2!3m1!1e1!1m4!1u2!2m2!2m1!1e1!2m1!1e2!2m1!1e3!3sIAE,lf:1,lf_ui:9&yv=3&tbm=lcl&fll=37.76464146543089,128.89528265717772&fspn=0.3066908949906022,0.5280303955078125&fz=11&sll=37.76464146543089,128.89528265717772&sspn=0.3066908949906022,0.5280303955078125&sz=11&q=%EA%B0%95%EB%A6%89+%EC%95%A0%EA%B2%AC%EB%8F%99%EB%B0%98%EC%B9%B4%ED%8E%98&ved=2ahUKEwiDlqeFzqz5AhXbtVYBHeD6Bw0Q0Cd6BQgCEK0C&start=0&asearch=rl_ist&cs=0&async=num:20,idx:0,hdr:true,stick:,_id:rl_ist0,_pms:s,_fmt:pc', cookies=cookies, headers=headers)

response.text

print("Data retrieved")
# import requests
