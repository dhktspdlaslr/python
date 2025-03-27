n=int(input("정수:"))
count=0
for i in range(1,n+1):
	if n%i==0:
		count=count+1

if count ==2:
	print(n, ":소수")
else:
	print(n, ":소수 아님")