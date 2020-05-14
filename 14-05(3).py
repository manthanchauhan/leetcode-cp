from math import log10

def seqN(low, high, dic):
    ld = int(log10(low) + 1)
    hd = int(log10(high) + 1)
    
    ans = []
    
    if ld == hd:
        for num in dic[ld]:
            if low <= num <= high:
                ans.append(num)
        return ans
    else:
        for num in dic[ld]:
            if low <= num:
                ans.append(num)
                
        for d in range(ld+1, hd):
            ans += dic[d]
            
        for num in dic[hd]:
            if num <= high:
                ans.append(num)
        return ans
    
class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        dic = {}
        
        for d in range(2, 11):
            dic[d] = []
            D = 1

            while D <= 10-d:
                num = D
                curr = D
                
                while curr < D+d-1:
                    curr += 1
                    num *= 10
                    num += curr
                
                dic[d].append(num)
                D += 1
        
        # print(dic)
        ans = seqN(low, high, dic)
        return ans
        
                
        
