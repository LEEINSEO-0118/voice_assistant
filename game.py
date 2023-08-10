from funcs import speak
from funcs import game_input
from word import Word

class Game:

    # 단어 api 사용 함수들
    word_func = Word()

    # 말했던 단어 저장
    user_answered = []
    comp_answered = []


    # 게임 시작 함수
    def start(self):
        print('')
        print('=' * 45)
        print('끝말잇기 게임을 시작합니다.')
        speak('끝말잇기 게임을 시작합니다.')

        print('단어를 이야기 해주세요.')
        speak('단어를 이야기 해주세요.')
    
        # 사용자 단어 입력
        while 1:
            user_input = game_input()
            # user_input = input('입력하세요 : ')
            if user_input:
                # 사전에 있는 단어인지 확인
                if self.word_func.word_check(user_input):
                    break
                else:
                    print('사전에 없는 단어 입니다.')
                    speak('사전에 없는 단어 입니다. 다시 입력해주세요.')
        # 단어가 입력되면 리스트에 저장
        self.user_answered.append(user_input)
        # 마지막 글자 추출
        last_spell = self.word_func.get_last_spell(user_input)

        # 첫번쨰 컴퓨터 차례부터 무한 루프 시작
        while 1:
            # 컴퓨터의 단어 찾기
            comp = self.word_func.reflect_word(last_spell, self.comp_answered)

            # 컴퓨터 패배 시 무한 루프 종료
            if comp == 'lose':
                break
            # 컴퓨터 단어 등록
            else:
                self.comp_answered.append(comp)
                print(comp)
                speak(comp)

            # 컴퓨터 단어에서 마지막 글자 추출
            last_spell = self.word_func.get_last_spell(comp)
            print(f'\'{last_spell}\'자로 시작하는 단어를 말하세요. 모르면 \'몰라\'라고 말하세요.')
            speak(f'{last_spell}짜로 시작하는 단어를 말하세요. 모르면 \'몰라\'라고 말하세요.')

            # 사용자 단어 입력
            while 1:
                user_input = game_input()
                # 입력이 들어오면
                if user_input:
                    # 입력 단어 첫 글자 검정 및 중복성 검정
                    if self.word_func.user_word_judge(user_input, last_spell, self.user_answered):
                        break
                    else:
                        print(f'첫 글자가 틀립니다. \'{last_spell}\'자로 시작하는 단어를 말하세요. 모르면 \'몰라\'라고 말하세요.')
                        speak(f'첫 글자가 틀립니다. {last_spell}자로 시작하는 단어를 말하세요. 모르면 \'몰라\'라고 말하세요.')
            
            # 사용자 포기 시 무한 루프 종료
            if user_input == '몰라':
                break
            # 사용자 단어 등록
            else:
                self.user_answered.append(user_input)
                last_spell = self.word_func.get_last_spell(user_input)

        # 컴퓨터 패배 검정
        if comp == 'lose':
            print('컴퓨터 패배')
            print('')
            speak('제가 졌습니다.')

        # 사용자 패배 검정
        if user_input == '몰라':
            print('패배')
            speak('당신은 졌습니다.')
            print('')
