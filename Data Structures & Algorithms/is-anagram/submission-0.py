class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        if set(s) != set(t):
            return False
        letters = set(s)
        map_s = dict.fromkeys(letters, 0)
        map_t = dict.fromkeys(letters, 0)
        for i in range(len(s)):
            map_s[s[i]] += 1
            map_t[t[i]] += 1
        for l in letters:
            if map_s[l] != map_t[l]:
                return False
        return True
        