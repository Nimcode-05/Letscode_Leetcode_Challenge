class Solution:
    def returnToBoundaryCount(self, nums: List[int]) -> int:
        count=0
        bound=0
        for i in range(len(nums)):
            bound+=nums[i]  
            if bound==0:
               count+=1
        return count
