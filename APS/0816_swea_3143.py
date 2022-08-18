T = int(input())
for tc in range(T):
    A, B = input().split()
    len_a = len(A)

    cnt = 0 # B가 몇번 들어있는지 체크
    while True:
        if len(A) < len(B): # 계속 슬라이싱하다가 더 비교할 수 없을 정도로 A가 짧아지면 종료.
            break
        if B[0] == A[0]: # B의 첫글자랑 일치할때 검사
            if B == A[:len(B)]: # B가 포함되어있으면 카운트하고, 슬라이싱
                cnt += 1
                A = A[len(B):]
                # print(A)
            else:
                A = A[1:]
        else:
            A = A[1:] # B랑 첫글차 일치안하면 한글자씩 잘라냄
            # print(A)

    print(f'#{tc+1} {len_a-(len(B)*cnt)+cnt}')