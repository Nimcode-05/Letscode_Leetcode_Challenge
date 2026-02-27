import math
class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        if n%2==0:
           return math.lcm(n,2)
        else:
            return n*2 
          
