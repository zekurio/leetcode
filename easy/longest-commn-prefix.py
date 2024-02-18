# https://leetcode.com/problems/longest-common-prefix/description/

from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        if len(strs) == 1:
            return strs[0]
        
        shortest_str = min(strs, key=len)
        
        for i in range(len(shortest_str)):
            for string in strs:
                if string[i] != shortest_str[i]:
                    return shortest_str[:i]
        
        return shortest_str