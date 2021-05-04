12Integer to Roman

class Solution:
    def intToRoman(self, num: int) -> str:
        # dic = {1:'I',5:'V',10:'X',50:'L',100:'C',500:'D',1000:'M'}
        dic = list(zip([1,5,10,50,100,500,1000],['I','V','X','L','C','D','M']))
        res = ''
        # print(dic)
        i = 6
        while num > 0:
            if num >= dic[i][0]:
                res += dic[i][1]
                num -= dic[i][0]
                continue
            if num >= dic[i][0] - dic[i-2+i%2][0]:
                res += dic[i-2+i%2][1]
                res += dic[i][1]
                num -= dic[i][0] - dic[i-2+i%2][0]
                continue
            i -= 1    
        return res