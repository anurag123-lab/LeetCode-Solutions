class Solution(object):
    def secondHighest(self, s):
        large = -1
        second = -1
        
        for ch in s:
            if ch.isdigit():
                num = int(ch)

                if num > large:
                    second = large
                    large = num
                
                elif num>second and num !=large:
                     second = num
        return second
                        