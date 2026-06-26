class Solution:
    def longestAlternatingSubarray(self, nums: list[int], threshold: int) -> int:
        max_len = 0
        current_len = 0
        
        for i in range(len(nums)):
            if nums[i] > threshold:
                current_len = 0
            elif current_len > 0 and nums[i] % 2 != nums[i - 1] % 2:
                current_len += 1
            else:
                current_len = 1 if nums[i] % 2 == 0 else 0
                
            max_len = max(max_len, current_len)
            
        return max_len
