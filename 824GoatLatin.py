# 824. Goat Latin

class Solution:
    def toGoatLatin(self, S: str) -> str:
        # print(S.split(' '))
        # s = ''
        # for i,word in enumerate(S.split(' ')):
        #     # if word[0].lower() not in {'a','e','i','o','u'}:
        #     #     s += word[1:] + word[0] + 'ma' + 'a' * (i+1) + ' '
        #     # else:
        #     #     s += word[1:] + word[0] +  word  + 'ma' + 'a' * (i+1) + ' '
        #     s += word if word[0].lower() in {'a','e','i','o','u'} else word[1:] + word[0] 
        #     s += 'ma' + 'a' * (i+1) + ' '
        # s = s[0:-1]
        # return s
        
        return ' '.join([word +'ma' + 'a' * (i+1)  if word[0].lower() in {'a','e','i','o','u'} else word[1:] + word[0] +'ma' + 'a' * (i+1)  for i,word in enumerate(S.split(' ')) ])