'''
정점 번호 V = 1 ~ E+1
간선 수
부모-자식 순
4
1 2 1 3 3 4 3 5
'''
def preorder(n):
    if n:
        print(n)
        preorder(ch1[n])
        preorder(ch2[n])

E = int(input())
arr = [list(map(int, input().split()))]
V = E + 1
# 부모를 인덱스로 자식 번호 저장
ch1 = [0]*(V+1)
ch2 = [0]*(V+1)
root = 1
for i in range(E):
    p, c = arr[i*2], arr[i*2+1]
    if ch1[p] == 0:     # 아직 자식이 없으면
        ch1[p] = c      # 자식1로 저장
    else:
        ch2[p] = c

preorder(root)