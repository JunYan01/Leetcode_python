# 1286. Iterator for Combination


class CombinationIterator:

    def __init__(self, characters: str, combinationLength: int):
        self.combinations = []
        n, k = len(characters), combinationLength
        
        # generate bitmasks from 0..00 to 1..11  
        print(1<<n)
        for bitmask in range(1 << n):
            # use bitmasks with k 1-bits
            if bin(bitmask).count('1') == k:
                # convert bitmask into combination 
                # bitmask & (1 << i) check i-th position of bitmask to be 1
                # 111 --> "abc", 000 --> ""
                # 110 --> "ab", 101 --> "ac", 011 --> "bc"
                curr = [characters[j] for j in range(n) if bitmask & (1 << n - j - 1)]       
                self.combinations.append(''.join(curr))

    def next(self) -> str:
        return self.combinations.pop()
        

    def hasNext(self) -> bool:
        return self.combinations
        


# Your CombinationIterator object will be instantiated and called as such:
# obj = CombinationIterator(characters, combinationLength)
# param_1 = obj.next()
# param_2 = obj.hasNext()