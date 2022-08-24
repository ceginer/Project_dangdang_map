# <1. 방식> 모든 제목&리뷰 검사 -> 리뷰 '동반' 검사 -> 그것의 제목&리뷰 나타내기
# <2. 속도> 훨씬 빨라짐 (강릉 기준 약 8~9초 걸림)
# <3. 지역 선택> input 통해 지역 입력시 해당하는 구글 검색페이지 이동
# <4. csv 저장> 7페이지 까지 csv 저장


from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import chromedriver_autoinstaller
import subprocess

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import csv

subprocess.Popen(r'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe --remote-debugging-port=9222 --user-data-dir="C:\chrometemp"') # 디버거 크롬 구동

option = Options()
option.add_experimental_option("debuggerAddress", "127.0.0.1:9222")

chrome_ver = chromedriver_autoinstaller.get_chrome_version().split('.')[0]
try:
    driver = webdriver.Chrome(f'./{chrome_ver}/chromedriver.exe', options=option)
except:
    chromedriver_autoinstaller.install(True)
    driver = webdriver.Chrome(f'./{chrome_ver}/chromedriver.exe', options=option)
driver.implicitly_wait(10)



# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time
# import csv
# # "&sa=N&ved=2ahUKEwjXosiFwK35AhUWmFYBHRdVA1AQ8tMDegUIAxCdAg"

# options = webdriver.ChromeOptions()
# options.add_experimental_option("excludeSwitches", ["enable-logging"])
# driver =webdriver.Chrome("./chromedriver", options=options)



def crawl():
  url = "https://www.google.com/search?q="+query+' 애견동반 카페'+"&newwindow=1&tbm=lcl&sxsrf=ALiCzsbVCyPLmiOJs7RCE3tAYtQBG1I-Ow:1659626914458&ei=ouXrYtfJG5aw2roPl6qNgAU&start="+str(urlnum)
  # url = "https://www.google.com/search?q="+query+'+강아지 여행지'+ '&newwindow=1&biw=1536&bih=720&sz=0&tbm=lcl&sxsrf=ALiCzsa8K31yYWJLMLLFidIYIjZl5n3nCw%3A1660362928046&ei=sCD3YvyeAoyz2roPwsa4kAU&oq='+query+'#rlfi=hd:;si:;;start:'+str(urlnum)
  driver.get(url)
  driver.implicitly_wait(5)
  time.sleep(2)
  
  search_list=[]
  search_raw = driver.find_elements(By.CLASS_NAME, 'OSrXXb' )

  for i in search_raw:
    search = i.text
    search_list.append(search)

  num =0
  
  for i in search_list:
    if ('동반' in i) or ('강아지' in i):
      if ('"' in i):
        # search_list[num-1] = 카페 이름
        # i = 후기
        try:
          print(search_list[num-1])
          print(i)
          csvWriter.writerow([search_list[num-1],query,i]) # csv 한 행씩 저장
        except:
          print('이모지')
          print(search_list[num-1])
          print(i)
          csvWriter.writerow([search_list[num-1],query,''])
        results.append([search_list[num-1],query,i])
      
    num += 1

  
###############################################
import pandas as pd
import os
import emoji 

urlnum=0
results = []

# 저장할 파일 지정
f = open(r"C:/Users/손병우/Desktop/Daedong_Mung!/withdog.csv", 'a', encoding='cp949', newline='')
csvWriter = csv.writer(f)
# csvWriter.writerow(['카페장소','리뷰','전화번호']) # csv 한 행씩 저장


# 지역 선택

location_list = ['부산']
# ['서울','경기','인천','강원','충북','충남','대전','세종','전북','전남','광주','경북','경남','대구','울산','부산','제주']
# '전북','전남','광주','대구','울산'
# '서울','경기','인천'
# '강원','충북','충남
# '대전','세종','전북'
# '전남','광주','경북'
# '경남','대구','울산'
# '부산','제주'

# 페이지 7번 크롤링
for j in location_list:
  query = j
  for i in range(5):
    crawl()
    urlnum += 20
  time.sleep(2)

f.close()
print('Rmx')

# 닫기
# f.close()

# 판다스 이용
# df = pd.DataFrame(results) # results = [[이름,지역], [이름,지역],....]
# df.columns=['카페 장소', '지역','리뷰']  # header부분
# csv_url = 'C:/Users/손병우/Desktop/Daedong_Mung!/test.csv'
# if not os.path.exists(csv_url):
#     df.to_csv(csv_url, index=False, mode='w', sep=',', na_rep='NaN', encoding='cp949')
# else:
#     df.to_csv(csv_url, index=False, mode='a', sep=',', na_rep='NaN', encoding='cp949', header=False)



