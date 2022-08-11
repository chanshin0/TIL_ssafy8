def isdecimal(num):
    if num == 2:
        return True
    for l in range(1, int(num)+1, 2):
        if num % 2 == 0 or num == 1:
            return False
        elif num % l == 0 and l not in [1, num]:
            return False
    return True

print(isdecimal(127))