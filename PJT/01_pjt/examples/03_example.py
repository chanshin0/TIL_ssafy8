# open 및 json 모듈 사용예시

import json
from pprint import pprint

lista = [[1, 2, 3], [1, 2, 3], [1, 2, 3]]

movie = open('sample.json', encoding='utf-8')
movie_detail = json.load(movie)
# pprint(movie_detail)
# print(movie_detail)
pprint(lista)
print(lista)
