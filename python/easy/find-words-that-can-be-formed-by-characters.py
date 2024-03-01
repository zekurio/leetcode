# https://leetcode.com/problems/find-words-that-can-be-formed-by-characters/

from typing import List

class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        occurences = {}
        result = 0
        for c in chars:
            if c in occurences:
                occurences[c] += 1
            else:
                occurences[c] = 1
        for word in words:
            good = True 
            d = {}
            for c in word:
                if c not in occurences:
                    good = False
                    break
                if c in d:
                    d[c] += 1
                    if d[c] > occurences[c]:
                        good = False
                        break
                else:
                    d[c] = 1
            if good:
                result += len(word)
        return result