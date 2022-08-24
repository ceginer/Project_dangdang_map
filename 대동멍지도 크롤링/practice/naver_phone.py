from urllib import request
from winreg import REG_QWORD
import requests
from bs4 import BeautifulSoup as bs

##### 네이버 맵 페이지

place = input('장소 이름')
url = "https://map.naver.com/v5/search/"+place+"/place/1270162518?c=14354407.1975116,4547279.3331188,13,0,0,0,dh&isCorrectAnswer=true"
response = requests.get(url)
soup = bs(response.text, 'html.parser')


starpoint = soup.select_one('._20Ivz ._1Y6hi em')
detail_page = soup.select_one('#_title a')['href']
raw_phone = soup.select_one('.place_section_content ._3ZA0S').text
address = soup.select_one('._2yqUQ').text

print(raw_phone, starpoint, detail_page, address)













####### 지역 + 장소이름 + 전화번호 형태로 할 것.
##### 네이버 본페이지
# place = input('장소 이름')

# url = "https://search.naver.com/search.naver?sm=tab_hty.top&where=nexearch&query="+place+'전화번호'
# response = requests.get(url)
# soup = bs(response.text, 'html.parser')


# starpoint = soup.select_one('._20Ivz ._1Y6hi em')
# detail_page = soup.select_one('#_title a')['href']
# raw_phone = soup.select_one('.place_section_content ._3ZA0S').text
# address = soup.select_one('._2yqUQ').text

# print(raw_phone, starpoint, detail_page, address)

