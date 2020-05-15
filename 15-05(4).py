class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        beg = 0
        n = len(nums)
        end = 2**n
        
        ans = []
        for num in range(beg, end):
            num_ = num
            st = []
            
            for ind in range(0, n):
                bit = num_%2
                num_ //= 2
                
                if bit:
                    st.append(nums[ind])
            
            st.sort()
            
            if st not in ans:
                ans.append(st)
            
        return ans
                
