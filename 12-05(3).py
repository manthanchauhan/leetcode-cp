class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        beg = 0
        end = 2**(2*n)
        ans = []
        
        for num in range(beg, end):
            nm = num
            zs = 0
            
            for i in range(0, 2*n):
                bit = nm%2
                nm //= 2
                
                if bit:
                    zs += 1
                    continue
                
                if zs:
                    zs -= 1
                    continue
                    
                zs = 1
                break
                    
            if zs:
                continue
                
            ans.append("")
            nm = num
            
            for i in range(0, 2*n):
                bit = nm%2
                nm //= 2
                
                if bit:
                    ans[-1] += "("
                else:
                    ans[-1] += ")"
                    
            # ans.append(s)
            
        return ans
        
