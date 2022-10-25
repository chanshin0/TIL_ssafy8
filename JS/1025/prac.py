from cgi import print_directory
from tkinter import E


while True:
    a, b = map(int, input().split())
    if a and b:
        print(a+b)
    else