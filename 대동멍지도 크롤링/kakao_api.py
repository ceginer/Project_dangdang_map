import requests 
import csv
import os
url = 'https://dapi.kakao.com/v2/local/search/keyword.json' 

locationList = ['서울','경기','인천','강원','충북','충남','대전','세종','전북','전남','광주','경북','경남','대구','울산','부산','제주']
place_name=[]
yes=0
value=0
# locationList=['통영 애견동반 펜션']


if not os.path.exists('C:/Users/손병우/Desktop/Daedong_Mung!/test.csv'):
    f = open(r'C:/Users/손병우/Desktop/Daedong_Mung!/onlydog.csv', 'w', encoding='cp949', newline='')

csvWriter = csv.writer(f)

def num_place(region,page_num):
    url = 'https://dapi.kakao.com/v2/local/search/keyword.json'
    params = {'query': region+' 애견카페','page': page_num}
    headers = {"Authorization": "KakaoAK 7aeccc3c69f4ba6ee437bd9852a66879"}

    places = requests.get(url, params=params, headers=headers).json()['documents']
    total = requests.get(url, params=params, headers=headers).json()['meta']['total_count']
    
    value = total // 15 
    value += 1

    if total > 45:
        print(total,'개 중 45개 데이터밖에 가져오지 못했습니다!')
        yes=0
        
    else :
        print('모든 데이터를 가져왔습니다!')
        yes=1

    for place in places:
        csvWriter.writerow([place['place_name'],region])    


for loc in locationList:
    # 1부터 value 페이지 까지
    if value <= 3:
        for page in range(1,4):
            num_place(loc,page)
    if value > 3:
        for page in range(1,4):
            num_place(loc,page)

f.close()
