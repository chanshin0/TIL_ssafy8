# 전쟁 - 전투
N, M = map(int, input().split())
battle = [list(input()) for _ in range(M)]

w = []
b = []
cntW = 0
cntB = 0
for i in range(N):
    for j in range(M):
      if battle[i][j] == 'W':
        cntW += 1
        b.append(cntB)
        cntB = 0
      elif battle[i][j] == 'B':
        cntB += 1
        w.append(cntW)
        cntW = 0
w.append(cntW)
b.append(cntB)
# [1, 8, 0, 0, 0, 0, 0, 0, 0, 7]
# [0, 1, 0, 0, 0, 0, 0, 0, 0, 8, 0, 0, 0, 0, 0, 0, 0]

ansW = 0
ansB = 0
temp = 0
isol = 0
for i in range(len(w)):
    if w[i] != 0:
        temp += w[i]
        isol = 0
    else:
        isol += 1
        if isol >= N:
            ansW += temp**2
            temp = 0
ansW += temp**2
temp = 0
isol = 0

for i in range(len(b)):
    if b[i] != 0:
        temp += b[i]
        isol = 0
    else:
        isol += 1
        if isol >= N:
            ansB += temp**2
            temp = 0
ansB += temp**2

print(ansW, ansB)

