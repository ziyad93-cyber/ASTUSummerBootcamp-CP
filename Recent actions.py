from collections import defaultdict
for i in range(int(input())):
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))
    post = []
    removed_post = []
    d = defaultdict(int)
    count = 1
    unchanged = n- len(set(arr))
    for i in range(unchanged):
        post.append(-1)
    for i in arr  :   # 5 5 24 24 24 5 6 7 8 9 10 12 13 14 15 16 17 18 19
        if d[i] >= 1 :
            count +=1
            d[i]+=1
    
        else:
            if len(removed_post) < n:
                removed_post.append(count)
            
            count +=1
            d[i]+=1
            
    print(*(post+removed_post[::-1]))
