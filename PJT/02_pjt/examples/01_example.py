# requests 사용 예시 1

import requests


URL = 'https://dog.ceo/api/breeds/image/random'

response = requests.get(URL).json() # requests의 get 메서드
# 요청 방식
# Get, Post .... Delete, Put
# Get
# 데이터 조회 = 주소창에 데이터를 넣는 방식
# Post
# 데이터 변경 -> DB에 영향이 있는 경우 / 주소창에 데이터가 표시되지 않음(데이터를 숨기고 싶을 떄)
print(response)

results = response.get('message') # 딕셔너리(JSON)의 get 메서드
print(results)
