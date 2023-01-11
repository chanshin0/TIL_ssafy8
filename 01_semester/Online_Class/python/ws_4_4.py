word1 = input('첫 번째 이름을 입력하세요 : ')
word2  = input('두 번째 이름을 입력하세요 : ')

word1_sum = 0
word2_sum = 0
for i in word1:
    word1_sum += ord(i)
for i in word2:
    word2_sum += ord(i)
if word1_sum - word2_sum > 0:
    print(word1)
elif word1_sum - word2_sum < 0:
    print(word2)
else:
    print("same")

