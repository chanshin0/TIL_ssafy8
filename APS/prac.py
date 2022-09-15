def post(n):
    if n<=5:
        post(n*2)
        post(n*2+1)
        print(a[n])


a = [0,1,2,3,4,5]

post(1)
