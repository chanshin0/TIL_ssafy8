T = int(input())
for tc in range(T):
    N = int(input())
    box_lst = [] # 박스 모서리 정보를 리스트로 담음
    for _ in range(N):
       box_lst.append(list(map(int, input().split())))

    inner_box = []
    # 입력된 박스 하나씩 꺼내서
    for i in box_lst:
        for j in range(i[0], i[2]+1): #행
            for k in range(i[1], i[3]+1): #열
                inner_box.append([j,k])

    violet = [] # 겹치는 영역 리스트
    for i in inner_box:
        if inner_box.count(i) == 1: # 겹치는 영역이 없다면 패스
            pass
        else:
            violet.append(i)

    # violet에는 겹치는 영역만 담겼기 떄문에 1/2한 뒤 출력
    print(f'#{tc+1} {int(len(violet)/2)}')




# 찾아야할 지점. 
# 좌표 싹 리스트 만들어서 일치되는 것만 뽑느 함수 만들고
# 다시 집어넣어서 일치하는 거 제외해서 최종 답

# def violet ():


