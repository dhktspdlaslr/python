a=int(input("정수:"))
m=a
while a!=0:
    if a>m:
        m=a
    a=int(input("정수:"))
print("최댓값:",m)