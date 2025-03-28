b=[1,1,0,0,1]
n=0
for i in range(0,5):
    n=n+b[i]*(2**(4-i))
print(n)