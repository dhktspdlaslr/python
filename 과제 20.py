n=int(input("정수:"))
count=0
for i in range(1, n+1):
    if n%i==0:
        print(i, end=" ")
        count+=1
print(count, end="개")