def fn_d(n):
    result = 0
    a = str(n)
    for i in a:
        result += int(i)
    return result+n

def is_selfnumber(n):
    lst = []
    for i in range(n):
        if fn_d(i) == n:
            lst.append(i)
            
    if len(lst) == 0:
        return True
    else:
        return False

print(fn_d(91))
print(is_selfnumber(2))