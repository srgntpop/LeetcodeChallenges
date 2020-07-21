# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        low = 1
        high = n
        mid = n // 2
        if n == 1:
            return 1
        if n == 2:
            if isBadVersion(1):
                return 1
            else:
                return n
        while (low <= high):
            mid = (high + low) // 2
            if isBadVersion(mid):
                if mid - 1 == 0:
                    return 1
                if not isBadVersion(mid-1):
                    return mid
                high = mid - 1
            else:
                if isBadVersion(mid+1):
                    return mid+1
                low = mid + 1
        return n+1
        
        
        
