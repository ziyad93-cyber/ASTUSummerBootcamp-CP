class Solution(object):
    def minNumberOperations(self, target):
        ans = target[0]
        for a, b in zip(target, target[1:]):
            if a < b:
                ans += b - a
        return ans
