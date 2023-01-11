# 새로운 버스 노선
T = int(input())
for tc in range(T):
    N = int(input())

    # 하나의 리스트에 모든 노선 전부 넣은 뒤,,,
    bus_stop = []
    for n in range(N): # 0 1 2
        bus, A, B = map(int, input().split())
        if bus == 1:
            bus_stop += list(range(A, B+1))
        elif bus == 2:
            bus_stop += list(range(A, B, 2))
            bus_stop.append(B)
        else:           # 광역급행
            bus_stop.append(A)
            bus_stop.append(B)
            if A % 2 == 1:   # 홀수일 때
                for i in range(A+1, B):
                    if i % 10 != 0 and i % 3 == 0:
                        bus_stop.append(i)
            else:       # 짝수일 때
                for i in range(A+1, B):
                    if i % 4 == 0:
                        bus_stop.append(i)
    # print(bus_stop)

    # 카운팅 리스트 길이 구하기
    maxV = 0
    for i in bus_stop:
        if i > maxV:
            maxV = i
    # print(maxV)
    counting = [0]*(maxV+1)    # 카운팅 리스트 생성

    # 노선 인덱스에 맞춰서 카운팅
    for i in range(len(bus_stop)):
        counting[bus_stop[i]] += 1
    # print(bus_stop)
    # print(counting)

    # 카운팅의 최댓값 계산 후 출력
    maxV = 0
    for i in counting:
        if i > maxV:
            maxV = i

    print(f'#{tc+1} {maxV}')