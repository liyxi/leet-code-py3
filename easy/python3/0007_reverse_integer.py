"""
Given a 32-bit signed integer, reverse digits of an integer.

Example 1:

Input: 123
Output: 321

Example 2:

Input: -123
Output: -321

Example 3:

Input: 120
Output: 21

Note:
    Assume we are dealing with an environment which could only store integers
    within the 32-bit signed integer range: [−231,  231 − 1]. For the purpose of
    this problem, assume that your function returns 0 when the reversed integer
    overflows.
"""

"""
Note:
 Input      -> Output       # Comment
 1563847412 -> 0            # overflow
-1563847412 -> 0            # overflow
"""

INT_MAX = (1<<31)-1
INT_MIN = -(1<<31)

INT_MAX_DIV_10 = int(INT_MAX / 10)
INT_MIN_DIV_10 = int(INT_MIN / 10)

class Solution:

    def reverse(self, x: int) -> int:
        # is x negative
        negative = x < 0
        # save reversed integer in y
        y = 0
        while x != 0:
            # pop last digit from x
            pop = abs(x) % 10
            if negative:
                pop = -pop
            # remove last digit of x
            x = int(x/10)
            # whether y will overflow
            if y > INT_MAX_DIV_10 or (y==INT_MAX_DIV_10 and pop > 7):
                return 0
            if y < INT_MIN_DIV_10 or (y==INT_MIN_DIV_10 and pop < -8):
                return 0
            # push last digit to y
            y = y * 10 + pop
        return y
