# 자료구조는 정말 최고야
N, M = map(int, input().split()) # 4 2
stack = [] # 담기
books = [] # 꺼내기
answer = 'Yes'
for tc in range(M):
    k = int(input()) # 2
    arr = list(map(int, input().split())) # [3, 1]
    books.append(arr)
# print(books) -> [[3, 1], [4, 2]]

for i in range(1, N+1): # 1 2 3 4
   for j in books:
       if i == j[-1] and j != []: # top이 인덱스에 맞으면 꺼내기
           stack.append(j.pop())
           # print(stack)

   if len(stack) != i: # j한바퀴 다돌았는데 꺼낸거 없으면 break
       answer = 'No'
       break

print(answer)