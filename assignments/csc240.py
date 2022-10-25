import math
def f(i):
    dict1 = {}
    for j in range(1,i):
        if j == 1:
            dict1[j] = 2
            print(2)
        elif j==2:
            dict1[j] = 3
            print(3)
        else:
            dict1[j] = 3*dict1[math.ceil(2*j/3)]+1
            print(dict1[j])
def g(n):
    while n !=2:
        n = math.ceil(2*n/3)
        print(n)

def h(n):
    while n >2:
        n = math.ceil(2*n/3)
        print(n)
