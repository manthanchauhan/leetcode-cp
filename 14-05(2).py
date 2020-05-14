def allC(i, n, k):
    if k < 0:
        return []
    
    if k == 0:
        return [[]]
    
    if n - i + 1 < k:
        return []
    
    ans = []
    combC = allC(i+1, n, k-1)
    
    for comb in combC:
        comb.append(i)
        
    ans += combC
    ans += allC(i+1, n, k)
    return ans

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = allC(1, n, k)
        return ans
