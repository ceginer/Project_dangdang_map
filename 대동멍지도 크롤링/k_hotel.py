import requests 
import csv
import os
import time
address_list=[]
dict=[]
def xy(query, page):
    url = 'https://dapi.kakao.com/v2/local/search/keyword.json'
    params = {'query': query, 'page' : page}
    headers = {"Authorization": "KakaoAK 7aeccc3c69f4ba6ee437bd9852a66879"}

    result = requests.get(url, params=params, headers=headers).json()
    return result

list=[]
loc_list=[]
page = 1
locationList = ['서울','경기','인천','강원','충북','충남','대전','세종','전북','전남','광주','경북','경남','대구','울산','부산','제주']

f = open(r'C:/Users/손병우/Desktop/crawl/k_location_hotel.csv','w',encoding="cp949",newline='')
writer = csv.writer(f)

while page <= 7:
    try :
        result = xy('애견동반 호텔', page)
        for document in result['documents']:
            name = document['place_name']
            list.append(name)
            address = document['address_name']
            location='기타'
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
            loc_list.append(location)
            # writer.writerow([name])
        if result['meta']['is_end'] is True : break
        page +=1
    except:
        break
for i,j in zip(list,loc_list):
    writer.writerow([i,j])
f.close()
