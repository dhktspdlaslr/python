a=[1,2,3,4,5,6,7,8,9,10]
temp=a[9]
for i in range(9,0,-1):
    a[i]=a[i-1]
a[0]=temp
print(a)
