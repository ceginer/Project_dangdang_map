# <1. 방식> 모든 제목&리뷰 검사 -> 리뷰 '동반' 검사 -> 그것의 제목&리뷰 나타내기
# <2. 속도> 훨씬 빨라짐 (강릉 기준 약 8~9초 걸림)
# <3. 지역 선택> input 통해 지역 입력시 해당하는 구글 검색페이지 이동
# <4. csv 저장> 7페이지 까지 csv 저장

############ 구글 크롤링 ###############
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import csv

options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-logging"])
driver =webdriver.Chrome("./chromedriver", options=options)

def google_crawl():
  url = "https://www.google.com/search?q="+query+'+애견동반카페'+"&newwindow=1&tbm=lcl&sxsrf=ALiCzsbVCyPLmiOJs7RCE3tAYtQBG1I-Ow:1659626914458&ei=ouXrYtfJG5aw2roPl6qNgAU&start="+str(urlnum)+"&sa=N&ved=2ahUKEwjXosiFwK35AhUWmFYBHRdVA1AQ8tMDegUIAxCdAg"
  driver.get(url)
  driver.implicitly_wait(5)

  search_list=[]
  search_raw = driver.find_elements(By.CLASS_NAME, 'OSrXXb' )

  for i in search_raw:
    search = i.text
    search_list.append(search)

  num =0
  
  for i in search_list:
    if ('동반' in i) and ('"' in i):
      print(search_list[num-1])
      print(i)
      all.append([search_list[num-1],i])
      cafe_list.append(search_list[num-1])
      review_list.append(i)
      
    num += 1

  
################ 네이버 크롤링 ##################
from urllib import request
from winreg import REG_QWORD
import requests
from bs4 import BeautifulSoup as bs

### 지역 + 장소이름 + 전화번호 형태로 할 것.

def naver_crawl():
  url = "https://search.naver.com/search.naver?sm=tab_hty.top&where=nexearch&query="+query+cafe+'전화번호'
  response = requests.get(url)
  soup = bs(response.text, 'html.parser')


  raw_phone = soup.select_one('.place_section_content ._3ZA0S')
  phone_list.append(raw_phone.text)
  print(raw_phone.text)




############## 통합 ###############
import pandas as pd
urlnum=0

# 지역 선택
query = input("어느 지역을 원하시나요?")

# 각자 리스트
cafe_list = []
review_list = []
phone_list = []
all=[]

# 페이지 7번 크롤링
for i in range(3):
  google_crawl()
  for cafe in cafe_list:
    naver_crawl()
  urlnum += 20

# 판다스 이용
data = pd.DataFrame(google_crawl)
data.columns=['카페 장소', '리뷰']
data.to_csv('C:/Users/손병우/Desktop/Daedong_Mung!/data.csv', sep=',', na_rep='NaN',index=False)

data = pd.read_csv('./data.csv')
data['전화번호'] = phone_list