words = []
while True:
    T = input("끝말잇기! 끝내려면 Done입력!")
    if T == 'Done' or T == 'done':
        break
    words.append(T)

for i, word in enumerate(words):
    if i < len(words)-1:
        if word[-1] != words[i+1][0]:
            print(f'{i+2}번째 사람 땡!')
    elif len(words) >i > 0 and words.count(word) > 1:
        print(f'{i+1}번째 사람 땡!')