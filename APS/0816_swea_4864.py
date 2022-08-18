# 3일차 - 문자열 비교 (제출용)
T = int(input())
for tc in range(T):
    str1 = input() # XYPV
    str2 = input() # EOGGXYPVSY

    for j in range(len(str2)):
        for i in range(len(str1)):
            if str1[i] == str2[j]:
