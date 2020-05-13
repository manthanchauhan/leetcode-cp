class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        end = 2**n
        
        pset = []
        
        for i in range(0, end):
            set_ = []
            i_ = i
            bno = 0
            
            while i_:
                bit = i_%2
                i_ //= 2
        
                if bit:
                    set_.append(nums[bno])
                    
                bno += 1
                    
            pset.append(set_)
            
        return pset
