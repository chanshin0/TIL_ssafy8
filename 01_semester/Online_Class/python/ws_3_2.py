txt = input("문자열을 입력하세요 : ")

if len(txt) % 2 == 1:
    print(txt[len(txt)//2:][:1])
else:
    print(txt[len(txt)//2-1:][:2])