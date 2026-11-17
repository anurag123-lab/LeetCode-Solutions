class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        pos = 0
        for i in range(0,n):
            if nums[i]!=0:
                if pos != i:
                    nums[i],nums[pos] = nums[pos],nums[i]
                pos +=1
