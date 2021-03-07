752  Open the Lock

class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
#         Not correct 
#         if '0000' in deadends:
#             return -1
#         l = len(target)
#         print(l)
#         deadends = set(deadends)
#         s1 = {'0000'}
#         s2 = {target}
#         step = 0
        
        
#         while len(s1) > 0 and len(s2) > 0:
#             step += 1
#             if len(s1) > len(s2): s1, s2 = s2, s1
#             s = set()   
#             for w in s1:
#                 new_words = []
#                 for i in range(l):
#                     for t in [str((int(w[i])+x)%10) for x in {1,9}]:
#                         new_words.append(w[:i] + t + w[i+1:])
#                 # new_words = [
#                 #     w[:i] + t + w[i+1:]  for t in [str((int(w[i])+x)%10) for x in {1,9}] for i in range(l)]
#                 for new_word in new_words:
#                     if new_word in deadends: continue
#                     if new_word in s2:  return step 
#                     s.add(new_word)
#             if len(s) == len(s1):
#                 return -1
#             s1 = s
            
#         return -1
        if '0000' in deadends:
            return -1
        if target == "0000":
            return 0
        l = len(target)
        # print(l)
        deadends = set(deadends)
        s1 = ['0000']
        s1All = s1
        s2 = [target]
        s2All = s2
        step = 0
        while True:
            step += 1
            l1 = []  
            for w in s1:
                new_words = []
                for i in range(l):
                    for t in [str((int(w[i])+x)%10) for x in {1,9}]:
                        new_words.append(w[:i] + t + w[i+1:])
                for new_word in new_words:
                    if new_word in deadends or new_word in s1All or new_word in l1: continue
                    if new_word in s2:  return step 
                    l1.append(new_word)
            # print(l1)
            if len(l1) == 0:
                return -1
            s1 = l1
            s1All.extend(l1)
            
            step += 1
            l2 = [] 
            for w in s2:
                new_words = []
                for i in range(l):
                    for t in [str((int(w[i])+x)%10) for x in {1,9}]:
                        new_words.append(w[:i] + t + w[i+1:])
                for new_word in new_words:
                    if new_word in deadends or new_word in s2All or new_word in l2: continue
                    if new_word in s1:  return step 
                    l2.append(new_word)
            # print(l2)
            if len(l2) == 0:
                return -1
            s2 = l2
            s2All.extend(l2)

