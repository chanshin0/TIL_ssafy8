
for tc in range(10):
    T = int(input())
    lst_height = list(map(int, input().split()))
    rst = 0 # 최고점 최저점의 차이
    cnt = 0 # 덤프 몇번 했는지
    while cnt <= T:
        for i in range(1, len(lst_height)): # 버블  정렬
            for j in range(i, len(lst_height)): #점차 범위를 줄여가면서
                if lst_height[j] < lst_height[j-1]:
                    lst_height[j], lst_height[j-1]  = lst_height[j-1], lst_height[j]
                    # 앞뒤 서로 뒤바꿈
        rst = lst_height[-1] - lst_height[0] 
            # 정렬 후 rst
        lst_height[0] += 1
        lst_height[-1] -= 1
        # 젤 작은거 +1, 젤 큰거 -1
        cnt += 1
        if rst <= 1:
            break
        # 하다가 평탄화 완료되면 종료

    print(f'#{tc+1} {rst}')
