def allC(cands, i, tar, n, vis):
    if tar < 0:
        return []
    
    if tar == 0:
        return [[]]
    
    if i == n:
        return []
    
    ans = []
    
    if cands[i] <= tar:
        if ((not cands[i] == cands[i-1]) or (i == 0)) or vis[i-1]:
            vis[i] = True
            combs = allC(cands, i+1, tar-cands[i], n, vis)

            for comb in combs:
                comb.append(cands[i])

            ans += combs
            del combs
            vis[i] = False
    else:
        return []
    
    ans += allC(cands, i+1, tar, n, vis)
    return ans

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        vis = [False]*len(candidates)
        return allC(candidates, 0, target, len(candidates), vis)
        
