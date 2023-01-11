# 백만장자 프로젝트
T = int(input())
for tc in range(T):
    N = int(input())
    price = list(map(int, input().split()))

    benef = 0
    ismax = 0 # 리스트의 최대값 담을 변수
    k = 0
    while k < N:
        # 최대값 구하기
        for i in range(k, N):
            if price[i] >= ismax:
                ismax = price[i]
                m_idx = i

        # 이익 계산하기
        for i in range(k, m_idx):
            benef += ismax - price[i]

        ismax = 0
        k = m_idx+1

    print(f'#{tc+1} {benef}')