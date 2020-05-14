def allC(st, i, n, tar):
    if tar == 0:
        return [[]]
    
    if tar < 0:
        return []
        
    ans = []
    
    if st[i] > tar:
        return ans
    
    combs = allC(st, i, n, tar-st[i])
        
    for comb in combs:
        comb.append(st[i])
        ans.append(comb)
            
    if i+1 < n:
        ans += allC(st, i+1, n, tar)
        
    return ans
    

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        ans = allC(candidates, 0, len(candidates), target)
        
        return ans
        
