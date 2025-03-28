a=[26,27,39,63,57,75,11,76,80,18]
key=int(input("키: "))
cnt=0
while cnt<10:
    if key==a[cnt]:
        print(cnt, "에서 탐색 성공")
        break
    cnt=cnt+1
if cnt==10:
    print("탐색 실패")