class Solution:
    def maxDepth(self, s: str) -> int:
        h, d = 0, 0
        for l in s:
            if l == '(':
                h += 1
                d = max(d, h)
            elif l == ')':
                h -= 1
        return d