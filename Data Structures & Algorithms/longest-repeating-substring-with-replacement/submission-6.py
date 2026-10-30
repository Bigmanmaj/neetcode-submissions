class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        start = 0
        end = 0
        char_count = dict.fromkeys(set(s), 0)
        result = 0
        while end < len(s):
            max_char = max(char_count.values())
            if (end - start) - max_char > k:
                char_count[s[start]] -= 1  
                start += 1
            else:
                char_count[s[end]] += 1
                end += 1
            max_char = max(char_count.values())
            result = max(result, max_char + k)
        if result > len(s):
            result = len(s)
        return result
