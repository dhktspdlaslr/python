sum=0
for i in range(1,101):
    if i%3==0:
        sum=sum-i
    else:
        sum=sum+i
print(sum)