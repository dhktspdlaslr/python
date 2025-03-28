a=[20, 50, 30, 10, 60, 40]
for i in range(0,5):
    for j in range(0, 5-i):
        if a[j]>a[j+1]:
            temp=a[j]
            a[j]=a[j+1]
            a[j+1]=temp
print(a)