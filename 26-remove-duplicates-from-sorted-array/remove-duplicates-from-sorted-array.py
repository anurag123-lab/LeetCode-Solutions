class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) <=1:
            return 1
        k = 1
        for i in range(1,len(nums)):
            if nums[i] != nums[k-1]:
                nums[k] = nums[i]
                k+=1
        return k       