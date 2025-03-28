import random
a=[]
for i in range(10):
    a.append(random.randint(1,100))
print(a)

m=a[0]
for i in range(1,10):
    if m<a[i]:
        m=a[i]
print("최댓값", m)