
class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]: 
        n = len(s)
        wordLen = len(words[0])
        count = len(words)

        if n < wordLen * count:
            return []
        
        h = {}
        for word in words:
            h[word] = h.get(word, 0) + 1
        
        res = []

        for start in range(wordLen):
            first = start
            index = start
            h1 = {}
            count1 = 0

            while first + wordLen <= n:
                st = s[first : first + wordLen]
                first += wordLen

                if st not in h:
                    index  = first
                    h1 = {}
                    count1 = 0
                    continue
                
                h1[st] = h1.get(st, 0) + 1
                count1 += 1

                while h1[st] > h[st]:
                    left_word = s[index : index + wordLen]
                    h1[left_word] -= 1
                    count1 -= 1
                    index += wordLen
                
                while count1 == count:
                    res.append(index)

                    left_word = s[index : index + wordLen]
                    h1[left_word] -= 1
                    count1 -= 1
                    index += wordLen
        return res
        

        
