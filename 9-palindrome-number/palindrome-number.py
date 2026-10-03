class Solution(object):
    def isPalindrome(self, x):
        rev  = ""
        s = str(x)
        for i in range(len(s)-1,-1,-1):
            rev = rev +s[i]
        if rev == s :
            return True
        else:
            return False
         







        
        