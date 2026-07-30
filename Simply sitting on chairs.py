for i in range (int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    count = 0
    for i in range(n):
        if i+1 >= arr[i] :
            count+=1
    print(count)
