chars = input()

chars_lst = []
answer = 0
for i in chars:
    if i.isalnum() == True:
        chars_lst.append(int(i))
    else:
        chars_lst.append(i)
print(chars_lst)
# [1, 2, 3, '*', '+']
cnt = 0
for i in range(len(chars_lst)): # 0 1 2 3 4
    if chars_lst[i] == '*':
        if answer == 0:
            answer = chars_lst[i-2] * chars_lst[i-1]
            chars_lst.remove(chars_lst[i])
            chars_lst.remove(chars_lst[i-1])
            chars_lst.remove(chars_lst[i-2])
        else:
            answer = chars_lst[i - 1] * answer
    elif chars_lst[i] == '/':
        if answer == 0:
            answer = chars_lst[i - 2] / chars_lst[i - 1]
            chars_lst.remove(chars_lst[i - 2])
            chars_lst.remove(chars_lst[i - 1])
            chars_lst.remove(chars_lst[i])
        else:
            answer = chars_lst[i - 1] / answer
    elif chars_lst[i] == '+':
        if answer == 0:
            answer = chars_lst[i - 2] + chars_lst[i - 1]
            chars_lst.remove(chars_lst[i - 2])
            chars_lst.remove(chars_lst[i - 1])
            chars_lst.remove(chars_lst[i])
        else:
            answer = chars_lst[i - 1] + answer
    elif chars_lst[i] == '-':
        if answer == 0:
            answer = chars_lst[i - 2] - chars_lst[i - 1]
            chars_lst.remove(chars_lst[i - 2])
            chars_lst.remove(chars_lst[i - 1])
            chars_lst.remove(chars_lst[i])
        else:
            answer = chars_lst[i - 1] - answer
print(answer)
# def sungpeol (chas):
#
#
#  11234665*/+