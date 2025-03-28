b=[]
n=int(input("10진수:"))
while n!=0:
    b.append(n%8)
    n=n//8
for i in range(len(b)-1, -1, -1):
    print(b[i], end=" ")