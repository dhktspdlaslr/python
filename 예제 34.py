for i in range(1,11):
    print(i, "약수:", end=" ")
    for j in range(1,i+1):
        if i%j==0:
            print(j, end=" ")
    print()