class Solution(object):
    def countDigitOccurrences(self, nums, digit):
        listToString = ""
        for i in nums:
            listToString += str(i)
        return listToString.count(str(digit))
