from collections import Counter
for _ in range(int(input())):
    input()
    arr = list(map(int, input().split()))
    cnt = Counter(arr)
    ans = []
    for x in sorted(cnt):
        ans.append(x)
    for x in sorted(cnt):
        ans.extend([x] * (cnt[x] - 1))
    print(*ans)
