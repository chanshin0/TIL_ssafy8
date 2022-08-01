Y = int(input("연도를 입력하세요"))

if Y % 4 == 0 and Y % 100 != 0:
    print("윤년입니다.")
elif Y & 40 == 0:
    print("윤년입니다.")
else:
    print("윤년 아닙니다.")
    