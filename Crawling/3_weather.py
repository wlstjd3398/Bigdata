"""
날짜 : 2021/06/07
이름 : 김철학
내용 : 파이썬 전국 날씨 데이터 크롤링 실습


"""
# bs4 = beautifulsoup 패키지설치


import requests as req

from bs4 import BeautifulSoup as bs

# 페이지 요청(네이버뉴스 헤드라인)
response = req.get('https://news.naver.com/', headers={'User-Agent': 'Mozilla/5.0'})
#print(response.text)

# 페이지 파싱 dom = document object model
dom = bs(response.text, 'html.parser')
titles = dom.select('#today_main_news > div.hdline_news > ul > li > div.hdline_article_tit > a')
#print(titles)

# 파싱 데이터 출력(strip : 공백제거)
for tit1 in titles:
    print(tit1.next.strip())


# 다음 뉴스 랭킹 1 ~ 10 출력하기


resp = req.get('http://news.daum.net/ranking/popular')

dom = bs(resp.text, 'html.parser')
news_tits = dom.select('#mArticle > div.rank_news > ul.list_news2 > li:nth-child(n) > div.cont_thumb > strong > a')

#print(news.tits)

for i in range(10):
    print(news_tits[i].text)

