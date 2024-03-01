# https://leetcode.com/problems/cheapest-flights-within-k-stops/

from typing import List

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        inf = float('inf')
        dp = [inf for _ in range(n)]
        dp[src] = 0
        for _ in range(k + 1):
            temp = dp[:]
            for u, v, w in flights:
                temp[v] = min(temp[v], dp[u] + w)
            dp = temp
        return dp[dst] if dp[dst] < inf else -1