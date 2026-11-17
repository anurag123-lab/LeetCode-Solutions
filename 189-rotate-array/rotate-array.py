class Solution(object):
    def reverse(self,arr, left, right):
        while left < right:
            arr[left],arr[right] = arr[right], arr[left]
            left+=1
            right-=1
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k%=n
        if n == 0:
            return arr
        self.reverse(nums,0,n-1)
        self.reverse(nums,0,k-1)
        self.reverse(nums,k,n-1)
        