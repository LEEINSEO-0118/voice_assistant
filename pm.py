import requests
import json
from funcs import speak

# 미세먼지 클래스
class PM:
    # 파라미터
    params = {
        'serviceKey': 'pyStQ7xmD2LHG2Q37jpasMCRPDu565rvMioWtiY8y1MEMu3BKynLI7sy8ogkAFuCvNJ/P4C/sxF24AvNr6cwTg==',
        'returnType': 'json',
        'numOfRows': '100',
        'pageNo': '1',
        'sidoName': '경북',
        'ver': '1.0'
    }
    
    # 미세먼지 정보 받아오기
    def searching(self):
        response = requests.get('http://apis.data.go.kr/B552584/ArpltnInforInqireSvc/getCtprvnRltmMesureDnsty', params = self.params)
        data = json.loads(response.text)

        airinfo_list = data['response']['body']['items']

        result = []

        # 여러 관측소 중 '연일읍' 관측소 찾기
        for airinfo in airinfo_list:
            if airinfo['stationName'] == '연일읍':
                result.append(['포항', airinfo['pm10Value'], airinfo['pm25Value']])
                break

        self.printing(result[0][0], result[0][1], result[0][2])
    
    # 미세먼지 프린트
    def printing(self, loc, pm10, pm25):
        print('')
        print('=' * 45)
        print(f'{loc} 미세먼지 수치 입니다.\n미세먼지 수치{pm10}, 초미세먼지 수치{pm25}')
        speak(f'{loc} 미세먼지 수치 입니다. 미세먼지 수치는{pm10}이며 초미세먼지 수치는{pm25}입니다.')
        print('')