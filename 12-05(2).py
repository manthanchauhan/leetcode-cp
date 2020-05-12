class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        perms = [list(nums)]
        n = len(nums)
        
        if n <= 1:
            return perms
        
        while True:
            # find i
            i = None
            
            for i_ in range(n-2, -1, -1):
                if nums[i_] < nums[i_+1]:
                    i = i_
                    break
                    
            if i is None:
                break
            
            # find j
            j = None
            
            for j_ in range(n-1, i, -1):
                if nums[j_] > nums[i]:
                    j = j_
                    break
                    
            nums[i], nums[j] = nums[j], nums[i]
            aftrI = nums[i+1:]
            nums = nums[:i+1] + aftrI[::-1]
            
            perms.append(list(nums))
            
        return perms
                    
            
        
