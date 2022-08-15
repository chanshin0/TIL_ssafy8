T  = int(input())
for tc in range(T):
    n = list(map(int, input()))
    # [1,2,3,4,5]
# 1990 9190 9910 9110 1910 1190
    max_n = n.copy() # 54301 54310 // 
    sorted_n = sorted(max_n)
    for i in range(len(max_n))[::-1]: # 0 1 2 3 4 
        if max_n[i] != sorted_n[i]:
            s_i = i #sorted한거랑 일치하지 않는 지점의 i
    
    
    
    min_n = n.copy()

            

    #print(f'#{tc+1}', end=" ")
    #print( ''.join(list(map(str, min_n))), ''.join(list(map(str, #max_n))))