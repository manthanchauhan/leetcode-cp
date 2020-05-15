def uniqChars(s):
    vis = [False]*26
    
    for c in s:
        if vis[ord(c) - 97]:
            return False
        
        vis[ord(c) - 97] = True
        
    return True

def acc(s, vis):
    for c in s:
        if vis[ord(c) - 97]:
            return False
        
    return True

def count(arr, n, i, vis):
    if i == n:
        return 0
        
    ans = 0
    
    if acc(arr[i], vis):
        for c in arr[i]:
            vis[ord(c) - 97] = True
            
        ans = max(ans, count(arr, n, i+1, vis) + len(arr[i]))
        
        for c in arr[i]:
            vis[ord(c) - 97] = False
        
    ans = max(ans, count(arr, n, i+1, vis))
    return ans
    

class Solution:
    def maxLength(self, arr: List[str]) -> int:
        arr = [s for s in filter(uniqChars, arr)]
        
        vis = [False]*26
        ans = count(arr, len(arr), 0, vis)
        return ans
        
