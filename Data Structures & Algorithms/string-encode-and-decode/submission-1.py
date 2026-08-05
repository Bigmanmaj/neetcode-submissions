class Solution:
    delim = "~"
    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for s in strs:
            encoded += s + self.delim
        return encoded

    def decode(self, s: str) -> List[str]:
        decoded = []
        temp = ""
        for c in s:
            if c == self.delim:
                decoded.append(temp)
                temp = ""
            else:
                temp += c
        return decoded

