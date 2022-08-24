import requests

cookies = {
    'SEARCH_SAMESITE': 'CgQIkJUB',
    'OTZ': '6606368_20_20__20_',
    'HSID': 'A7yc0C1Juq2LPwEUC',
    'SSID': 'ANThYTbtgIvtCBip3',
    'APISID': 'm1Dk7hPiKc9GA-81/AT9z1luD7l8KjxD2w',
    'SAPISID': '-Hgs1bxaLY1NCFaM/A5JF5g3aF_bUxH6M7',
    '__Secure-1PAPISID': '-Hgs1bxaLY1NCFaM/A5JF5g3aF_bUxH6M7',
    '__Secure-3PAPISID': '-Hgs1bxaLY1NCFaM/A5JF5g3aF_bUxH6M7',
    '_ga': 'GA1.1.595943184.1659505270',
    'SID': 'Mwi90vg3vO0AXx6FZqGA_FEdIwr1vFChOH6mwSejADsTHbqA2FepoDpmj1cbRUquLlUg_w.',
    '__Secure-1PSID': 'Mwi90vg3vO0AXx6FZqGA_FEdIwr1vFChOH6mwSejADsTHbqAvRniJ1KhwZDytmlT_7EV3A.',
    '__Secure-3PSID': 'Mwi90vg3vO0AXx6FZqGA_FEdIwr1vFChOH6mwSejADsTHbqAE9Xkbpq9EgBd8_YVKb4iEA.',
    'OGPC': '19022552-1:19030633-1:',
    'AEC': 'AakniGNTWFFI_nlGL0LAJSFuWYQBl_qBSRmX7WxxjyIpYISZTBOlDZF_5w',
    'NID': '511=Nw8y0Ht0jRBeRSkt8FjpjmdwApqsgqCxC8mi7uDjmkECfpORRwnF5y6I19VN3SG3jD-ua8c2Oa9pUpUopTSuPdFHKO3hED2gdrr-cMfpmStaYweJYk5liKsHp7-8kkN24i7g11msrJCieO7fzTH7RVcIYqACxtyLoQ9VnBmZX1HtANOn9pTW4X_xn6iYs_8JJiR2cBk84Ji-vOwYrQ1PEWX83PLm6eNyaLcRIVcXvt2vIHwU7ByGYsm92LXl5o1J0qbCpPhkS0AyEvkj5ffptsMT2M63MX7L9rTdxgh156Ic6GCHEy7KyeZMPc4qll953RUyRUkIVXpI239LI0NqAnhTHyvawg',
    '1P_JAR': '2022-08-13-12',
    'DV': 'kxrllMLF2yRWAGyjKp6JziDbLexxKdit5q0RccyLCQAAAICGSTB--aTyIAAAAASIm0L1K13fHQAAAFb_DT3VWQh5FgAAAA',
    'SIDCC': 'AEf-XMSMdETuz_lrFfMu6yQp6brbyU4LdHdL7lsmz0AyVR2q7ZD_dbFD_1xVMaWDDFhcRbNF2tM',
    '__Secure-1PSIDCC': 'AEf-XMSsZGn-YXdpQHnTUI97Ztypo94wGYOPP-KVqDKfTJkvO-015b1DiAOHQ12c2OL7kE8l3ew',
    '__Secure-3PSIDCC': 'AEf-XMQepc5BgOx-ApHfrjaDdN7HVza1QU7MoEkYASJB_VjAj1jFC6K6Eos3IJX8uFxDbi649P4',
}

