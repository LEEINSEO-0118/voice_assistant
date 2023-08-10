import requests
import json

# 단어 관련 함수들
class Word:
     
    params = {
        'key' : 'BD9C0CDE7F474D08DFAFA6D4550BB831',
        'q' : '검색어',
        'req_type' : 'json',
        'start': 1,
        'num' : 100,
        'part' : 'word',
        'sort' : 'dict',
        'advanced' : 'y',
        'type1' : ['word'],
        'method' : 'start',
        'letter_s' : 2
    }

    # 마지막 한 글자 찾기
    def get_last_spell(self, word):
        return word[-1]
        
    
    # 첫 글자 찾기 및 단어 중복 검정
    def user_word_judge(self, word, last_spell, user_answered):
        if last_spell == word[0]:
            if word not in user_answered:
                return True
        elif word == '몰라':
            return True
        else:
            return False
    
    # 컴퓨터 대답 찾기
    def reflect_word(self, first_spell, comp_answered):
        data = self.request_func(first_spell)

        # 아이템 리스트
        item_list = data['channel']['item']
        
        words = self.get_words(item_list)
        return self.get_one_word(words, comp_answered)

    # 아이템 리스트에서 - 문자 정제
    def get_words(self, items):
        words = []
        for item in items:
            word = item['word']
            if '-' in word:
                non_space = word.replace('-','')
                if self.len_check(non_space):
                    words.append(non_space)
            else:
                if self.len_check(word):
                    words.append(word) 
        return list(set(words))
    
    # 여러 단어 리스트 중 하나 골라오기
    def get_one_word(self, words, comp_answered):
        for word in words:
            if word not in comp_answered:
                return word
        return 'lose'

    
    # 단어 길이 체크
    def len_check(self, word):
        if len(word) >=2:
            return True
        else:
            return False
        
    # 사용자 단어 유의성 체크(글자수, 사전 등록 유무)
    def word_check(self, word):
        data = self.request_func(word)
        # 아이템 리스트
        if (data['channel']['total']) >= 1:
            return True
        else:
            return False
    
    # api 요청 및 얻은 json을 사용할 수 있는 data로 변환
    def request_func(self, word):
        self.params['q'] = word
        response = requests.get(f'https://opendict.korean.go.kr/api/search', params = self.params, verify=False)
        # response 로 얻어온 json을 파이썬이 사용할 수 있도록 변경
        data = json.loads(response.text)

        return data

