def func(a):
    if a == 1:
        print("소수 아님", end="")
        return
    for i in range(2, a):  
        if a % i == 0: 
            print("소수 아님", end="")
            return
    print("소수", end="")  

for i in range(1, 11):
    print(i, ":", end=" ")
    func(i)
    print() 