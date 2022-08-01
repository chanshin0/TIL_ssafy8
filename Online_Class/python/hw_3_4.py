s_triangle = input('세 개의 변을 입력해주세요(x y z) :  ')

lst_s = s_triangle.split(' ')
lst_s.sort()
int_lst_s = list(map(int, lst_s))
if sum(int_lst_s[:2]) > int_lst_s[2]:
    if int_lst_s.count(int_lst_s[0]) == 3:
        print("정삼각형")
    elif int_lst_s.count(int_lst_s[1]) == 2:
        print("이등변 삼각형")
    elif int_lst_s[0]**2 + int_lst_s[1]**2 == int_lst_s[2]**2:
        print("직각삼각형")
    else:
        print("삼각형")
else:
    print("삼각형이 아닙니다.")