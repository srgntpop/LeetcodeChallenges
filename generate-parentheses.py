class Solution(object):
    def generateParenthesis(self, n):
        """
        
        
        
        :type n: int
        :rtype: List[str]
        """
        # n = 2
        if n <= 0:
            return [""]
        if n == 1:
            return ["()"]
        self.ans = []
        def generate(array, n, onstack):
            """
            if n is zero and onstack is zero:
                self.ans.append(''.join(array))
            if n is big enough:
                add left paren
                update n and onstack
                recursively call
            if onstack is big enough:
                add right paren
                update n and onstack
                recursively call
            """
        
            if n == 0 and onstack == 0:
                self.ans.append(''.join(array))
            
            if n > 0:
                array.append('(')
                generate(array, n-1, onstack+1)
            if onstack > 0:
                array.append(')')
                generate(array, n, onstack-1)
            if array:
                array.pop(len(array)-1)
            
        generate([], n, 0)
        return self.ans
