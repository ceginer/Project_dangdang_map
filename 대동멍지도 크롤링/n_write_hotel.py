from pydoc import describe
import requests
import time

# 네이버 검색 api 사용
client_id = "36NgoXERBPivzcHTqRIs"
client_secret = "pPxIN3EzzC"

def get_naver_result(keyword):
    time.sleep(0.1)
    api_url = f"https://openapi.naver.com/v1/search/local.json?query={keyword}&display=10&start=1&sort=random"
    headers = {'X-Naver-Client-Id': client_id, 'X-Naver-Client-Secret': client_secret }
    # 검색 결과를 data에 저장합니다.
    data = requests.get(api_url, headers=headers)
    data = data.json()
    return data['items']

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
import csv
import os
import pandas as pd

data = None
cafe_name_list=[]
location_list=[]
# csv 파일의 1행(카페이름) 읽기
file_dir = 'C:/Users/손병우/Desktop/Daedong_Mung!/hotel_edit.csv'


# (선희) csvWriter는 여기서 열어야 해! for문 밖에서
ff = open(r'C:/Users/손병우/Desktop/Daedong_Mung!/hotel_edit.csv', 'w', encoding='CP949', newline='')
csvWriter = csv.writer(ff)

locationList = ['서울','경기','인천','강원','충청북도','충청남도','대전','세종','전라북도','전라남도','광주','경상북도','경상남도','대구','울산','부산','제주']
# locationList = ['서울']

i =1
# 각 카페장소에 맞는 내용 크롤링
for place in locationList:
  place = place + ' 반려동물 호텔'
  page1(place)
  
  # csr파일 python형식으로 읽기
  # csr파일 첫번째
  dict=response1.json()

  if not dict:
    continue
  
  try:
    pre_dict = dict['result']['place']['list']
  except:
    continue

  for dict_prepare in pre_dict:
    id=dict_prepare['id']  # 각 검색결과 id


    name = dict_prepare['name']

    try:
      phone=dict_prepare['virtualTel'] # 전화번호
    except:
      phone=''

    address=dict_prepare['address'] # 주소

    location = '기타' # location -> 경기, 서울, 전남, 전북, 대구, 등등
    for loc in locationList:
      if loc in address:
          location = loc 

    try:
      type=dict_prepare['category'] # 카테고리
      for type_category in type:
        if "반려동물호텔" in type:
            type = '반려동물호텔'
        else:
            type = '지우자' 
    except:
      type=''

    # try:
    #   hourInfo=dict_prepare['bizhourInfo'] # 영업시간
    # except:
    #   hourInfo=''

    try:
      link1=dict_prepare['homePage'] # 상세페이지 url
    except:
      link1=''

    page2(id)

    # csr파일 python형식으로 읽기
    # csr파일 두번째(상세페이지 - id관련)
    dict2=response2.json()

    try:
      desc=dict2['description'] # 상세내용
    except:
      desc=''

    try:
      main_img=dict2['imageURL'] # 메인이미지 url
    except:
      main_img=''

    try:
      images=dict2['images'] # 이미지 url 여러개
    except:
      images=''

    try:
      res = get_naver_result(name)
    except:
      res = ''
    if res:
      mapx = res[0]['mapx'] # for 지도 api
      mapy = res[0]['mapy']
    else:
      mapx = ''
      mapy = ''

    
    try:
      if type == '지우자' or type == '':
        continue
      if type == '반려동물호텔':
        csvWriter.writerow([name, location,address,phone,type,link1,desc,main_img, mapx, mapy])
    except:
      if type == '지우자' or type == '':
        continue
      if type == '반려동물호텔':
        csvWriter.writerow([name, location,address,phone,type,link1,'',main_img, mapx, mapy])      

    print(i)
    i+=1



  

  # df_add = pd.read_csv('./test.csv')

  # df_add['전화번호'] = virtualTel
  # df_add['주소'] = address
  # df_add['카테고리'] = category
  # df_add['메뉴'] = menuInfo
  # df_add['영업시간'] = hourInfo
  # df_add['상세페이지'] = homePage
  # df_add['상세내용'] = description
  # df_add['메인이미지 url url'] = main_img

  # if not os.path.exists('./test_fin.csv'):
  #   df_add.to_csv('./test_fin.csv', index=False, mode='w', sep=',', na_rep='NaN', encoding='utf-8')
  # else:
  #   df_add.to_csv('./test_fin.csv', index=False, mode='a', sep=',', na_rep='NaN', encoding='utf-8', header=False)
  # # df_add.to_csv('./test.csv', index=False, mode='a', sep=',', na_rep='NaN', encoding='utf-8')

ff.close()
print('끝')

# # 이미지 url 들 저장
# image_url=[]

# for image in images:
#   image_url.append(image['url'])