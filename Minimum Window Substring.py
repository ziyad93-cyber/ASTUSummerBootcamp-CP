class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or not s:
            return ""

        count_t = {}
        for c in t:
            count_t[c] = count_t.get(c, 0) + 1

        required = len(count_t)
        formed = 0
        window_counts = {}
        
        l = 0
        ans = float("inf"), None, None  

        for r in range(len(s)):
            c = s[r]
            window_counts[c] = window_counts.get(c, 0) + 1

            if c in count_t and window_counts[c] == count_t[c]:
                formed += 1

          
            while l <= r and formed == required:
                c = s[l]

                
                if r - l + 1 < ans[0]:
                    ans = (r - l + 1, l, r)

                window_counts[c] -= 1
                if c in count_t and window_counts[c] < count_t[c]:
                    formed -= 1

                l += 1

        return "" if ans[0] == float("inf") else s[ans[1] : ans[2] + 1]
