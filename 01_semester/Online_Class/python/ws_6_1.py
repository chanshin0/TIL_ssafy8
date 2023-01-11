id = input()
str = ''
for i in id:
    if i.isalnum() == True:
        str += i

print(str[:6]+ '*'*len(str[7:])) # 그냥 7로 해도됨