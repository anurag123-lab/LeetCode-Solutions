class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        sum = 0
        total = n*(n+1)//2
        for i in range(0,n):
            sum+=nums[i]
        return total - sum
        