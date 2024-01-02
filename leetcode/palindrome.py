class Solution:
    def isPalindrome(self, x: int) -> bool:
        self.x = str(x)
        length = len(self.x)
        result = True
        i = 0
        j = 1
        for t in self.x:
            if self.x[i] != self.x[length - j]:
                result = False
                return result
            i += 1
            j += 1
        return result
