class Solution(object):
    def pivotArray(self, nums, pivot):
        res = [0] * len(nums)
        i = 0
        
        for num in nums:
            if num < pivot:
                res[i] = num
                i += 1
        for num in nums:
            if num == pivot:
                res[i] = num
                i += 1
        for num in nums:
            if num > pivot:
                res[i] = num
                i += 1
                
        return res
