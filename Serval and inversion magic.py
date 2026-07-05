t = int(input())
for _ in range(t):
    n = int(input())
    s = input()
    mismatch = []
    for i in range(n // 2):
        if s[i] != s[n - 1 - i]:
            mismatch.append(i)
    if len(mismatch) == 0:
        print("Yes")
    else:
        ok = True
        for i in range(1, len(mismatch)):
            if mismatch[i] != mismatch[i - 1] + 1:
                ok = False
                break
        if ok:
            print("Yes")
        else:
            print("No")
