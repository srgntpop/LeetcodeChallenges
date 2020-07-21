class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if not s:
            return True
        start = 0
        end = len(s)-1
        while start < end:
            # check if st and end are alphanumeric
            while start < end and not s[start].isalnum():
                start += 1
            while end > start and not s[end].isalnum():
                end -= 1
            lowSt = s[start].lower()
            lowEnd = s[end].lower()
            if lowSt != lowEnd:
                return False
            start += 1
            end -= 1
        return True
