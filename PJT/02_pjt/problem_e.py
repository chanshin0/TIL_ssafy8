import requests
from pprint import pprint

def credits(title):
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
        
        #https://api.themoviedb.org/3/movie/{movie_id}/credits?api_key=57de5060634a5ea8e52134e23e6e8a4c&language=en-US
        path2 = f'/movie/{movie_id}/credits'
        query_string2 = {
            'api_key' : '57de5060634a5ea8e52134e23e6e8a4c',
            'language' : 'ko',
            'region' : 'KR',
        } 
        response2 = requests.get(BASE_URL + path2, params=query_string2).json()
        result2 = response2.get('cast')
        result3 = response2.get('crew')
        dict = {}
        cast_lst = []
        for i in result2:
            if i.get('cast_id') < 10:
                cast_lst.append(i.get('name'))
        direc_lst = []
        for i in result3:
            if i.get('department') == 'Directing':
                direc_lst.append(i.get('name'))
        dict.setdefault('cast', cast_lst)
        dict.setdefault('directing', direc_lst)

        return dict
    except Exception:
        return None
# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    제목에 해당하는 영화가 있으면 해당 영화 id를 통해 영화 상세정보를 검색하여 주연배우 목록(cast)과 스태프(crew) 중 연출진 목록을 반환
    영화 id 검색에 실패할 경우 None을 반환
    """
    pprint(credits('기생충'))
    # {'cast': ['Song Kang-ho', 'Lee Sun-kyun', ..., 'Jang Hye-jin'], 'crew': ['Bong Joon-ho', 'Park Hyun-cheol', ..., 'Yoon Young-woo']}
    pprint(credits('검색할 수 없는 영화'))
    # None
