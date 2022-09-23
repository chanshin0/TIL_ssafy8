# 정식이의 은행업무
T = int(input())
for tc in range(T):
    bin = input()
    trit = input()

    nums = [] # [2, 14, 8, 11]
    for i in range(len(bin)):
        if bin[i] == '1':
            temp = '0'
        else:
            temp = '1'
        nums.append(int(bin[:i]+temp+bin[i+1:], 2))

    rst = ''
    for i in range(len(trit)):
        if trit[i] == '2':
            for j in ['0', '1']:
                temp = j
                ans = int(trit[:i] + temp + trit[i+1:], 3)
                if ans in nums:
                    rst = ans
                    break
        elif trit[i] == '1':
            for j in ['0', '2']:
                temp = j
                ans = int(trit[:i] + temp + trit[i+1:], 3)
                if ans in nums:
                    rst = ans
                    break
        else:
            for j in ['1', '2']:
                temp = j
                ans = int(trit[:i] + temp + trit[i+1:], 3)
                if ans in nums:
                    rst = ans
                    break

    print(f'#{tc+1} {rst}')

