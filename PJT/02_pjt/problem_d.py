import requests
from pprint import pprint


def recommendation(title):
    try:
        BASE_URL = 'https://api.themoviedb.org/3'
        # https://api.themoviedb.org/3/search/movie?api_key=<<api_key>>&language=en-US&page=1&include_adult=false
        path = '/search/movie'
        query_string = {
            'api_key' : '57de5060634a5ea8e52134e23e6e8a4c',
            'language' : 'ko',
            'region' : 'KR',
            'query' : title
        } 
        response = requests.get(BASE_URL + path, params=query_string).json()
        result = response.get('results')
        movie_id = result[0].get('id')

        #https://api.themoviedb.org/3/movie/496243/recommendations?api_key=57de5060634a5ea8e52134e23e6e8a4c&language=en-US&page=1
        path = f'/movie/{movie_id}/recommendations'
        query_string = {
            'api_key' : '57de5060634a5ea8e52134e23e6e8a4c',
            'language' : 'ko',
        } 
        response = requests.get(BASE_URL + path, params=query_string).json()
        result = response.get('results')
        result_lst = []
        for i in range(len(result)):
            result_lst.append(result[i]['title'])
        
        return result_lst
    
    except Exception:
        return None
    
# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    제목에 해당하는 영화가 있으면 해당 영화의 id를 기반으로 추천 영화 목록 구성
    추천 영화가 없을 경우 []를 반환
    영화 id 검색에 실패할 경우 None을 반환
    (주의) 추천 영화의 경우 아래 예시 출력과 차이가 있을 수 있음
    """
    pprint(recommendation('기생충'))
    # ['조커', '1917', '조조 래빗', ..생략.., '살인의 추억', '펄프 픽션']
    pprint(recommendation('그래비티'))
    # # []
    pprint(recommendation('검색할 수 없는 영화'))
    # None
