def func(a):
    for i in range(1, a+1):
        if a%1==0:
            print(i, end=" ")
for i in range(1,11):
    print(i, ":", end=" ")
    func(i)
    print()