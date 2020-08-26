# 412. Fizz Buzz

class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        a = []
        for i in range(1,n+1):
            if i%15 ==0:
                a.append('FizzBuzz')
            elif i%3 == 0:
                a.append('Fizz')
            elif i%5 == 0:
                a.append('Buzz')
            else:
                a.append(str(i))
        return a

        # res = [0] *n
        # for i in range(1,n+1):
        #     if i % 15 == 0:
        #         res[i-1] = "FizzBuzz"
        #     elif i % 3 == 0:
        #         res[i-1] = "Fizz"
        #     elif i % 5 == 0:
        #         res[i-1] = "Buzz"
        #     else:
        #         res[i-1] = str(i)
        # return res
        
        # return ["FizzBuzz" if i % 15 == 0 else "Fizz" if i % 3 == 0 else "Buzz" if i % 5 == 0 else str(i) for i in range(1,n+1)]
                
            