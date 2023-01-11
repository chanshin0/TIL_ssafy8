orders = '아이스아메리카노,카라멜마키야또,에스프레소,아메리카노,아메리카노,아이스라떼,핫초코,아이스아메리카노,아메리카노,아이스카라멜마키야또,아이스라떼,라떼마키야또,카푸치노,라떼마키야또'
a = [i for i in orders]
lst_orders = orders.split(',') 

count_ice = 0
for i in lst_orders:
    if '아이스' in i:
        count_ice += 1
print(f'아이스 음료 주문은 총 {count_ice}개 입니다.')

dict = {}
for order in set(lst_orders):
    dict.setdefault(order, lst_orders.count(order))
print('<<메뉴 별 주문 수>>')
for k, v in dict.items():
    print(k, v)