
class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]: 
        n = len(s)
        wordLen = len(words[0])
        count1 = len(words)

        if n < wordLen * count1:
            return []

        h1 = {}
        for word in words:
            h1[word] = h1.get(word, 0) + 1
        
        res = []

        for begin in range(wordLen):
            start = begin
            index = begin
            h2 = {}
            count2 = 0

            while start + wordLen <= n:
                st = s[start : start + wordLen]
                start += wordLen

                if st not in h1:
                    h2 = {}
                    count2 = 0
                    index = start
                    continue
                
                h2[st] = h2.get(st, 0) + 1
                count2 += 1

                while h2[st] > h1[st]:
                    leftWord = s[index : index + wordLen]
                    h2[leftWord] -= 1
                    count2 -= 1
                    index += wordLen
                
                while count1 == count2:
                    res.append(index)

                    leftWord = s[index : index + wordLen]
                    h2[leftWord] -= 1
                    count2 -= 1
                    index += wordLen
        return res

        
        

        
