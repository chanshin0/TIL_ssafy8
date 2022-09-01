import imp
from tkinter import E
from django.shortcuts import render
import requests
import random

# Create your views here.

def lotto(request):
    # 1. 이번 회차 당첨 정보 받아오기
    API_URL = 'https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo=1'
    lotto = requests.get(API_URL).json()
    num1 = lotto.get('drwtNo1')
    num2 = lotto.get('drwtNo2')
    num3 = lotto.get('drwtNo3')
    num4 = lotto.get('drwtNo4')
    num5 = lotto.get('drwtNo5')
    num6 = lotto.get('drwtNo6')
    bonus = lotto.get('bnusNo')
    w = [num1,num2,num3,num4,num5,num6]

    check = [0]*6
    k = 1
    while k != 1000:
        mynum = []
        for i in range(7):
            a = random.randint(1, 45)
            if a in mynum:
                while a in mynum:
                    a = random.randint(1, 45)
                mynum.append(a)
            else:
                mynum.append(a)

        cnt = 0
        for i in mynum:
            if i in w:
                cnt += 1
        
        if cnt >= 6:
            check[1] += 1
        elif cnt == 5:
            if bonus in mynum:
                check[2] += 1
            else:
                check[3] += 1
        elif cnt == 4:
            check[4] += 1
        elif cnt == 3:
            check[5] += 1
        else:
            check[0] += 1
        k += 1

    context = {
        'w': w,
        'bonus':bonus,
        'check':check,
    }
    return render(request, 'lotto.html', context)