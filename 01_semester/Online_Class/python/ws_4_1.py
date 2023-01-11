pw='9899'
count = 0
i = ''

while i != pw:
    i = input("4자리 숫자를 입력하세요 : ")
    count += 1
    if count == 3:
        break
    print("땡!")
print("정답")