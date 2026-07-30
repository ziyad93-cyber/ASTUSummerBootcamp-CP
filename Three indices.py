from collections import Counter
for i in range (int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    for i in range(1,n-1):
        if arr[i-1] < arr[i] and arr[i] > arr[i+1] :
            print("YES")
            print(i, i+1, i+2)
            break

    else:
        print("NO")
