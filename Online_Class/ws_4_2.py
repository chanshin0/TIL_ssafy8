students = ['박해피', '이영희', '조민지', '조민지', 
            '김철수', '이영희', '이영희', '김해킹',
            '박해피', '김철수', '한케이', '강디티',
            '조민지', '박해피', '김철수', '이영희',
            '박해피', '김해킹', '박해피', '한케이','강디티']

dict = {}
for i in set(students):
    dict.setdefault(i, students.count(i))
arrange = sorted(dict.items(), key=lambda x : x[1], reverse=True)

for k, v in arrange:
    print(k, v)