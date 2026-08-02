t = int(input())
     
    for _ in range(t):
        n = int(input())
        a = list(map(int, input().split()))
     
        seen = set()
        ans = 0
     
        for i in range(n - 1, -1, -1):
            if a[i] in seen:
                ans = i + 1
                break
            seen.add(a[i])
        print(ans)
