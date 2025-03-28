a=[11,18,26,27,39,57,63,75,76,80]
key=int(input("키 : "))
low=0
high=9
while low<=high:
    mid=(low+high)//2
    if key ==a[mid]:
        print(mid, "에서 탐색 성공")
        break
    elif key<a[mid]:
        high=mid-1
    else:
        low=mid+1
if low>high:
    print("탐색 실패")