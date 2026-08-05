class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        opening = ['(', '{', '[']
        closing = [')', '}', ']']
        for c in s:
            if c in opening:
                stack.append(c)
            elif c in closing:
                if len(stack) > 0:
                    top = stack.pop()
                else:
                    return False
                c_index = closing.index(c)
                o_index = opening.index(top)
                if o_index != c_index:
                    return False
        return len(stack) == 0

        