import csv
import os
import pandas as pd

pension_name_list=[]
big_location_list=[]
location_list=[]
phone_list=[]
type_list=[]
url_list=[]
desc_list=[]
img_list=[]
mapx_list=[]
mapy_list=[]
# csv 파일의 1행(카페이름) 읽기
file_dir = 'C:/Users/손병우/Desktop/Daedong_Mung!/pension_edit_fin.csv'
with open(file_dir,'r', encoding='CP949') as csvfile:
  reader = csv.reader(csvfile, skipinitialspace =True)
  for row in reader:
    if row[0]:
      pension1=row[0]
    if row[1]:
      pension2=row[1]
    if row[2]:
      pension3=row[2]

    if not ''.join(row[3]).strip():
      pension4=''
    else:
      pension4=row[3]

    if not ''.join(row[4]).strip():
      pension5=''
    else:
      pension5=row[4]

    if not ''.join(row[5]).strip():
      pension6=''
    else:
      pension6=row[5]

    if not ''.join(row[6]).strip():
      pension7=''
    else:
      pension7=row[6]

    if not ''.join(row[7]).strip():
      pension8=''
    else:
      pension8=row[7]

    if not ''.join(row[8]).strip():
      pension9=''
    else:
      pension9=row[8]

    if row[9]:
      pension10=row[9]

    pension_name_list.append(pension1)
    big_location_list.append(pension2)
    location_list.append(pension3)

    if not pension4:
      phone_list.append('')
    else:
      phone_list.append(pension4)
    
    if not pension5:
      type_list.append('')
    else:
      type_list.append(pension5)

    if not pension6:
      url_list.append('')
    else:
      url_list.append(pension6)

    if not pension7:
      desc_list.append('')
    else:
      desc_list.append(pension7)

    if not pension8:
      img_list.append('')
    else:
      img_list.append(pension8)
  
    mapx_list.append(pension9)
    mapy_list.append(pension10)

print(phone_list)
# (선희) csvWriter는 여기서 열어야 해! for문 밖에서
ff = open(r'C:/Users/손병우/Desktop/Daedong_Mung!/penseion_edit_fin_edit.csv', 'w', encoding='CP949', newline='')
csvWriter = csv.writer(ff)

locationList = ['서울','경기','인천','강원','충청북도','충청남도','대전','세종','전라북도','전라남도','광주','경상북도','경상남도','대구','울산','부산','제주']
# locationList = ['서울']

for i in range(len(pension_name_list)):
  if '펜션' in pension_name_list[i]:
    if ('강아지' in desc_list[i]) or ('애견' in desc_list[i]) or ('반려견' in desc_list[i]) or ('반려동물' in desc_list[i]) or ('형견' in desc_list[i]):
      order = location_list[i]
      for loc in locationList:
        if loc in order:
          location = loc 
        elif '충청북도' in order:
            location = '충북'
        elif '충청남도' in order:
            location = '충남'
        elif '전라북도' in order:
            location = '전북'
        elif '전라남도' in order:
            location = '전남'
        elif '경상북도' in order:
            location = '경북'
        elif '경상남도' in order:
            location = '경남'
      csvWriter.writerow([pension_name_list[i], location, location_list[i],phone_list[i],'펜션',url_list[i],desc_list[i],img_list[i], mapx_list[i], mapy_list[i]])
      
ff.close()

