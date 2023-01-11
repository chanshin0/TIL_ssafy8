# 화물 도크
T= int(input())
for tc in range(T):
    N = int(input())
    papers = [[] for _ in range(N)]
    for i in range(N):
        s, e = map(int, input().split())
        papers[i] = [s, e]

    papers.sort(key=lambda x:x[1])
    print(papers)
    end = papers[0][1]
    cnt = 1
    for i in range(1, N):
        if end <= papers[i][0]:
            end = papers[i][1]
            cnt += 1
    print(f'#{tc+1} {cnt}')

