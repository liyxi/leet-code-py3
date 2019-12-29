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
