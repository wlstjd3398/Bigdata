"""
날짜 : 2021/06/08
이름 : 김철학
내용 : 가상 브라우저를 활용한  네이버 영화 평점리뷰 크롤링 실습
"""

from selenium import webdriver

# 가상 브라우저 실행
browser = webdriver.Chrome('./chromedriver.exe')

# 페이지 이동
browser.get('https://movie.naver.com/')

# 영화 랭킹 클릭
btn_ranking = browser.find_elements_by_css_selector('#scrollbar > div.scrollbar-box > div > div > ul > li:nth-child(3) > a')
btn_ranking.click()


# 평점순 클릭
btn_score = browser.find_element_by_css_selector('')
btn_score.click()

# 순위별 영화 클릭
titles = browser.find_element_by_css_selector('#old_content > table > tbody > tr > td.title > div > a')
titles[0].click()

# 영화 평점 클릭
menu_score = browser.find_element_by_css_selector('')
menu_score.click()

# 현재 가상 브라우저를 영화리뷰가 있는 iframe으로 전환
browser.switch_to.frame('pointAfterListIframe')

# 영화 리뷰 출력
lis = browser.find_elements_by_css_selector('body > div > div > div.score_result > ul > li')


for li in lis:
    score = li.find_element_by_css_selector('div.star_score > em').text
    reple = li.find_element_by_css_selector('').text

    print('{},{}'.format(score, reple))

    