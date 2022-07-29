import requests

def popular_count():
    BASE_URL = 'https://api.themoviedb.org/3' # 대문자 == 상수
    path = '/movie/popular'
    # 여기에 코드를 작성합니다.  
    # params는 보통 주소 ? 뒤에 있는 내용
    query_string = {
        'api_key' : '57de5060634a5ea8e52134e23e6e8a4c',
        'language' : 'ko',
        'region' : 'KR',
    }
    response = requests.get(BASE_URL + path, params=query_string).json()
    #print(response)  # response는 딕셔너리
    result = response.get('results') 
   
    return len(result)

    #print(result) # result는 리스트(api마다 다르게 응답이 오는데, 여기서는 리스트)

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    popular 영화목록의 개수 반환
    """
    print(popular_count())
    # 20
