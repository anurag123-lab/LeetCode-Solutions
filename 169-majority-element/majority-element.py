class Solution(object):
    def majorityElement(self, nums):
        n =len(nums)
        freq = {}
        for i in range (0,n):
            if nums[i] in freq:
                freq[nums[i]]+=1
            else:
                freq[nums[i]] = 1
        maxx = 0
        ans = None
        for key,count in freq.items():
            if count>maxx:
                maxx = count
                ans = key
        return ans



         

        