for i in range(2,101):
    chk=1
    for j in range(2,i):
        if i%j==0:
            chk=0
            break
    if chk==1:
        print(i, end=" ")