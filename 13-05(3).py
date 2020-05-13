def allc(k, n, trv, beg):
    if n <= 0:
        return []
    
    if k == 1:
        if (beg <= n <= 9) and (not trv[n-1]):
            return [[n]]
        else:
            return []
        
    ans = []
    
    for i in range(beg, 10):
        if not trv[i-1]:
            trv[i-1] = True
            
            combs = allc(k-1, n-i, trv, i+1)
            
            for comb in combs:
                comb.append(i)
                ans.append(comb)
                
            trv[i-1] = False
    
    return ans

class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        trv = [False]*9
        
        ans = allc(k, n, trv, 1)
        
        return ans
        
