"""
날짜 : 2021/06/07
이름 : 김철학
내용 : 파이썬 1시간마다 전국 날씨 데이터 크롤링 실습

"""
import os

import requests as req
from bs4 import BeautifulSoup as bs


from datetime import datetime


response = req.get('https://www.weather.go.kr/w/obs-climate/land/city-obs.do')
# print(response.text)

# 페이지 파싱
dom = bs(response.text, 'html.parser')
trs = dom.select('#weather_table > tbody > tr')

# 디렉터리 생성
dir = "./wea/{:%Y-%m-%d}".format(datetime.now())

if not os.path.exists(dir):
        # 경로에 해당 디렉터리가 존재하지 않으면 날짜기반으로 디렉터리 만든다
        os.makedirs(dir)

# 데이터 파일 생성
fname = "{:%Y-%m-%d-%H-%M.txt}".format(datetime.now())
file = open(dir+'/'+fname, mode='w', encoding='utf-8')

# 데이터 파일 저장
file.write('지역,현재일기,현재기온,불쾌지수,일강수,습도,풍향\n')
for i, tr in enumerate(trs):
    tds = tr.find_all('td')
    file.write("{},{},{},{},{},{},{}\n".format(tds[0].text if tds[0].text.strip() else 'NA',
                                                  tds[1].text if tds[1].text.strip() else 'NA',


                                                  tds[5].text if tds[5].text.strip() else 'NA',

                                                  tds[7].text if tds[7].text.strip() else 'NA',
                                                  tds[8].text if tds[8].text.strip() else 'NA',
                                                  tds[9].text if tds[9].text.strip() else 'NA',
                                                  tds[10].text if tds[10].text.strip() else 'NA',))

# 파일 닫기
file.close()
print('날씨 데이터 수집완료!')





