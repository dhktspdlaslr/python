a=[20,50,30,10,60,40]
for i in range(0,5):
    m=i
    for j in range(i+1, 6):
        if a[j]<a[m]:
            m=j
    temp=a[i]
    a[i]=a[m]
    a[m]=temp
print(a)