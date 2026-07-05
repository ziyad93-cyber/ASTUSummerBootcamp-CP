t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    left = 0
    right = n - 1
    ans = 0
    while left < right:
        while left < right and a[left] == 0:
            left += 1
        while left < right and a[right] == 1:
            right -= 1
        if left < right:
            ans += 1
            left += 1
            right -= 1
    print(ans)
