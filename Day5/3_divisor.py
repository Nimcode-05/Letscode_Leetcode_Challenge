import math

class Solution:
    def isprime(n):
        if n > 1 and all(n % i for i in range(2, int(math.sqrt(n)) + 1)):
           return True
        else:   
           return False


    def isThree(self, n: int) -> bool:
        root = math.isqrt(n)
        if n==root*root :
            return Solution.isprime(root)
                
        else:
            return False          
