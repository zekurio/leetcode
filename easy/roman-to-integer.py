# https://leetcode.com/problems/roman-to-integer/

class Solution:
    def romanToInt(self, s: str) -> int:
        rom_dict = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        prev_num = 0
        res = 0

        for i in range(len(s)):
            curr_num = rom_dict[s[i]]
            if prev_num < curr_num:
                res += curr_num - 2 * prev_num
            else:
                res += curr_num
            prev_num = curr_num

        return res