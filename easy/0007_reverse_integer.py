INT_MAX = (1<<31)-1
INT_MIN = -(1<<31)

class Solution:
    
    def reverse(self, x: int) -> int:
        minus = x < 0
        x = abs(x)
        y = 0
        while x != 0:
            y *= 10
            y += x % 10
            x //= 10
        if minus:
            y = -y
        # TODO: need a better method to identify overflow
        if y > INT_MAX or y < INT_MIN:
            return 0
        return y
