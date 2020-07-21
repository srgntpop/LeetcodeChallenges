class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        R = []
        val = 1
        for i in range(len(nums)):
            R.append(val)
            val *= nums[i]
        l = 1
        for i in reversed(range(len(nums))):
            R[i] *= l
            l *= nums[i]
        return R
        
        
