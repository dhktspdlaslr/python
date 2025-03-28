a=[1,2,3,4,5,6,7,8,9,10]
temp=a[0]
for i in range(0,9):
    a[i]=a[i+1]
a[9]=temp
print(a)