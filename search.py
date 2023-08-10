import time
from selenium import webdriver
from selenium.webdriver.common.by import By

# 검색 클래스
class Search:
    # 인스턴스 생성하며 단어 입력
    def __init__(self, word):
        self.word = word

    # 단어 검색
    def searching(self):
        # selenium이 작동할 때 크롬이라는 웹브라우저를 사용
        driver = webdriver.Chrome()
        # 크롬 브라우저를 통해, 주소로 접근
        driver.get('https://www.naver.com/')

        search_input = driver.find_element(By.CSS_SELECTOR, '#query')
        search_input.send_keys(self.word)

        search_button = driver.find_element(By.CSS_SELECTOR, '#search-btn')
        search_button.click()

        time.sleep(10)

        driver.quit()