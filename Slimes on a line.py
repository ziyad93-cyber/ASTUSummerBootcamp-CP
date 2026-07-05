import sys

def solve():
    n = int(sys.stdin.readline())
    a = list(map(int, sys.stdin.readline().split()))
    
   
    mn = min(a)
    mx = max(a)
    
   
    ans = (mx - mn + 1) // 2
    print(ans)

def main():
    try:
        t = int(sys.stdin.readline())
        for _ in range(t):
            solve()
    except Exception:
        pass

if name == 'main':
    main()
