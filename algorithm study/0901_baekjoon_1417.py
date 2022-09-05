# 국회의원 선거
N = int(input())
vote = []
for n in range(N):
    vote.append(int(input()))
vote2 = vote[1:]
vote3 = vote2.copy()
vote2.sort(reverse=True)
dasom = vote[0]
dasom2 = vote[0]

cnt1 = 0
for i in range(len(vote2)):
    if vote2[i] >= dasom:
        while vote2[i] >= dasom:
            vote2[i] -= 1
            dasom += 1
            cnt1 += 1
            if max(vote) == dasom:
                break
cnt2 = 0
while True:
    if len(vote) == 1:
        break
    else:
        if max(vote3) < dasom2:
            break
        else:
            for i in range(len(vote3)):
                if vote3[i] >= dasom2:
                    vote3[i] -= 1
                    dasom2 += 1
                    cnt2 += 1
                    if max(vote3) == dasom2:
                        break

if vote3.count(cnt2) > 1:
    cnt2 += 1

print(min(cnt1,cnt2))
# print(cnt1,cnt2)

