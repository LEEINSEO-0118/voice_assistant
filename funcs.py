import speech_recognition as sr
from gtts import gTTS 
import playsound
import os

# 음성 인식 및 말하기 파일

# stt 인식을 위한 객체 생성
r = sr.Recognizer()
# 마이크 사용을 위한 객체 생성
mic = sr.Microphone()

# 비서 부르기
def assistant_check():
    with mic as source: # 마이크에 담긴 소리를 토대로 아래 코드 실행
        print('인식 중...')
        audio = r.listen(source) # 해당 소리를 오디오 파일 형태로 변환
        try:
            result = r.recognize_google(audio, language = "ko-KR") # 오디오를 토대로 음성 인식
            print('인식 :', result)
            if result in ['비서야', '비서', '종료']:
                return result
            else:  
                # 비서 or 종료 가 아닌 경우 다시 음성 인식을 받도록
                return False
        # 에러를 발생하지 않고 음성 인식을 무한 대기
        except sr.UnknownValueError:
            # print("음성 인식 실패")
            return 0
        except sr.RequestError:
            # print("서버 에러 발생")
            return 0
        except sr.WaitTimeoutError:
            # print("인식 실패")
            return 0

# 첫 음성을 통해, 메뉴와 주제를 분리
def menu_to_text():
    with mic as source: # 마이크에 담긴 소리를 토대로 아래 코드 실행
        print('인식 중...')
        audio = r.listen(source) # 해당 소리를 오디오 파일 형태로 변환
        try:
            result = r.recognize_google(audio, language = "ko-KR") # 오디오를 토대로 음성 인식
            print('인식 :', result)
            words = result.split()
            menu = find_menu(words)
            topic = get_topic(words, menu)
            return menu, topic
        except sr.UnknownValueError:
            # print("음성 인식 실패")
            return 0, 0
        except sr.RequestError:
            # print("서버 에러 발생")
            return 0, 0
        except sr.WaitTimeoutError:
            # print("인식 실패")
            return 0, 0
    
    

menu_list = ['검색', '검색해', '날씨', '미세먼지', '미세', '종료', '게임', '끝말잇기','축구']

# 음성에서 메뉴 찾기
def find_menu(words):
    for word in words:
        if word in menu_list:
            return word
        else:
            pass
    

# 음성에서 주제 찾기
def get_topic(words, menu):
    if menu in menu_list:
        menu_loc = words.index(menu)
        topics = [words[i] for i in range(0, menu_loc)]
        topic = ' '.join(topics)
        return topic
    else:
        pass


# 문자를 스피커로
def speak(text): 
	tts = gTTS(text=text, lang='ko') # 함수 인자로 들어온 text 를 음성으로 변환
	tts.save('voice.mp3') # 변환된 음성을 voice.mp3 라는 이름으로 저장
	playsound.playsound('voice.mp3') # 저장한 음성 파일을 재생
	os.remove('voice.mp3') # 재생 후에는 해당 파일 삭제

# 끝말잇기 단어 음성 입력 
def game_input():
    with mic as source: # 마이크에 담긴 소리를 토대로 아래 코드 실행
        print('인식 중...')
        audio = r.listen(source) # 해당 소리를 오디오 파일 형태로 변환
        try:
            result = r.recognize_google(audio, language = "ko-KR") # 오디오를 토대로 음성 인식
            print('인식 :', result)
            return result
        # 에러를 발생하지 않고 음성 인식을 무한 대기
        except sr.UnknownValueError:
            # print("음성 인식 실패")
            return 0
        except sr.RequestError:
            # print("서버 에러 발생")
            return 0
        except sr.WaitTimeoutError:
            # print("인식 실패")
            return 0