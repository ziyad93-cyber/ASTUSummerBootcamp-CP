t = int(input())

for _ in range(t):
    n, m = map(int, input().split())

    for i in range(n):
        row = []
        for j in range(m):
            if ((i // 2) + (j // 2)) % 2 == 0:
                row.append((i + j) % 2)
            else:
                row.append(1 - ((i + j) % 2))
        print(*row)
