class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
       arr=[]
       nums.sort()

       while nums:
         ali=nums.pop(0)
         bob=nums.pop(0)
         arr.append(bob)
         arr.append(ali)

       return arr  
      
