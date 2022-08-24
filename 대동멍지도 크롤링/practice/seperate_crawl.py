from selenium import webdriver
import time

options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-logging"])
driver =webdriver.Chrome("./chromedriver", options=options)
driver.get("https://www.google.com/search?newwindow=1&tbs=lf:1,lf_ui:9&tbm=lcl&q=%EA%B0%95%EB%A6%89+%EC%95%A0%EA%B2%AC%EB%8F%99%EB%B0%98%EC%B9%B4%ED%8E%98")
driver.implicitly_wait(5) 
search = driver.find_elements_by_class_name('rllt__details')

for i in search:
  try:
    review = i.find_element_by_class_name('X0w5lc')
  except:
    continue
  title_review = i.find_elements_by_class_name('OSrXXb')
  if '동반' in title_review[1].text:
    print(title_review[0].text)
    print(title_review[1].text)
    


# 빠르게 하기 위해서 일단 리뷰 체크해서 리뷰 '동반' 들어가는 거 찾고 그 찾은것의 페이지만 빠르게 크롤링
# 하나하나 말고

# searchbox = driver.find_element_by_id('tsuid9').find_element_by_class_name('cXedhc')
# searchbox2 = searchbox.find_element_by_class_name('OSrXXb').text
#tsuid9 > div > div > div > a.vwVdIc.wzN8Ac.rllt__link.a-no-hover-decoration > div > div > div.dbg0pd.eDIkBe > span