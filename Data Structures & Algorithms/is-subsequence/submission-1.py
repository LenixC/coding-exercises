class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        s_p = 0
        t_p = 0
        if len(s) == 0:
            return True

        while t_p < len(t):
            if t[t_p] == s[s_p]:
                s_p += 1
            if s_p == len(s):
                return True
            t_p += 1
        
        return False