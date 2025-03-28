def func(a,b,c):
    if a>b:
        if a>c:
            return a
        else:
            return c
    else:
        if b>c:
            return b
        else:
            return c
a=int(input("정수: "))
b=int(input("정수: "))
c=int(input("정수: "))
r=func(a,b,c)
print(r)