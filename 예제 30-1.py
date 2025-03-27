n=int(input("정수:"))
for i in range(2,n):
	if n%i==0:
		print(n, ":소수가 아닙니다")
		break
else:
	print(n, ":소수")