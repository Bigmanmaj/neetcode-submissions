class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        string_set = set()
        l = 0
        length = 0
        for i in range(len(s)):
            r = i
            if s[r] in string_set:
                while s[r] in string_set:
                    string_set.remove(s[l])
                    l += 1
            length = max(r - l + 1, length)
            string_set.add(s[r])
        return length