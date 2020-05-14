class Solution:
    def grayCode(self, n: int) -> List[int]:
        if n == 0:
            return [0]
        
        l1 = self.grayCode(n-1)
        l2 = l1[::-1]
        
        add = 2**(n-1)
        
        for i, num in enumerate(l2):
            l2[i] += add
            
        return l1+l2
        
