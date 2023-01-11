# 의석이의 세로로 말해요
T = int(input())
for tc in range(T):
    arr = [list(input()) for _ in range(5)]
    # [['A', 'A', 'B', 'C', 'D', 'D'], ['a', 'f', 'z', 'z'], ['0', '9', '1', '2', '1'], ['a', '8', 'E', 'W', 'g', '6'], ['P', '5', 'h', '3', 'k', 'x']]
    new_arr = ''
    for i in range(15):  # 문자열 길이는 최대 15
        for j in range(5):
            try:
                new_arr += arr[j][i]
            except IndexError:
                continue
    print(f'#{tc+1} {new_arr}')