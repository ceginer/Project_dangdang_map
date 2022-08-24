import requests

############ 네이버 쳤을 때 창
def page1(place):
  
  cookies = {
      'NNB': 'G5AA6C3FLZ4V2',
      'ASID': 'dbffcf840000016e3a5eee630000004a',
      'NFS': '2',
      '_ga_7VKFYR6RV1': 'GS1.1.1597901340.14.1.1597901683.46',
      'm_loc': 'd5fae313eb8f8d9c7050efd25232798d9d46bed2a51ca5b050c23aad802b4a881dfb12bada235ad6a69a9ce7f073c11ed5ec98ec7cfd21f8212a26f84dad9d5d',
      'NV_WETR_LOCATION_RGN_M': '"MDMyMjAxMTE="',
      'NV_WETR_LAST_ACCESS_RGN_M': '"MDMyMjAxMTE="',
      '_fbp': 'fb.1.1652333053952.1864013727',
      '_gcl_au': '1.1.924982538.1652333054',
      '_ga_1BVHGNLQKG': 'GS1.1.1653819791.2.1.1653819793.0',
      '_ga': 'GA1.2.1918082713.1576255170',
      '_ga_4BKHBFKFK0': 'GS1.1.1657104703.4.1.1657105489.0',
      'nx_ssl': '2',
      'csrf_token': 'c9ff8dc89d0d26f7321703f51cfc2d4448818847853c526728a4d2219155c97e9b6490d088524f5e2d1f9fdd189f23d95bdd86f6e9ca8c8b07bf30c857e040c6',
      'nid_inf': '1648409857',
      'NID_JKL': 'k/RAiTYAFS6RkhgqnogzAaXMauAE19RkQbwr15wgb58=',
      'BMR': 's=1659778687634&r=https%3A%2F%2Fm.blog.naver.com%2FPostView.naver%3FisHttpsRedirect%3Dtrue%26blogId%3Denglishtoto1%26logNo%3D220309727641&r2=https%3A%2F%2Fwww.google.com%2F',
      'page_uid': 'aa030e03-045c-47e7-b1cb-e53cf84aa4ee',
      '_naver_usersession_': 'mSmf4dxGzWxu2j4wJ8Rr8A==',
      'page_uid': 'hYtT8lp0J1Zssbe79xwsssssttl-328898',
  }

  headers = {
      'authority': 'map.naver.com',
      'accept': 'application/json, text/plain, */*',
      'accept-language': 'ko-KR,ko;q=0.8,en-US;q=0.6,en;q=0.4',
      'cache-control': 'no-cache',
      'content-type': 'application/json',
      # Requests sorts cookies= alphabetically
      # 'cookie': 'NNB=G5AA6C3FLZ4V2; ASID=dbffcf840000016e3a5eee630000004a; NFS=2; _ga_7VKFYR6RV1=GS1.1.1597901340.14.1.1597901683.46; m_loc=d5fae313eb8f8d9c7050efd25232798d9d46bed2a51ca5b050c23aad802b4a881dfb12bada235ad6a69a9ce7f073c11ed5ec98ec7cfd21f8212a26f84dad9d5d; NV_WETR_LOCATION_RGN_M="MDMyMjAxMTE="; NV_WETR_LAST_ACCESS_RGN_M="MDMyMjAxMTE="; _fbp=fb.1.1652333053952.1864013727; _gcl_au=1.1.924982538.1652333054; _ga_1BVHGNLQKG=GS1.1.1653819791.2.1.1653819793.0; _ga=GA1.2.1918082713.1576255170; _ga_4BKHBFKFK0=GS1.1.1657104703.4.1.1657105489.0; nx_ssl=2; csrf_token=c9ff8dc89d0d26f7321703f51cfc2d4448818847853c526728a4d2219155c97e9b6490d088524f5e2d1f9fdd189f23d95bdd86f6e9ca8c8b07bf30c857e040c6; nid_inf=1648409857; NID_JKL=k/RAiTYAFS6RkhgqnogzAaXMauAE19RkQbwr15wgb58=; BMR=s=1659778687634&r=https%3A%2F%2Fm.blog.naver.com%2FPostView.naver%3FisHttpsRedirect%3Dtrue%26blogId%3Denglishtoto1%26logNo%3D220309727641&r2=https%3A%2F%2Fwww.google.com%2F; page_uid=aa030e03-045c-47e7-b1cb-e53cf84aa4ee; _naver_usersession_=mSmf4dxGzWxu2j4wJ8Rr8A==; page_uid=hYtT8lp0J1Zssbe79xwsssssttl-328898',
      'expires': 'Sat, 01 Jan 2000 00:00:00 GMT',
      'pragma': 'no-cache',
      'referer': 'https://map.naver.com/',
      'sec-ch-ua': '".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"',
      'sec-ch-ua-mobile': '?0',
      'sec-ch-ua-platform': '"Windows"',
      'sec-fetch-dest': 'empty',
      'sec-fetch-mode': 'cors',
      'sec-fetch-site': 'same-origin',
      'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
  }

  global response1
  response1 = requests.get('https://map.naver.com/v5/api/search?caller=pcweb&query='+place+'&type=all&searchCoord=128.91334039999987;37.78818840000017&page=1&displayCount=20&isPlaceRecommendationReplace=true&lang=ko', cookies=cookies, headers=headers)

