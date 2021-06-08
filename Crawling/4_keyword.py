"""
날짜 : 2021/06/08
이름 : 김철학
내용 : 파이썬 zum 이슈 트렌드 실시간 검색어 크롤링 실습

"""
import os

import requests as req
from bs4 import BeautifulSoup as bs

from datetime import datetime

# 페이지 요청하기
response = req.get('https://issue.zum.com/')
#print(response.text)

# 데이터 파싱하기
dom = bs(response.text, 'html.parser')
divs =  dom.select('#issueKeywordList > li > div.cont')

# 데이터 출력하기
for div in divs:
    rank = div.find(class_='num').text
    word = div.find(class_='word').text

    print('%s, %s' %(rank, word))




 # 디렉터리 생성
dir = "./keyword/{:%Y-%m-%d}".format(datetime.now())

if not os.path.exists(dir):
        # 경로에 해당 디렉터리가 존재하지 않으면 날짜기반으로 디렉터리 만든다
        os.makedirs(dir)

# 데이터 파일 생성
fname = "{:%Y-%m-%d-%H-%M.txt}".format(datetime.now())
file = open(dir+'/'+fname, mode='w', encoding='utf-8')

# 데이터 파일 저장, rank[:-1] 마지막숫자 뒤부터
for div in divs:
    rank = div.find(class_='num').text
    word = div.find(class_='word').text
    file.write('%s, %s\n' %(rank[:-1], word))


    # 파일 닫기
file.close()
print('실시간 검색어 수집완료!')

