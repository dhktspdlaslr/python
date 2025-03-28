def fibo(a):
    if a<=2:
        return 1
    return fibo(a-1)+fibo(a-2)
n=int(input("정수: "))
result=fibo(n)
print(result)