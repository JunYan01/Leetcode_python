966  Vowel Spellchecker

class Solution:
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
        org = dict()
        low = dict()
        vow = dict()
        for w in wordlist:
            org[w] = w
            l = w.lower()
            if l not in low: low[l] = w
            v = re.sub(r'[aeiou]', '*', l)
            if v not in vow: vow[v] = w
        ans = []
        for q in queries:
            if q in org:
                ans.append(q)
                continue
            l = q.lower()
            if l in low:
                ans.append(low[l])
                continue
            v = re.sub(r'[aeiou]','*',l)
            if v in vow:
                ans.append(vow[v])
                continue
            ans.append("")
        return ans