for _ in range(int(input())):
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))
    
    max_val = max(arr)
    ans = []
    
    for _ in range(m):
        c, l, r = input().split()
        l, r = int(l), int(r)
        
        if l <= max_val <= r:
            if c == "+":
                max_val += 1
            else:
                max_val -= 1
        ans.append(max_val)
        
    print(*ans)
