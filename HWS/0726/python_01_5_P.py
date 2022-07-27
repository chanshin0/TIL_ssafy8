def loney(num_list):
    result = [num_list[0]]
    for i in range(len(num_list)):
        if result[len(result)-1] == num_list[i]: 
        ## result에 몇 개가 담겨있을지 모르니,
        ## result[len(result)-1]로 맨 마지막 index를 반환.         
            continue                             
        else:
            result.append(num_list[i])
        
    return result

print(loney([1, 1, 3, 3, 0, 1, 1]))
print(loney([4, 4, 4, 3, 3]))