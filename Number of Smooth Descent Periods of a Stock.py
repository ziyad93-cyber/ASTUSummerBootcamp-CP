class Solution:
    def getDescentPeriods(self, prices: list[int]) -> int:
        total_periods = 1
        current_streak = 1 
        for i in range(1, len(prices)):
            if prices[i] == prices[i - 1] - 1:
                current_streak += 1
            else:
                current_streak = 1
            total_periods += current_streak    
        return total_periods
