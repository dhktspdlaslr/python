def func(n):
    if n <= 1:
        return 1
    return n * func(n - 1)

n = int(input("정수 입력: "))

result = func(n)
print(n,"! = ", result)