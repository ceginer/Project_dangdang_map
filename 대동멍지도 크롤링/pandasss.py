import pandas as pd
data = pd.read_csv('C:/Users/손병우/Desktop/crawl/hotel_person.csv',encoding="cp949",header=None,names=['지역','주소','전화번호','카테고리','상세링크','설명','메인이미지','mapx','mapy'])
data.index.name='이름'





data['star']= 
data.to_csv("C:/Users/손병우/Desktop/panss.csv",encoding="cp949")