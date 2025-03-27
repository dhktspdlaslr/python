a=1
b=1
sum=2
for i in range(3,21):
    c=a+b
    sum=sum+c
    a=b
    b=c
print(sum)