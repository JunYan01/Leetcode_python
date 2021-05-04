423  Reconstruct Original Digits from English

class Solution:
    def originalDigits(self, s: str) -> str:
        # dic = {'zero':0, 'one':1, 'two': 2, 'three':3, 'four':4, 'five':5, 'six':6, 'seven': 7, 'eight':8, 'nine':9}
        # z 0
        # g 8
        # w 2
        # u 4
        # x 6
        
        # o 1
        # h 3
        # f 5
        # s 7
        
        # i 9
        keys = ['zero','one','two','three','four','five','six','seven','eight','nine']
        vals = range(10)
        check_seq = ['z','g','w','u','x','o','h','f','s','i']
        check_num = [0, 8, 2, 4, 6, 1, 3, 5, 7, 9]
        
        
        dic = dict(zip(vals,keys))
        words = [dic[i] for i in check_num]
        
        print(dic)
        res = []
        count = [0]*26
        # print(ord('a'))
        for c in s:
            count[ord(c) - 97] += 1
        
        print(count)
        for i in range(10):
            cnt = count[ord(check_seq[i]) - 97]
            for c in words[i]:
                count[ord(c) - 97] -= cnt
            # print(res,cnt,words[i],'a')
            while cnt >0:
                res.append(check_num[i])
                cnt -= 1
            # print(res,cnt,'b')
        print(res)
        res.sort()
        print(res)
        return ''.join([str(c) for c in res])

        