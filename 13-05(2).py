def cnt(vis, N, i):
    ans = 0
    
    for num in range(1, N+1):
        if vis[num-1]:
            continue
            
        if num%(i+1) and (i+1)%num:
            continue
            
        vis[num-1] = True
        
        if i < N-1:
            ans += cnt(vis, N, i+1)
        else:
            ans += 1
            
        vis[num-1] = False
        
    return ans
    
class Solution:
    def countArrangement(self, N: int) -> int:
        vis = [False]*N
        
        ans = cnt(vis, N, 0)
        
        return ans
