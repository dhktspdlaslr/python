a=[1,3,5,7]
b=[3,4,8,10]
c=[]
i=0
j=0
while i<4 and j<4:
    if a[i]<b[j]:
        c.append(a[i])
        i=i+1
    else:
        c.append(b[j])
        j=j+1
if i==4:
    while j<4:
        c.append(b[j])
        j=j+1
else:
    while i<4:
        c.append(a[i])
        i=i+1
print(c)