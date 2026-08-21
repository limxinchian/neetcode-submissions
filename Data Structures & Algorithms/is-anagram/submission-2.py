class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        check = {}

        if len(s) != len(t):
            return False

        for char in s:
            check[char] = check.get(char, 0) + 1

        for char in t:
            check[char] = check.get(char, 0) - 1

        for i in check.values(): 
            if i != 0:
                return False

        return True