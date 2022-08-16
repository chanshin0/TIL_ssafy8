# [기본] 3일차 - 글자수 (제출용)
T = int(input())
for tc in range(1, T+1):
    str1 = input()
    str2 = input()

    ismax = 0
    for i in str1: # str1에서 하나 꺼내서
        cnt = 0
        for j in str2: # str2 전체 한바퀴 돌리며 비교
            if i == j:
                cnt += 1
                if cnt > ismax:
                    ismax = cnt
    print(f'#{tc} {ismax}')