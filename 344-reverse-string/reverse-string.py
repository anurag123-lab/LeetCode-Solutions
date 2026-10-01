class Solution(object):
    def reverseString(self, s):
       left = 0
       right = len(s)-1
       for i in range(len(s)):
        while left<right:

            s[left],s[right] = s[right],s[left]
            left = left+1
            right = right-1
        if left==right:
            return s[left]


        return s[left]