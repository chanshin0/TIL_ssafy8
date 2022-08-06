x, y, w, h = map(int, input().split())

distance = [x, y, (w-x), (h-y)]
if min(distance) < 0:
    print(min(distance)*-1)
else:
    print(min(distance))