headers = {
    'authority': 'www.google.com',
    'accept': '*/*',
    'accept-language': 'ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7',
    # Requests sorts cookies= alphabetically
    # 'cookie': 'SEARCH_SAMESITE=CgQIkJUB; OTZ=6606368_20_20__20_; HSID=A7yc0C1Juq2LPwEUC; SSID=ANThYTbtgIvtCBip3; APISID=m1Dk7hPiKc9GA-81/AT9z1luD7l8KjxD2w; SAPISID=-Hgs1bxaLY1NCFaM/A5JF5g3aF_bUxH6M7; __Secure-1PAPISID=-Hgs1bxaLY1NCFaM/A5JF5g3aF_bUxH6M7; __Secure-3PAPISID=-Hgs1bxaLY1NCFaM/A5JF5g3aF_bUxH6M7; _ga=GA1.1.595943184.1659505270; SID=Mwi90vg3vO0AXx6FZqGA_FEdIwr1vFChOH6mwSejADsTHbqA2FepoDpmj1cbRUquLlUg_w.; __Secure-1PSID=Mwi90vg3vO0AXx6FZqGA_FEdIwr1vFChOH6mwSejADsTHbqAvRniJ1KhwZDytmlT_7EV3A.; __Secure-3PSID=Mwi90vg3vO0AXx6FZqGA_FEdIwr1vFChOH6mwSejADsTHbqAE9Xkbpq9EgBd8_YVKb4iEA.; OGPC=19022552-1:19030633-1:; AEC=AakniGNTWFFI_nlGL0LAJSFuWYQBl_qBSRmX7WxxjyIpYISZTBOlDZF_5w; NID=511=Nw8y0Ht0jRBeRSkt8FjpjmdwApqsgqCxC8mi7uDjmkECfpORRwnF5y6I19VN3SG3jD-ua8c2Oa9pUpUopTSuPdFHKO3hED2gdrr-cMfpmStaYweJYk5liKsHp7-8kkN24i7g11msrJCieO7fzTH7RVcIYqACxtyLoQ9VnBmZX1HtANOn9pTW4X_xn6iYs_8JJiR2cBk84Ji-vOwYrQ1PEWX83PLm6eNyaLcRIVcXvt2vIHwU7ByGYsm92LXl5o1J0qbCpPhkS0AyEvkj5ffptsMT2M63MX7L9rTdxgh156Ic6GCHEy7KyeZMPc4qll953RUyRUkIVXpI239LI0NqAnhTHyvawg; 1P_JAR=2022-08-13-12; DV=kxrllMLF2yRWAGyjKp6JziDbLexxKdit5q0RccyLCQAAAICGSTB--aTyIAAAAASIm0L1K13fHQAAAFb_DT3VWQh5FgAAAA; SIDCC=AEf-XMSMdETuz_lrFfMu6yQp6brbyU4LdHdL7lsmz0AyVR2q7ZD_dbFD_1xVMaWDDFhcRbNF2tM; __Secure-1PSIDCC=AEf-XMSsZGn-YXdpQHnTUI97Ztypo94wGYOPP-KVqDKfTJkvO-015b1DiAOHQ12c2OL7kE8l3ew; __Secure-3PSIDCC=AEf-XMQepc5BgOx-ApHfrjaDdN7HVza1QU7MoEkYASJB_VjAj1jFC6K6Eos3IJX8uFxDbi649P4',
    'referer': 'https://www.google.com/',
    'sec-ch-ua': '"Chromium";v="104", " Not A;Brand";v="99", "Google Chrome";v="104"',
    'sec-ch-ua-arch': '"x86"',
    'sec-ch-ua-bitness': '"64"',
    'sec-ch-ua-full-version': '"104.0.5112.81"',
    'sec-ch-ua-full-version-list': '"Chromium";v="104.0.5112.81", " Not A;Brand";v="99.0.0.0", "Google Chrome";v="104.0.5112.81"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-ch-ua-platform-version': '"10.0.0"',
    'sec-ch-ua-wow64': '?0',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36',
    'x-client-data': 'CIu2yQEIpbbJAQjEtskBCKmdygEI14HLAQiUocsBCL68zAEIxLzMAQiAwcwBCJvBzAEIs8HMAQjEwcwBCNfBzAEI3cTMAQjfxMwBCL3GzAEInMnMAQjjy8wB',
}

response = requests.get('https://www.google.com/maps/vt?pb=!1m4!1m3!1i9!2i435!3i197!1m4!1m3!1i9!2i435!3i198!1m4!1m3!1i9!2i435!3i199!1m4!1m3!1i9!2i436!3i197!1m4!1m3!1i9!2i437!3i197!1m4!1m3!1i9!2i436!3i198!1m4!1m3!1i9!2i436!3i199!1m4!1m3!1i9!2i437!3i198!1m4!1m3!1i9!2i437!3i199!1m4!1m3!1i9!2i438!3i197!1m4!1m3!1i9!2i438!3i198!1m4!1m3!1i9!2i438!3i199!2m3!1e0!2sm!3i614345944!2m48!1e2!2sspotlight-no-personal!5i1!8m44!11e7!12m40!3m1!3s0x35632df441b9c5cf%3A0xd78877e119775c1f!3m1!3s0x35632db97d0d32d5%3A0xb58f06332b13e4!3m1!3s0x35633e9cda995c3f%3A0x5e5cb07a544966e!3m1!3s0x356332770d1d7a7f%3A0xdb42fd13a5961ca9!3m1!3s0x356310326128f5bd%3A0xcf5497237fe0d99d!3m1!3s0x356332711a79abeb%3A0xd680874b67b2c2e5!3m1!3s0x3562d762c877ac27%3A0x2c1e4e52a7da397e!3m1!3s0x3562d3b984ac1a6f%3A0x7aaad51332d19957!3m1!3s0x35631323561d1815%3A0x9100d64c69353a29!3m1!3s0x357b0b0bf0c1e883%3A0x18fd714e78199dae!3m1!3s0x356333ae0c62d469%3A0xe2d49bb29c94dc0a!3m1!3s0x35632df458dad265%3A0x1a7c847fe6c1f7fd!3m1!3s0x3562d86178c545e1%3A0xf8c715aeb8ca8c6d!3m1!3s0x35632b9b869b84b9%3A0x192afea7a190654d!3m1!3s0x357ce0725f955453%3A0xef1e5f80462cb67!3m1!3s0x35632ddb664f3877%3A0x203b5b0204cc255d!3m1!3s0x356313a4723c4663%3A0xfc83085e2a247264!3m1!3s0x35632df45fddc477%3A0x9fb6a287c46230e0!3m1!3s0x35632b2197e9ed09%3A0x6177beca1c22571f!3m1!3s0x3562d5df0439ad57%3A0xa95f808d7887feb9!20m1!1e4!3m12!2sko-KR!3sKR!5e78!12m4!1e68!2m2!1sset!2sRoadmap!12m3!1e37!2m1!1ssmartmaps!4e3!12m1!5b1!23i1379903&client=google-maps-lite&token=44645', cookies=cookies, headers=headers)




print(response.text)