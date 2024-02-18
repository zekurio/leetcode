# https://leetcode.com/problems/longest-palindromic-substring/

class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if n == 0:
            return ""
        if n == 1:
            return s
        if n == 2:
            return s if s[0] == s[1] else s[0]
        
        max_len = 1
        start = 0
        
        for i in range(n):
            l, r = i, i
            while l >= 0 and r < n and s[l] == s[r]:
                if (r - l + 1) > max_len:
                    start = l
                    max_len = r - l + 1
                l -= 1
                r += 1
            
            l, r = i, i+1
            while l >= 0 and r < n and s[l] == s[r]:
                if (r - l + 1) > max_len:
                    start = l
                    max_len = r - l + 1
                l -= 1
                r += 1
                
        return s[start:start+max_len]