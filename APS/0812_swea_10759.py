# 색칠하기2
T = int(input())
for tc in range(1, T+1):
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

    non_violet = [] # 보라색 뺀 영역만 담긴 리스트
    for i in inner_box:
        if inner_box.count(i) == 1: # 겹치는 영역 없는 칸만 집어넣음
           non_violet.append(i)
            # [[2, 2], [2, 3], [2, 4], [3, 2], [4, 2], [3, 5], [3, 6], [4, 5], [4, 6], [5, 3],
            # [5, 4], [5, 5], [5, 6], [6, 3], [6, 4], [6, 5], [6, 6]]

    cnt = 0 # 외각이 아닌 면 개수 체크용 변수
    for i in non_violet: # 하나씩 꺼내서 외각에 해당하는 면 몇 개인지 체크
        if 0 < i[0] < 9 and 0 < i[1] < 9:
            if non_violet.count([i[0]+1, i[1]]) == 0 or non_violet.count([i[0]+1, i[1]]) > 1: # 아래쪽 체크 cnt+1
                cnt += 1
            if non_violet.count([i[0]-1, i[1]]) == 0 or non_violet.count([i[0]-1, i[1]]) > 1: # 위쪽 체크 cnt+1
                cnt += 1
            if non_violet.count([i[0], i[1]+1]) == 0 or non_violet.count([i[0], i[1]+1]) > 1: # 오른쪽 체크 cnt+1
                cnt += 1
            if non_violet.count([i[0], i[1]-1]) == 0 or non_violet.count([i[0], i[1]-1]) > 1: # 왼쪽 체크 cnt+1
                cnt += 1
        elif i[0] == 0:
            if non_violet.count([i[0]+1, i[1]]) == 0 or non_violet.count([i[0]+1, i[1]]) > 1: # 아래쪽 체크 cnt+1
                cnt += 1
            if non_violet.count([i[0], i[1]+1]) == 0 or non_violet.count([i[0], i[1]+1]) > 1: # 오른쪽 체크 cnt+1
                cnt += 1
            if non_violet.count([i[0], i[1]-1]) == 0 or non_violet.count([i[0], i[1]-1]) > 1: # 왼쪽 체크 cnt+1
                cnt += 1
        elif i[0] == 9:
            if non_violet.count([i[0]-1, i[1]]) == 0 or non_violet.count([i[0]-1, i[1]]) > 1: # 위쪽 체크 cnt+1
                cnt += 1
            if non_violet.count([i[0], i[1]+1]) == 0 or non_violet.count([i[0], i[1]+1]) > 1: # 오른쪽 체크 cnt+1
                cnt += 1
            if non_violet.count([i[0], i[1]-1]) == 0 or non_violet.count([i[0], i[1]-1]) > 1: # 왼쪽 체크 cnt+1
                cnt += 1
        elif i[1] == 0:
            if non_violet.count([i[0]+1, i[1]]) == 0 or non_violet.count([i[0]+1, i[1]]) > 1: # 아래쪽 체크 cnt+1
                cnt += 1
            if non_violet.count([i[0]-1, i[1]]) == 0 or non_violet.count([i[0]-1, i[1]]) > 1: # 위쪽 체크 cnt+1
                cnt += 1
            if non_violet.count([i[0], i[1]+1]) == 0 or non_violet.count([i[0], i[1]+1]) > 1: # 오른쪽 체크 cnt+1
                cnt += 1
        elif i[1] == 9:
            if non_violet.count([i[0]+1, i[1]]) == 0 or non_violet.count([i[0]+1, i[1]]) > 1: # 아래쪽 체크 cnt+1
                cnt += 1
            if non_violet.count([i[0]-1, i[1]]) == 0 or non_violet.count([i[0]-1, i[1]]) > 1: # 위쪽 체크 cnt+1
                cnt += 1
            if non_violet.count([i[0], i[1]-1]) == 0 or non_violet.count([i[0], i[1]-1]) > 1: # 왼쪽 체크 cnt+1
                cnt += 1

    print(f'#{tc} {cnt}') # 전체 면 개수에서 외각 아닌 면의 개수뺀거 출력







