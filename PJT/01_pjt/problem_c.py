import json
from pprint import pprint


def movie_info(movies, genres):
    for movie in movies:
        genre_ids = movie.get('genre_ids')
        genres_name = []
        result_list = []
        result = {}
        for genre_id in genre_ids:
            for genre in genres:
                if genre.get('id') == genre_id:
                    genres_name.append(genre.get('name'))
        result['genres_name'] = genres_name
        result['id'] = movie.get('id')
        result['overview'] = movie.get('overview')
        result['poster_path'] = movie.get('poster_path')
        result['title'] = movie.get('title')
        result['vote_average'] = movie.get('vote_average')
        print(result)
        result_list.append(result)
        return result_list

              
        
        
# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movies_json = open('data/movies.json', encoding='utf-8')
    movies_list = json.load(movies_json)

    genres_json = open('data/genres.json', encoding='utf-8')
    genres_list = json.load(genres_json)

    pprint(movie_info(movies_list, genres_list))
