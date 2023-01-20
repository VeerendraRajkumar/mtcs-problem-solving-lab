class Solution:
    def minOperations(self, logs: List[str]) -> int:
        h = 0
        for log in logs:
            if log == "../":
                if h > 0:
                    h -= 1
            elif log != "./":
                h += 1
        return h