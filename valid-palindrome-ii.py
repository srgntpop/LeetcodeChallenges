class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        start = 0
        end = len(s)-1
        def isPali(s, start, end):
            while start <= end:
                if s[start] != s[end]:
                    return False
                start += 1
                end -= 1
            return True
        while start <= end:
            if s[start] != s[end]:
                return isPali(s, start+1, end) or isPali(s, start, end-1)
            start += 1
            end -= 1
        return True
        
        
