277Find the Celebrity

# The knows API is already defined for you.
# return a bool, whether a knows b
# def knows(a: int, b: int) -> bool:

class Solution:
    def findCelebrity(self, n: int) -> int:
        queue = list(range(n))
        discard = []
        while len(queue) > 1:
            x, y= queue.pop(), queue.pop()
            if knows(x,y) == 1:
                discard.append(x)
                queue.append(y)
            else:
                discard.append(y)
                queue.append(x)
        
        # print(queue)
        
        # return queue[0] if (all([knows(x,queue[0]) for x in range(n) if x!= queue[0]]) and not (any([knows(queue[0],x) for x in range(n) if x!= queue[0]]))) else -1
        # return queue[0] if (all([knows(x,queue[0]) for x in discard]) and not (any([knows(queue[0],x) for x in discard ]))) else -1
        return queue[0] if all([knows(x,queue[0]) and not knows(queue[0],x) for x in discard]) else -1