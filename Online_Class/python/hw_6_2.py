# S = input("농도를 입력하세요(예시 : 12 15 27 13) :")
# T = input("소금물 양을 입력하세요 (예시 : 150 200 300 350) : ")
# U = input("제대로 입력하셨다면, Done : ")

lst = []
s_lst = []
t_lst = []
for i in range(5):
    s = input("농도는? : ")
    t = input("소금물 양은? : ")
    if s == 'Done' or t == 'Done':
        if len(s_lst) == len(t_lst):
            for j in range(len(s_lst)):