############################각 장소의 상세페이지
import requests

def page2(id):
  cookies = {
    'NNB': 'G5AA6C3FLZ4V2',
    'ASID': 'dbffcf840000016e3a5eee630000004a',
    'NFS': '2',
    '_ga_7VKFYR6RV1': 'GS1.1.1597901340.14.1.1597901683.46',
    'm_loc': 'd5fae313eb8f8d9c7050efd25232798d9d46bed2a51ca5b050c23aad802b4a881dfb12bada235ad6a69a9ce7f073c11ed5ec98ec7cfd21f8212a26f84dad9d5d',
    'NV_WETR_LOCATION_RGN_M': '"MDMyMjAxMTE="',
    'NV_WETR_LAST_ACCESS_RGN_M': '"MDMyMjAxMTE="',
    '_fbp': 'fb.1.1652333053952.1864013727',
    '_gcl_au': '1.1.924982538.1652333054',
    '_ga_1BVHGNLQKG': 'GS1.1.1653819791.2.1.1653819793.0',
    '_ga': 'GA1.2.1918082713.1576255170',
    '_ga_4BKHBFKFK0': 'GS1.1.1657104703.4.1.1657105489.0',
    'nx_ssl': '2',
    'csrf_token': 'c9ff8dc89d0d26f7321703f51cfc2d4448818847853c526728a4d2219155c97e9b6490d088524f5e2d1f9fdd189f23d95bdd86f6e9ca8c8b07bf30c857e040c6',
    'nid_inf': '1648409857',
    'NID_JKL': 'k/RAiTYAFS6RkhgqnogzAaXMauAE19RkQbwr15wgb58=',
    'BMR': 's=1659778687634&r=https%3A%2F%2Fm.blog.naver.com%2FPostView.naver%3FisHttpsRedirect%3Dtrue%26blogId%3Denglishtoto1%26logNo%3D220309727641&r2=https%3A%2F%2Fwww.google.com%2F',
    'page_uid': 'hYtT8lp0J1Zssbe79xwsssssttl-328898',
    'page_uid': '129552a0-b083-42e7-8d1e-85eeae8b8e99',
}

  headers = {
    'authority': 'map.naver.com',
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'ko-KR,ko;q=0.8,en-US;q=0.6,en;q=0.4',
    'cache-control': 'no-cache',
    'content-type': 'application/json',
    # Requests sorts cookies= alphabetically
    # 'cookie': 'NNB=G5AA6C3FLZ4V2; ASID=dbffcf840000016e3a5eee630000004a; NFS=2; _ga_7VKFYR6RV1=GS1.1.1597901340.14.1.1597901683.46; m_loc=d5fae313eb8f8d9c7050efd25232798d9d46bed2a51ca5b050c23aad802b4a881dfb12bada235ad6a69a9ce7f073c11ed5ec98ec7cfd21f8212a26f84dad9d5d; NV_WETR_LOCATION_RGN_M="MDMyMjAxMTE="; NV_WETR_LAST_ACCESS_RGN_M="MDMyMjAxMTE="; _fbp=fb.1.1652333053952.1864013727; _gcl_au=1.1.924982538.1652333054; _ga_1BVHGNLQKG=GS1.1.1653819791.2.1.1653819793.0; _ga=GA1.2.1918082713.1576255170; _ga_4BKHBFKFK0=GS1.1.1657104703.4.1.1657105489.0; nx_ssl=2; csrf_token=c9ff8dc89d0d26f7321703f51cfc2d4448818847853c526728a4d2219155c97e9b6490d088524f5e2d1f9fdd189f23d95bdd86f6e9ca8c8b07bf30c857e040c6; nid_inf=1648409857; NID_JKL=k/RAiTYAFS6RkhgqnogzAaXMauAE19RkQbwr15wgb58=; BMR=s=1659778687634&r=https%3A%2F%2Fm.blog.naver.com%2FPostView.naver%3FisHttpsRedirect%3Dtrue%26blogId%3Denglishtoto1%26logNo%3D220309727641&r2=https%3A%2F%2Fwww.google.com%2F; page_uid=hYtT8lp0J1Zssbe79xwsssssttl-328898; page_uid=129552a0-b083-42e7-8d1e-85eeae8b8e99',
    'expires': 'Sat, 01 Jan 2000 00:00:00 GMT',
    'pragma': 'no-cache',
    'referer': 'https://map.naver.com/',
    'sec-ch-ua': '".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
}

  params = {
    'lang': 'ko',
}
  global response2
  response2 = requests.get('https://map.naver.com/v5/api/sites/summary/'+id, params=params, cookies=cookies, headers=headers)

#############################################

place =input('어느 지역?')

page1(place)
dict=response1.json()
dict_prepare = dict['result']['place']['list'][2]

id=dict_prepare['id']

name = dict_prepare['name']
virtualTel=dict_prepare['virtualTel']
address=dict_prepare['address']
category=dict_prepare['category'][0]
menuInfo=dict_prepare['menuInfo']
hourInfo=dict_prepare['bizhourInfo']
homePage=dict_prepare['homePage']

page2(id)
dict2=response2.json()
description=dict2['description']
images=dict2['images']
image_url=[]

print(name, virtualTel,address,category,menuInfo,hourInfo,homePage,description,sep='\n')

for image in images:
  # image_url.append(image['url'])
  print(image['url'])