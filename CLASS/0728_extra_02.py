import random

class ClassHelper:
    def __init__(self, lst):
        self.lst = lst
    
    def pick(self, n):
        ran_lst = random.sample(self.lst, n)
        return ran_lst

    def match_pair(self):
        ran_lst = random.sample(self.lst, len(self.lst))
        new_lst = [ran_lst[i:i+2] for i in range(0,len(self.lst), 2)]
        # 리스트 n개 만큼 잘라서 담기
        at_last = new_lst[len(new_lst)-1]
        # 리스트 마지막 인덱스 변수에 담기
        if len(self.lst) % 2 == 1:
            new_lst[len(new_lst)-2].append(at_last[0])
            # 끝에 있는 애를 끝에서 두번째에 추가하고
            new_lst.remove(at_last)
            # 걔 삭제
        return new_lst

ch = ClassHelper(['김싸피', '이싸피', '조싸피', '박싸피', '정싸피'])

print(ch.pick(1)) 
print(ch.pick(1)) 
print(ch.pick(2)) 
print(ch.pick(3))
print(ch.pick(4)) 

print(ch.match_pair())