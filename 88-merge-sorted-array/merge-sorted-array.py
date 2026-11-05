class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        for x in range(0,n):
            nums1[m+x] = nums2[x]
        for i in range(1,m+n):
            key = nums1[i]
            j = i-1
            while j>=0 and nums1[j]> key:
                nums1[j+1] = nums1[j]
                j-=1
            nums1[j+1] = key
            


        