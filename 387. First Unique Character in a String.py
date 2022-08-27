class Solution:
    def firstUniqChar(self, s: str) -> int:
        store = {}
        for c in s:
            if c not in store:
                store[c] = 0 
            else:
                store[c] = 1
        for i,c in enumerate(s):
            if store[c] == 0:
                return i
        return -1
