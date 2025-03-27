chk=1
n=int(input("정수:"))
for i in range(2,n):
    if n%i==0:
        chk=0
        break
if chk==1:
    print(n, ":소수")
else:
    print(n, ":소수가 아닙니다")