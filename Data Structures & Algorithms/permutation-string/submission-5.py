class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        left = 0
        right = 0
        s1_dict = dict.fromkeys(set(s1), 0)
        s2_dict = {}
        for c in s1:
            s1_dict[c] += 1
        while right < len(s2):
            if s2[right] in s2_dict.keys():
                s2_dict[s2[right]] += 1
            else:
                s2_dict[s2[right]] = 1

            right += 1
            if right - left > len(s1):
                print(right)
                print(left)
                s2_dict[s2[left]] -= 1
                if s2_dict[s2[left]] == 0:
                    del s2_dict[s2[left]]
                left += 1
            print(s1_dict)
            print(s2_dict)
            if s1_dict == s2_dict:
                return True

        return False
            
        