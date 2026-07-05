t = int(input())
for i in range(t):
    n = int(input())
    s = input()
    ans = 0
    for k in range(n):
        cur=s[k:]+s[:k]
        blocks= 1
        for i in range(1,n):
            if cur[i]!=cur[i-1]:
                blocks += 1
        ans=max(ans,blocks)
    print(ans)
