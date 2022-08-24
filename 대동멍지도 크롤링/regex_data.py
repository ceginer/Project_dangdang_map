### 사이트에서 이미지 불러오기
from turtle import end_fill
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

import csv
from bs4 import BeautifulSoup as bs
import re

data = None
place_name_list=[]
location_list=[]

# # csv 파일의 1행(카페이름) 읽기
file_dir = 'C:/Users/손병우/Desktop/read_data/dogonly_read.csv'
with open(file_dir,'r', encoding='CP949') as csvfile:
  reader = csv.reader(csvfile)
  for row in reader:
    if row[0]:
      place_name_csv=row[0]
    if row[1]:
      location_csv=row[1]
    place_name_list.append(place_name_csv)
    location_list.append(location_csv)
i=1
star_list=[]
review_list=[]
fail_list=[]

ff = open(r'C:/Users/손병우/Desktop/regex_data/dogonly_new.csv', 'w', encoding='CP949', newline='')
csvWriter = csv.writer(ff)
type=input('카테고리는? : ')
for place,loc in zip(place_name_list,location_list):
  try:
    search = loc + ' ' + place            # 카테고리
    page1(search)
    
    try: 
      dict=response1.json()
      dict_prepare = dict['result']['place']['list'][0]
      id=dict_prepare['id']
      url = "https://pcmap.place.naver.com/accommodation/"+id+"/review/visitor"
      response = requests.get(url)
    except:
      continue
    
    
    response.encoding='utf-8'
    soup = bs(response.text, 'html.parser')

    try:
      star = soup.select_one('.place_section_content ._1V5HD .ANYgl em') # 별점
      star=star.text
    except:
      star=''
    
    try:
      review_select = soup.select_one('.place_section_content ._3F4VF ._3l2Wz .faZHB a span') # 리뷰
      review = review_select.text
    except:
      review = ''

    try:
      style = soup.select_one('._3F4VF ._3l2Wz ._2OQVC ._2IOo9 a div')['style'] # 리뷰 이미지
      review_img_re = re.findall('"(http.*?)"', style)
      review_img = review_img_re[0]
    except:
      review_img=''

    try:
      csvWriter.writerow([place, loc,type,star,review,review_img])
    except:
      csvWriter.writerow([place, loc,type,star,'',review_img])
    
    print(i)
    i+=1
  except:
    csvWriter.writerow(['','','','','',''])
    print('Tlqkf', i)
    fail_list.append(i)
    i+=1
    continue
    
  

ff.close()
print('Rmx')
print(fail_list)
# import pandas as pd
# data = pd.read_csv('C:/Users/손병우/Desktop/crawl/hotel_person.csv',encoding="cp949",header=None,names=['지역','주소','전화번호','카테고리','상세링크','설명','메인이미지','mapx','mapy'])
# data.index.name='이름'

# data['star']= star_list
# # data['review']=review_list
# data.to_csv("C:/Users/손병우/Desktop/panss2222.csv",encoding="cp949")


  # for review in review_list:
    #   review = review.select_one('.faZHB a .WoYOw')
      
    #   print(star)
    #   # img.append(result)

