# 1492. The kth Factor of n


class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        # List = []
        # for i in range(1,n+1):
        #     if k == 0:
        #         print(List)
        #         return List.pop()
        #     if n%i ==0 and k > 0:
        #         List.append(i)
        #         k -= 1
                
        # if k > 0:
        #     return -1
        # else:
        #     return List.pop()
            
        # divisors, sqrt_n = [], int(n**0.5)
        # for x in range(1, sqrt_n + 1):
        #     if n % x == 0:
        #         k -= 1
        #         divisors.append(x)
        #         if k == 0:
        #             return x
        
        # If n is a perfect square
        # we have to skip the duplicate 
        # in the divisor list
        if (sqrt_n * sqrt_n == n):
            k += 1
                
        n_div = len(divisors)
        return n // divisors[n_div - k] if k <= n_div else -1    