import requests
import json
from funcs import speak

# 날씨 클래스
class Climate:
    location = {
        '서울' : {'lat' : 37.566, 'long' : 126.9784},
        '런던' : {'lat' : 51.5085, 'long' : -0.1257},
        '뉴욕' : {'lat' : 40.7143, 'long' : -74.006},
        '포항' : {'lat' : 36.8144, 'long' : 128.1211}
        }

    # 포항 날씨 조회
    def searching(self):
        response = requests.get(f'https://api.open-meteo.com/v1/forecast?latitude={self.location["포항"]["lat"]}&longitude={self.location["포항"]["long"]}&current_weather=true')
        
        # response 로 얻어온 json을 파이썬이 사용할 수 있도록 변경
        data = json.loads(response.text)
        self.printing('포항', data['current_weather']['temperature'])
    
    # 날씨 프린트
    def printing(self, loc, temp):
        print('')
        print('=' * 45)
        print(f'{loc}날씨는 {temp}도 입니다.')
        speak(f'{loc}날씨는 {temp}도 입니다.')
        print('')
    