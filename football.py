import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
from funcs import speak

# 축구 순위 크롤링
class FootBall:
    # 셀리니움 통한 html 추출
    def searching(self):
        # 옵션을 통해 크롬창을 띄우지 않고 백그라운드에서 크롤링 가능
        options = webdriver.ChromeOptions()
        options.add_argument('headless')
        driver = webdriver.Chrome(options=options)
        # 크롬 브라우저를 통해, 주소로 접근
        driver.get('https://sports.news.naver.com/wfootball/record/index?category=epl&year=2022&tab=team')
        
        html = driver.page_source
        soup = BeautifulSoup(html, 'html.parser')

        league_name = '프리미어리그'
        season = soup.select('#_currentYearButton > em')[0].text.replace('선택된 시즌', '')
        rank_list = soup.select('#wfootballTeamRecordBody > table > tbody > tr > td.align_l > div > span.name')

        driver.quit()
        self.parsing(league_name, season, rank_list)
        
    # html 데이터를 통한 파싱 및 프린트
    def parsing(self, league_name, season, rank_list):
        top4 = []
        for i in range(4):
            team = rank_list[i].text
            top4.append({'rank' : i + 1, 'team' : team })
        
        print('')
        print('=' * 45)
        print(f'{season} {league_name} 순위')
        speak(f'{season} {league_name} 순위 입니다.')

        for top in top4:
            print(f'{top["rank"]}위 {top["team"]}')
            speak(f'{top["rank"]}위 {top["team"]}')
        print('')
