import math
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
       if num<1:
        return False
       a = int(math.sqrt(num))
       if a*a==num:
        return True
       else:
        return False  
