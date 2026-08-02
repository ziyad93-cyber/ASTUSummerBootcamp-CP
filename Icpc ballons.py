t = int(input())

for _ in range(t):
    n = int(input())
    s = input()

    seen = set()
    ans = 0

    for c in s:
        if c in seen:
            ans += 1
        else:
            ans += 2
            seen.add(c)

    print(ans)
