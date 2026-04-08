class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        sume=0
        sumd=0
        for i in nums:
            sume+=i
            n=i
            while n!=0:
               sumd+=n%10
               n=n//10
        return abs(sume-sumd)        
