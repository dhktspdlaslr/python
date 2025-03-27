n1=int(input("정수:"))
n2=int(input("정수:"))
for i in range(n1, 0, -1):
    if n1%i==0 and n2%i==0:
        print(i)
        break