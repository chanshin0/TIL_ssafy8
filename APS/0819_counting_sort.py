# 카운팅 정렬 연습

data = [0, 4, 1, 3, 1, 2, 4, 1]
N = len(data)
k = 4 # 정수의 최댓값
d_cnt = [0]*(k+1)
d_cntSort = [0]*N

for i in range(N):
    d_cnt[data[i]] += 1
# print(d_cnt) [1, 3, 1, 1, 2]

for i in range(1,len(d_cnt)):
    d_cnt[i] += d_cnt[i-1]
# print(d_cnt) [1, 4, 5, 6, 8]

for i in range(len(d_cntSort)-1, -1, -1): # 7 6 5 4 3 2 1 0
    d_cnt[data[i]] -= 1
    d_cntSort[d_cnt[data[i]]] = data[i]
print(d_cntSort)