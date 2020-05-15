class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        ans = 1
        
        if n == 0:
            return ans
        
        for i in range(1, n+1):
            add = 9
            
            for j in range(1, i):
                add *= 10-j
                
            ans += add
        
        
        # for i in range(1, n+1):
            
        return ans
        
