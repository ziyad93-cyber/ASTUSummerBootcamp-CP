import sys

def solve():
    input = sys.stdin.read
    data = input().split()
    
    if not data:
        return
    
    t = int(data[0])
    idx = 1
    
    out = []
    for _ in range(t):
        n = int(data[idx])
        a = [int(x) for x in data[idx + 1 : idx + 1 + n]]
        idx += 1 + n
        
      
        a.sort()
        
        possible = True
       
        for i in range(1, n - 1, 2):
            if a[i] != a[i + 1]:
                possible = False
                break
                
        if possible:
            out.append("YES")
        else:
            out.append("NO")
            
    print('\n'.join(out))
