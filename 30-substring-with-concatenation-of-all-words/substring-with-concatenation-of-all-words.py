
class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not s or not words:
            return []

        count = len(words)
        h = {}

        for word in words:
            h[word] = h.get(word, 0) + 1

        wordLen = len(words[0])
        res = []

        for offset in range(wordLen):
            start = offset
            index = offset
            h2 = {}
            count1 = 0

            while start + wordLen <= len(s):
                st = s[start:start + wordLen]
                start += wordLen

                if st not in h:
                    h2 = {}
                    count1 = 0
                    index = start
                    continue

                h2[st] = h2.get(st, 0) + 1
                count1 += 1

                while h2[st] > h[st]:
                    left_word = s[index:index + wordLen]
                    h2[left_word] -= 1
                    count1 -= 1
                    index += wordLen

                if count1 == count:
                    res.append(index)

                    left_word = s[index:index + wordLen]
                    h2[left_word] -= 1
                    count1 -= 1
                    index += wordLen

        return res
