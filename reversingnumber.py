class Solution(object):
    def reverse(self, x,):
        if x > 0:
            sign = 1
        else:
            sign = -1
        x = abs(x)
        rev = 0
        while x!=0:
            a = x%10
            rev = (rev*10)+a
            x = x//10
        rev = rev * sign

        if rev < -2**31 or rev > 2**31 - 1:
            return 0
        return(rev)
    

        