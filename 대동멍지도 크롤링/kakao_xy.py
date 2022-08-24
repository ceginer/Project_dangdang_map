import requests 
import csv
import os
import time
address_list=[]
dict=[]
def xy(query):
    url = 'https://dapi.kakao.com/v2/local/search/address.json'
    params = {'query': query}
    headers = {"Authorization": "KakaoAK 7aeccc3c69f4ba6ee437bd9852a66879"}

    places = requests.get(url, params=params, headers=headers).json()['documents']
    if places:
        dict.append(places[0]['x'])
        dict.append(places[0]['y'])
    else:
        dict.append('1')
        dict.append('1')


with open('C:/Users/손병우/Desktop/data/place_edit_fin.csv','r',encoding='cp949') as f:
    with open('C:/Users/손병우/Desktop/data/place_edit_result.csv', 'w',encoding='cp949') as ff:
        csvReader = csv.reader(f)
        csvWriter = csv.writer(ff)
        i=0
        for row in csvReader:
            dict=[]
            if row[2]:
                xy(row[2])
            try:
                if dict[0] != '1':
                    csvWriter.writerow([row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],dict[1],dict[0]])
            except:
                print('noooooooo')
            print(i)
            i+=1

