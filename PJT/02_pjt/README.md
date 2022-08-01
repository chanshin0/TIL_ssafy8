1. problem_a.py
   
   request모듈을 불러온뒤 get요청을 통해(api key활용)
   
   TMDB의 데이터를 불러오는 과정을 연습할 수 있었다.

2. problem_b.py
   
   a에서 불러온 데이터를 간단한 조건문으로 처리하여 출력하는 연습을 할 수 있었다.

3. problem_c.py
   
   리스트 안에 들어있는 딕셔너리를 특정 key값의 value를 기준으로 정렬할 때,
   
   sorted함수의 parameter에 람다함수를 집어넣어 해결하는 방법을 배웠다.
   
   ```
   sorted_lst = sorted(result, key=lambda x : x.get('vote_average'), reverse=True)
   ```

4. problem_d.py
   
   get요청을 한번 해서 특정 값에 접근한 뒤 이를 변수에 담고,
   
   그 변수를 활용해서, 다른 데이터에 재차 get요청을 하는 과정을 연습했다.
   
   원하는 데이터가 출력되도록 처리한 뒤, try와 except문을 활용해 예외처리하는 과정을 연습했다.

5. problem_e.py
   
   마찬가지로 get요청을 두번 해서 원하는 값에 접근했고, 형변환과 조건문을 통해 출력을 맞춘 뒤 예외처리해서 문제를 풀이 했다.



새로 배운 부분.

    get과 post에 대한 간락한 이해

    Get

    데이터 조회 = 주소창에 데이터를 넣는 방식

    Post

    데이터 변경 -> DB에 영향이 있는 경우 / 주소창에 데이터가 표시되지 않음(데이터를 숨기      고 싶을 때)

    api key를 받아서 request.get() 메서드를 활용해 DB에 데이터를 불러오는 방법.

    웹페이지의 설명을 보면서 괄호 안에 들어갈 url을 알맞게 작성하는 법.

    리스트 안의 딕셔너리를 그 내부의 특정한 값을 기준으로 정렬하는 방법(parameter에     람다함수)

    try-except문을 활용해 예외처리하는 방법.
