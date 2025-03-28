def s(a):
    if a<=1:
        return 1
    return a+s(a-1)
n=int(input("정수: "))
result=s(n)
print(result)