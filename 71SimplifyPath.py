71Simplify Path

class Solution:
    def simplifyPath(self, path: str) -> str:
        cache = path.split('/')
        # print(cache)
        i = 0
        while i < len(cache):
            if cache[i] == '' or cache[i] == '.':
                cache.pop(i)
            elif cache[i] == '..':
                cache.pop(i)
                if i>=1:
                    i -= 1
                    cache.pop(i)
            else:
                i += 1
        
        cache.insert(0,'') 
        if len(cache) == 1:
            cache.append('')

        
        # print(cache)
                
        return '/'.join(cache)