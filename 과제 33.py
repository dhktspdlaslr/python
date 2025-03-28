a=[80,76,75,63,57,39,27,26,18,11]
key=int(input("키:"))
high=0
low=9
while low>=high:
    mid=(low+high)//2
    if key==a[mid]:
        print(mid, "에서 탐색 성공")
        break
    elif key<a[mid]:
        high=mid+1
    else:
        low=mid-1
if low<high:
    print("탐색 실패")