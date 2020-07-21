class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        if n == 0:
            return True
        
        if not flowerbed:
            if n == 0:
                return True
            else:
                return False 
        
        if len(flowerbed) == 1:
            if flowerbed[0] == 0:
                return True
            else:
                return False
        
        if flowerbed[0] == 0 and flowerbed[1] == 0:   
            n -= 1
            flowerbed[0] = 1
            
        for i in range(1, len(flowerbed)-1):
            if flowerbed[i-1] == 0 and flowerbed[i+1] == 0 and flowerbed[i] == 0:
                flowerbed[i] = 1
                n -= 1
                
        if flowerbed[len(flowerbed)-1] == 0 and flowerbed[len(flowerbed)-2] == 0:
            flowerbed[len(flowerbed)-1] = 1
            n-= 1
        
        if n <= 0:
            return True
        else:
            return False
        
        
        
