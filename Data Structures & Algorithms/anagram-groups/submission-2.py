class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}
        output = []
        for s in strs:
            char_count = [0 for i in range(26)]
            for c in s:
                char_count[ord(c) - 97] += 1
            if str(char_count) not in groups.keys():
                groups[str(char_count)] = [s]
            else:
                groups[str(char_count)].append(s)
        for v in groups.values():
            output.append(v)
        return output
            
