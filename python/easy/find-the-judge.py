# https://leetcode.com/problems/find-the-town-judge/

from typing import List

class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        trusts = [0] * (n + 1)
        is_trusted = [0] * (n + 1)

        for a, b in trust:
            trusts[a] += 1
            is_trusted[b] += 1

        for i in range(1, n + 1):
            if trusts[i] == 0 and is_trusted[i] == n - 1:
                return i

        return -1