for _ in range(int(input())):
    n = int(input())

    seen = set()
    ans = []

    for i in range(n):
        row = list(map(int, input().split()))

        for x in row:
            if x not in seen:
                seen.add(x)
                ans.append(x)

    missing = 0

    for x in range(1, 2 * n + 1):
        if x not in seen:
            missing = x
            break

    print(missing, *ans)
