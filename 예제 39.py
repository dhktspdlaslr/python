a=[1,2,3,4,5,6,7,8,9,10]
for i in range(0,5):
    temp=a[i]
    a[i]=a[9-i]
    a[9-i]=temp
print(a)