from ctypes import WinError
from pydoc import describe
import requests
import time


### 에러 시 쉬었다가 재전송
import time
from functools import wraps


def retry(ExceptionToCheck, tries=4, delay=3, backoff=2, logger=None):
    """Retry calling the decorated function using an exponential backoff.

    http://www.saltycrane.com/blog/2009/11/trying-out-retry-decorator-python/
    original from: http://wiki.python.org/moin/PythonDecoratorLibrary#Retry

    :param ExceptionToCheck: the exception to check. may be a tuple of
        exceptions to check
    :type ExceptionToCheck: Exception or tuple
    :param tries: number of times to try (not retry) before giving up
    :type tries: int
    :param delay: initial delay between retries in seconds
    :type delay: int
    :param backoff: backoff multiplier e.g. value of 2 will double the delay
        each retry
    :type backoff: int
    :param logger: logger to use. If None, print
    :type logger: logging.Logger instance
    """
    def deco_retry(f):

        @wraps(f)
        def f_retry(*args, **kwargs):
            mtries, mdelay = tries, delay
            while mtries > 1:
                try:
                    return f(*args, **kwargs)
                except ExceptionToCheck:
                    msg = "%s, Retrying in %d seconds..." % (str('sorry'), mdelay)
                    if logger:
                        logger.warning(msg)
                    else:
                        print (msg)
                    time.sleep(mdelay)
                    mtries -= 1
                    mdelay *= backoff
            return f(*args, **kwargs)

        return f_retry  # true decorator

    return deco_retry

# 카카오 api 사용
address_list=[]
dict=[]
def xy(query):
    url = 'https://dapi.kakao.com/v2/local/search/keyword.json'
    params = {'query': query}
    headers = {"Authorization": "KakaoAK 7aeccc3c69f4ba6ee437bd9852a66879"}

    places = requests.get(url, params=params, headers=headers).json()['documents']
    if places:
      x = (places[0]['x'])
      y = (places[0]['y'])
    return x,y
  
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
place_name_list=[]
location_list=[]
review_list=[]
loc_list=[]
# csv 파일의 1행(카페이름) 읽기
file_dir = 'C:/Users/손병우/Desktop/crawl/k_hotel.csv'
with open(file_dir,'r', encoding='CP949') as csvfile:
  reader = csv.reader(csvfile)
  for row in reader:
    if row[0]:
      place_name_csv=row[0]
    if row[1]:
      location_csv=row[1]
    place_name_list.append(place_name_csv)
    loc_list.append(location_csv)

# (선희) csvWriter는 여기서 열어야 해! for문 밖에서
ff = open(r'C:/Users/손병우/Desktop/crawl/k_rewrite.csv', 'w', encoding='CP949', newline='')
csvWriter = csv.writer(ff)

locationList = ['서울','경기','인천','강원','충북','충남','대전','세종','전북','전남','광주','경북','경남','대구','울산','부산','제주']
# locationList = ['서울']

i =0
# 각 카페장소에 맞는 내용 크롤링
for place,loc in zip(place_name_list,loc_list):
  place = loc + ' ' + place
  print(i)
  i+=1
  
  page1(place)

  
  # csr파일 python형식으로 읽기
  # csr파일 첫번째
  dict=response1.json()

  if not dict:
    continue

  try:
    dict_prepare = dict['result']['place']['list'][0]
  except:
    continue

  id=dict_prepare['id']  # 각 검색결과 id

  # csr파일 python형식으로 읽기
  # csr파일 두번째(상세페이지 - id관련)
  page2(id)

  dict2=response2.json()

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
    elif '충청북도' in address:
        location = '충북'
    elif '충청남도' in address:
        location = '충남'
    elif '전라북도' in address:
        location = '전북'
    elif '전라남도' in address:
        location = '전남'
    elif '경상북도' in address:
        location = '경북'
    elif '경상남도' in address:
        location = '경남'


  try:
    type=dict_prepare['category'][0] # 카테고리
  except:
    type=''


  try:
    link1=dict_prepare['homePage'] # 상세페이지 url
  except:
    link1=''


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
    mapx, mapy = xy(place)
  except:
    mapx = ''
    mapy = ''

  try :
    booking_url = dict2['naverBookingUrl'] # 네이버 예약 링크
  except:
    booking_url = ''
  
  try:
    csvWriter.writerow([name, location,address,phone,type,link1,desc,main_img, mapy, mapx, booking_url])
  except:
    csvWriter.writerow([name, location,address,phone,type,link1,'',main_img, mapy, mapx, booking_url])

  retry(TimeoutError, tries=4, delay=3, backoff=2, logger=None)








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