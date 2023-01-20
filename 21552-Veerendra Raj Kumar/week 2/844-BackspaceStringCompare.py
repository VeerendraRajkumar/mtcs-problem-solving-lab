# Solution using yield method of python

class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def BEST(s: str):# BEST stands for Build Effective STring
            skip=0
            for l in reversed(s):
                if l =='#':
                    skip+=1
                elif skip:
                    skip-=1
                else:
                    yield l
        return all(x == y for x,y in itertools.zip_longest(BEST(s), BEST(t))) # py3 version
        # return all(x == y for x,y in itertools.izip_longest(BEST(s), BEST(t))) # py2 version