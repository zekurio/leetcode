# https://leetcode.com/problems/least-number-of-unique-integers-after-k-removals/

from typing import List
from collections import Counter

class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        counter = Counter(arr)
        freq = sorted(counter.values())
        i = 0
        while i < len(freq) and k >= freq[i]:
            k -= freq[i]
            i += 1
        return len(freq) - i